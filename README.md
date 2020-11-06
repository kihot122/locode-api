In order to build use: docker build -t [mytag] ./[path-to-repo] <br />
This application implements custom command 'getdb' use with: <br />
python manage.py getdb <br />
This command will run initially to set up a database while building docker image. <br />

This will download up-to-date file from UNECE and parse it into database. <br />
THIS COMMAND WILL ERASE ANY DATA THAT WAS PREVIOUSLY STORED INSIDE THE DATABASE, USE WITH CAUTION. <br />

For serving dynamic content, ex. api requests, this server uses uwsgi. <br />

This API has following endpoints: <br />
/api/namewodiacritics/<str> #Browsing locations by their NameWoDiacritics entry, example: /api/namewodiacritics/Pekin <br />
/api/locode/<str>           #Get single entry by LOCODE, example: /api/locode/ADEAC <br />
