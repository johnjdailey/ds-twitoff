# web_app/__init__.py



# Entry point into a directory
# Tells the website to run the app
# Define app, tell it the routes to use
# all the supporting code is on other pages that this refers to


import os
from dotenv import load_dotenv
from flask import Flask, session
from web_app.models import db, migrate


# Import all of the routes that we have created so the app can run them

from web_app.routes.admin_routes import admin_routes
from web_app.routes.home_routes import home_routes
from web_app.routes.tweet_routes import tweet_routes
from web_app.routes.twitter_routes import twitter_routes
from web_app.routes.stats_routes import stats_routes
#from web_app.routes.iris_stats_routes import iris_stats_routes


load_dotenv()


# Set a path to the database we will be using to store the data
# Do not need to create the page, it will be created automatically by the app

# Fine when running locally

DATABASE_URI = os.getenv("DATABASE_URI")
SECRET_KEY = os.getenv("SECRET_KEY")


# Set up for heroku web app to work

#DATABASE_URI = 
#SECRET_KEY = os.getenv("SECRET_KEY", default="super secret key")


# Initialize app

def create_app():
    app = Flask(__name__)
    #app.config["SECRET_KEY"] = SECRET_KEY

    # Configure the database

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    #app.config['SECRET_KEY'] = SECRET_KEY # prevents cookies to be modified
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    # Configure routes - register each route we have with the app

    app.register_blueprint(admin_routes)
    app.register_blueprint(home_routes)
    app.register_blueprint(tweet_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(stats_routes)
    #app.register_blueprint(iris_stats_routes)

    return app


# Create instance of our app and return our app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
