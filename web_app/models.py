# web_app/models.py



from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()


migrate = Migrate()


class User(db.Model):
    """Twitter Users"""
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(15), nullable=False)
    location = db.Column(db.String)
    followers_count = db.Column(db.Integer)
    #latest_tweet_id = db.Column(db.BigInteger)

    #def __repr__(self):
    #    return f"<User {self.id} {self.title}>"


# Set a user.id as a foreign key
# Create an embedding attribute, we will need this when using the Basilica api
class Tweet(db.Model):
    """Tweets"""
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"), nullable=False)
    full_text = db.Column(db.Unicode(500))
    embedding = db.Column(db.PickleType, nullable=False)

    user = db.relationship("User", backref=db.backref("tweets", lazy=True))

    #def __repr__(self):
    #    return f"<Tweet {self.id}>" # self.id just returns bullets #{self.title} there is no self.title


def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON
    Param: database_records (a list of db.Model instances)
    Example: parse_records(User.query.all())
    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Tweet 1"},
            {"id": 2, "title": "Tweet 2"},
            {"id": 3, "title": "Tweet 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records
    