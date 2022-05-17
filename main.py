from flask import Flask, request, render_template
from pymongo import MongoClient
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# define the mongodb client
client = MongoClient(port=27017)

# define the database to use
db = client.devopsdb

@app.route("/data_entry.py/", methods = ["GET", "POST"])
def data_entry():
    data = {}
    
    if request.method == "POST":
        data['First'] = request.form['first_name']
        data['Last'] = request.form['last_name']
    db.namecollection.insert_one(data)
    
    return render_template("data_entry.html")

@app.route("/data_show.py") 
def data_show():
    L = db.namecollection.find({})  #selecting all entries

    for i in L:
        print(i)
    return render_template("data_show.html", L=i)

if __name__ == '__main__':
    app.run(host="localhost",port=5656, debug=True) 

