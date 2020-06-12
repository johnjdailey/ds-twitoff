# twitoff-pt5


# Installation

```sh
git clone git@github.com:johnjdailey/twitoff-pt5.git
cd twitoff-pt5/
```

# Setup

```sh
pipenv install
```

# Change Directories

cd web_app

# Run Flask

# Mac:
FLASK_APP=web_app flask run

# Windows:
set FLASK_APP=web_app # one-time thing, to set the env var
flask run

# Migration for DB

Windows users can omit the "FLASK_APP=web_app" part...

```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```

# Usage

```sh
FLASK_APP=web_app flask run

or, in Windows just use: flask run
```

Home Page: http://127.0.0.1:5000/

About Page: http://127.0.0.1:5000/about

Tweets Page: http://127.0.0.1:5000/tweets

New Tweets Page: http://127.0.0.1:5000/tweets/new

Users Page: http://127.0.0.1:5000//users/<screen_name> 
    
    (replace <screen_name> with a twitter handle to add
    that user's twitter data to the SQLite DB for further
    analysis)


# Example Database URLs for local SQLite DB:

local .env file...

mac:

DATABASE_URL="sqlite:////Users/YOURUSERNAME/Desktop/my-web-app-12/web_app/web_app_12.db"

windows:

DATABASE_URL="sqlite:///C:\\Users\\YOURUSERNAME\\Desktop\\TwitterApp\\web_app\\web_app_200.db"


# Provisioning production database:

```heroku config```
```heroku addons:create heroku-postgresql:hobby-dev```
#> provisions a new DATABASE_URL
```heroku config```


# Migrating the production database:

first login to the server, then run the migration commands there:

```heroku run bash```

 ... ```FLASK_APP=web_app flask db init```
 ... ```FLASK_APP=web_app flask db migrate```
 ... ```FLASK_APP=web_app flask db upgrade```

that should work, but alternatively you might be able to run these detached commands (if you didn't ignore your migrations dir):

```heroku run "FLASK_APP=web_app flask db init```
```heroku run "FLASK_APP=web_app flask db stamp head```
```heroku run "FLASK_APP=web_app flask db migrate```
```heroku run "FLASK_APP=web_app flask db upgrade```

# Connecting to a Postgres Database (from Table Plus or another DBMS)

postgres://USERNAME:PASSWORD@HOST:5432/DB_NAME


# Configuring production environment variables:

```heroku config```
```heroku config:set ALPHAVANTAGE_API_KEY="_____"```
```heroku config:set BASILICA_API_KEY="_____"```
```heroku config:set TWITTER_API_KEY="_____"```
```heroku config:set TWITTER_API_SECRET="______"```
```heroku config:set TWITTER_ACCESS_TOKEN="______"```
```heroku config:set TWITTER_ACCESS_TOKEN_SECRET="_____"```
```heroku config```
