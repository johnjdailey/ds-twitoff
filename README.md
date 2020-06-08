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
