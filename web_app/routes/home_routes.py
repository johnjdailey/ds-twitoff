# web_app/routes/home_routes.py



from flask import Blueprint, render_template
from web_app.models import User

# Define home routes
home_routes = Blueprint("home_routes", __name__)

# Decorating the home routes object
# Adding routes to our blueprint object we called home_routes

# When the user visits the home page
@home_routes.route("/")
def index():
    #print("Twittoff Home Page!")
    users = User.query.all()
    usernames = [user.screen_name for user in users]
    return render_template("prediction_form.html", users=usernames)


# When the user visits /about
@home_routes.route("/about")
def about():
    print("VISITING THE ABOUT PAGE")
    return "This is the Twittoff App!"
