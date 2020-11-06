In order to build use: docker build -t [mytag] ./[path-to-repo]
This application implements custom command 'getdb' use with:
python manage.py getdb
This command will run initially to set up a database while building docker image.

This will download up-to-date file from UNECE and parse it into database. THIS COMMAND WILL ERASE ANY DATA THAT WAS PREVIOUSLY STORED INSIDE THE DATABASE, USE WITH CAUTION.

For serving dynamic content, ex. api requests, this server uses uwsgi.

This API has following endpoints:
/api/namewodiacritics/<str> #Browsing locations by their NameWoDiacritics entry, example: /api/namewodiacritics/Pekin
/api/locode/<str>           #Get single entry by LOCODE, example: /api/locode/ADEAC
