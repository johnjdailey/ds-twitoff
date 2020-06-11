# web_app/routes/stats_routes.py



# Adding a route to implement our model to make predictions


from flask import Blueprint, request, jsonify, render_template

from sklearn.linear_model import LogisticRegression # for example

from web_app.models import User, Tweet
#from web_app.iris_classifier import load_model
from web_app.services.basilica_service import connection as basilica_connection


stats_routes = Blueprint("stats_routes", __name__)

@stats_routes.route("/predict", methods=["POST"])
def predict():
    print("PREDICT ROUTE...")
    print("FORM DATA:", dict(request.form))
    #> {'screen_name_a': 'elonmusk', 'screen_name_b': 's2t2', 'tweet_text': 'Example tweet text here'}
    screen_name_a = request.form["screen_name_a"]
    screen_name_b = request.form["screen_name_b"]
    tweet_text = request.form["tweet_text"]


    # Fetch users and tweets from the database

    #print("-----------------")
    #print("FETCHING TWEETS FROM THE DATABASE...")
    ## todo: wrap in a try block in case the user's don't exist in the database
#
#
    ## Filter so that we select only the username equal to screen_name_a (the first one the user picked on the form)
#
    #user_a = User.query.filter(User.screen_name == screen_name_a).one() # try: .first()
    #user_b = User.query.filter(User.screen_name == screen_name_b).one() # also try: one or none() # no error handling required
#
#
    # # Select only tweets from user a and user b
#
    #user_a_tweets = user_a.tweets
    #user_b_tweets = user_b.tweets

    #user_a_embeddings = [tweet.embedding for tweet in user_a_tweets]
    #user_b_embeddings = [tweet.embedding for tweet in user_b_tweets]
   #print("USER A", user_a.screen_name, len(user_a.tweets))
   #print("USER B", user_b.screen_name, len(user_b.tweets))

   #print("-----------------")
   #print("TRAINING THE MODEL...")
   #embeddings = []
   #labels = []

   #for tweet in user_a_tweets:
   #    labels.append(user_a.screen_name)
   #    embeddings.append(tweet.embedding)

   #for tweet in user_b_tweets:
   #    labels.append(user_b.screen_name)
   #    embeddings.append(tweet.embedding)

   #classifier = LogisticRegression() # for example
   #classifier.fit(embeddings, labels)

   #print("-----------------")
   #print("MAKING A PREDICTION...")

   ##result_a = classifier.predict([user_a_tweets[0].embedding])
   ##result_b = classifier.predict([user_b_tweets[0].embedding])
   ##results = classifier.predict([embeddings[0]])[0] #> elon

   #
   ## Use Basilica connection to embed input tweet, use Basilica model trained on twitter
   #example_embedding = basilica_connection.embed_sentence(tweet_text, model="twitter")
   #result = classifier.predict([example_embedding])
    #breakpoint()


    # Direct user to prediction result page after running prediction
    
    #return jsonify({"message": "RESULTS", "most_likely": result[0]})
    return render_template("prediction_results.html",
        screen_name_a=screen_name_a,
        screen_name_b=screen_name_b,
        tweet_text=tweet_text,
        screen_name_most_likely= "TODO" #result[0]
    )
    