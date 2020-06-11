# web_app/routes/twitter_routes.py


  
# Add twitter route for inclass app, tells the website what to do


# Imports
from flask import Blueprint, render_template, jsonify, request, flash, redirect

# Import connections to Twitter and Basilica from service pages we set up
from web_app.services.twitter_service import api as twitter_api_client
from web_app.services.basilica_service import connection as basilica_api_client

# Import models we created from the models page
from web_app.models import db, User, Tweet, parse_records


# Define twitter route, tie to app
twitter_routes = Blueprint("twitter_routes", __name__)


# Tell the website what to do
@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)


    # Use the input screen name to get user info and save as attributes of twitter_user
    # (using get_user method on twitter api)
    twitter_user = twitter_api_client.get_user(screen_name)

    # Use the input screen name to get latest tweets (using user_timeline method on twitter_api)
    #  exclude_replies=True, include_rts=False - excludes replies and retweets - causes a different amount of tweets per user

    # Collect 150 latest tweets from each user
    statuses = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=150)
    print("STATUSES COUNT:", len(statuses))
    #return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})


    ## ADD USER TABLE INFORMATION TO DB
    # Get existing user from the db or initialize a new one if it doesn't exist yet:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count


    # Add and commit changes to the database user table
    db.session.add(db_user)
    db.session.commit()
    #return "OK"
    #breakpoint()


    ## ADD TWEETS TO TWEET TABLE IN DB
    # List comprehension to create a list of strings to feed to Basilica model
    all_tweet_texts = [status.full_text for status in statuses]


    # Use Basilica to embed the written words of the tweets as numeric values
    # Define twitter specific model for Basilica to use
    embeddings = list(basilica_api_client.embed_sentences(all_tweet_texts, model="twitter"))
    print("NUMBER OF EMBEDDINGS", len(embeddings))


    # Store each tweet in the database
    # For each tweet in the list of tweets pulled from the twitter api above and stored as statuses
    counter = 0
    for status in statuses:
        print(status.full_text)
        print("----")

        # Get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)
        

        # Set user_id and the full text of the tweet attribute of instance
        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.full_text = status.full_text


        #embedding = basilica_connection.embed_sentence(status.full_text, model="twitter") # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet
        #embedding = embeddings[counter]
        #print(len(embedding))


        # Set the corresponding embedding from our list of embeddings
        db_tweet.embedding = embeddings[counter]


        # Add the tweet to the database
        db.session.add(db_tweet)


        # We are using the counter to identify the series of tweets
        counter+=1


    # Commit changes to database table
    db.session.commit()
    #breakpoint()
    

    # This is what the front end website will see
    #return "User added"
    return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets


# Define new_user route
@twitter_routes.route("/users/new")
def new_user():
    return render_template("new_user.html")


# Define users/create route
@twitter_routes.route("/users/create", methods=["POST"])
def create_user():

    screen_name = request.form['screen_name']
     # Use the input screen name to get user info and save as attributes of twitter_user
    # (using get_user method on twitter api)
    twitter_user = twitter_api_client.get_user(screen_name)

    
    # Use the input screen name to get latest tweets (using user_timeline method on twitter_api)
    #  exclude_replies=True, include_rts=False - excludes replies and retweets - causes a different amount of tweets per user


    # Collect 150 latest tweets from each user
    statuses = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=150)
    

    ## ADD USER TABLE INFORMATION TO DB
    # Get existing user from the db or initialize a new one if it doesn't exist yet:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)


    # Set attributes for db user equal to info gathered from twitter
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count


    # Add and commit changes to the database user table
    db.session.add(db_user)
    db.session.commit()


    ## ADD TWEETS TO TWEET TABLE IN DB
    # List comprehension to create a list of strings to feed to Basilica model
    all_tweet_texts = [status.full_text for status in statuses]


    # Use Basilica to embed the written words of the tweets as numeric values
    # Define twitter specific model for Basilica to use
    embeddings = list(basilica_api_client.embed_sentences(all_tweet_texts, model="twitter"))
    print("NUMBER OF EMBEDDINGS", len(embeddings))


    # Store each tweet in the database
    # For each tweet in the list of tweets pulled from the twitter api above and stored as statuses
    counter = 0
    for status in statuses:
        print(status.full_text)
        print("----")
        

        # Get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(status.id) or Tweet(id=status.id)


        # Set user_id and the full text of the tweet attribute of instance
        db_tweet.user_id = status.author.id 
        db_tweet.full_text = status.full_text
        

        # Set the corresponding embedding from our list of embeddings
        db_tweet.embedding = embeddings[counter]


        # Add the tweet to the database
        db.session.add(db_tweet)


        # We are using the counter to identify the series of tweets
        counter+=1


    # Commit changes to database table
    db.session.commit()


    # This is what the front end website will see
    # Can customize this to include the data that we saved to the database
    flash(f"User '{db_user.screen_name}' created successfully!", "success")
    return redirect("/")
    