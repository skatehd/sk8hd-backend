# This is the backend for the hd skateboarding website


## To build: 

Create a virtualenv: 
```
python3 -m venv venv
```

Acitvate: 
```
source venv/bin/activate
```

Install the requirements: 
```
pip install -r requirements.txt
```

Make and run the migrations: 
```
python manage.py makemigrations
python manage.py migrate
```

When testing you need to add GIS extensions to sqlite: 
```
apt install libsqlite3-mod-spatialite
```

### For production: 

A file named 'secrets.json' in the root folder is required, if the file is found, the project will run in production mode.  
The file has to contain any secrets, and some settings: 

SECRET_KEY
EMAIL_HOST
EMAIL_USER
EMAIL_PASSWORD
ALLOWED_HOSTS
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD

The Database and Python has to support Geo things: 
```
apt install gdal-bin libgdal-dev python3-gdal binutils libproj-dev
```

Then add PostGis extension: 

```
apt install postgis
```

Run the SQL in the database to sctivate postgis: 
```
su postgres
psql <db name>
CREATE EXTENSION postgis;
```