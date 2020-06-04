# web_app/routes/home_routes.py



from flask import Blueprint


home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    print("VISITING THE HOME PAGE")
    return "Twittoff Home Page!"


@home_routes.route("/about")
def about():
    print("VISITING THE ABOUT PAGE")
    return "This is the Twittoff App!"
