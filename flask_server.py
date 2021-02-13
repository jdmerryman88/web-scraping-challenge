from flask import Flask, render_template, redirect
from pymongo import MongoClient
import scrape_mars
import time


# MONGODB
# connect to mongo
mongodb_url = 'mongodb://localhost:27017'
mongo_client = MongoClient(mongodb_url)

# get handle to mongo db and create collection
mongo_db = mongo_client.mars_db
collection = mongo_db.mars
news = mongo_db.news


# FLASK
# instantiate flask application object
flask_app = Flask(__name__)

# functions for flask routes
@flask_app.route('/')
def home():

   mars = collection.find()
   test2 = news.find()
   return render_template('index.html', images=mars, tests =test2)
   
# Route that will trigger the scrape function
@flask_app.route("/scrape")
def scrape():
    
    render_template('index2.html')

    collection.drop()
    time.sleep(10)

    
    news_data = scrape_mars.scrape()
    news.update({}, news_data, upsert=True)

    
    hemisphere = scrape_mars.scrape2()
    collection.insert_many(hemisphere)

    # Redirect back to home page
    return redirect("/")




if __name__ == '__main__':
    # start flask server
    flask_app.run(debug=True)

