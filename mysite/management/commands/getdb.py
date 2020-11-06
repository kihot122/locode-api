from datetime import datetime
from mysite.models import Location
from django.core.management.base import BaseCommand
from django.core.management import call_command

import requests
import zipfile
import csv
import glob
import pathlib

class Command(BaseCommand):
    help = "Downloads up to date database from server"

    def handle(self, *args, **options):
        self.stdout.write("Downloading database file")
        
        url = "http://www.unece.org/fileadmin/DAM/cefact/locode/loc201csv.zip"
        req = requests.get(url)
        open("file.zip", "wb").write(req.content)

        self.stdout.write("Unpacking")
        zipfile.ZipFile("file.zip", "r").extractall("temp")

        self.stdout.write("Flushing database")
        call_command("flush", "--noinput")

        tab = []

        for filepath in glob.iglob("temp/*UNLOCODE*.csv"):
            print("Applying " + filepath)
            with open(filepath, encoding = "ISO-8859-1") as file:
                reader = csv.reader(file, delimiter = ',')
                for row in reader:
                    try:
                        tab.append(Location(
                            LOCODE = (row[1] + row[2]),
                            NameWoDiacritics = row[4],
                            Port = True if row[6][0] == '1' else False,
                            RailwayTerminal = True if row[6][1] == '2' else False,
                            RoadTerminal = True if row[6][2] == '3' else False,
                            Airport = True if row[6][3] == '4' else False,
                            PostalExchange = True if row[6][4] == '5' else False,
                            MultimodalFunction = True if row[6][5] == '6' else False,
                            FixedTransportFunction = True if row[6][6] == '7' else False,
                            BorderCrossing = True if row[6][7] == 'B' else False,
                            Unknown = True if row[6][0] == '0' else False,
                            Date = datetime.strptime(row[8], "%y%m"),
                            Coords = row[10]
                        ))
                    except:
                        pass
        
        self.stdout.write("Writing to database")
        Location.objects.bulk_create(tab)

        self.stdout.write("Cleaning up...")
        for filepath in glob.iglob("temp/*"):
            pathlib.Path(filepath).unlink()
        pathlib.Path("temp").rmdir()
        pathlib.Path("file.zip").unlink()

        self.stdout.write("Downloaded and applied up to date database")
