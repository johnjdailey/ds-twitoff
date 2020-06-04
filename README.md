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

Migrate the database:

Windows users can omit the "FLASK_APP=web_app" part...

```sh
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```

# Usage

```sh
FLASK_APP=web_app flask run
```