from scrape_mars import Scrape
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect

app = Flask(__name__)

#Mongodb connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/MarsDB"
mongo = PyMongo(app)

@app.route("/scrape")
def scrape():
    mars_data = Scrape()
    mongo.db.mars.drop()
    mongo.db.mars.insert_one(mars_data)
    return redirect("http://localhost:5000/", code=302)

@app.route("/")
def home():
    mars_data = mongo.db.mars.find_one()
    return render_template('index.html',mars_data=mars_data)



if __name__ == "__main__":
    app.run(debug=True)