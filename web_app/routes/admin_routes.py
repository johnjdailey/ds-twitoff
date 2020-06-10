# web_app/routes/admin_routes.py



from flask import Blueprint, jsonify, request, render_template, flash, redirect

from web_app.models import db


API_KEY = "abc123" # TODO: set as secret env var


admin_routes = Blueprint("admin_routes", __name__)

# GET /admin/db/reset?api_key=abc123
@admin_routes.route("/admin/db/reset")
def reset_db():
    print("URL PARMS", dict(request.args))

    if "api_key" in dict(request.args) and request.args["api_key"] == API_KEY:
        print(type(db))
        db.drop_all()
        db.create_all()
        return jsonify({"message": "DB RESET OK"})
    else:
        flash("OOPS Permission Denied", "danger")
        return redirect("/users")

@admin_routes.route("/admin/db/seed")
def seed_db():
    print(type(db))
    # TODO: refactor the existing user and tweet storage logic from our twitter_routes into a re-usable function
    # ... so we can "seed" our database with some example users and tweets
    # ... to ensure that it is ready to make predictions later
    
    # FYI: you might run into Timeout errors, which you'll need to think about how to avoid

    return jsonify({"message": "DB SEEDED OK (TODO)"})
