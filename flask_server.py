from flask import Flask, render_template, redirect
from pymongo import MongoClient
import scrape_mars



# MONGODB
# connect to mongo
mongodb_url = 'mongodb://localhost:27017'
mongo_client = MongoClient(mongodb_url)

# get handle to mongo db and create collection
mars = mongo_client.mars_db


# FLASK
# instantiate flask application object
flask_app = Flask(__name__)

# functions for flask routes
@flask_app.route('/')
def home():

   mars_info = mars.mars_info.find_one()
  
   return render_template('index.html', mars_info=mars_info)
   
# Route that will trigger the scrape function
@flask_app.route("/scrape")
def scrape():
    

    mars_info = mars.mars_info
    mars_data = scrape_mars.scrape()
    mars_info.update({}, mars_data, upsert=True)

# Redirect back to home page
    return redirect("/", code =302)




if __name__ == '__main__':
    # start flask server
    flask_app.run(debug=True)

