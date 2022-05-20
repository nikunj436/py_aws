from flask import Flask, request, render_template
from pymongo import MongoClient
app = Flask(__name__, template_folder="Templates") #Templates folder added here #issue in container alpine unable to find "index.html"

@app.route("/")
def index():
    return render_template("index.html")

# define the mongodb client 
client = MongoClient(host='test_mongodb',port=27017)  #host name added, same mention in docker-compose
#client = MongoClient('mongodb://root:pass@localhost:27017/') #if password used 

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
    ans = []
    for i in L:
        temp = i['First']+ " " + i['Last'] 
        ans.append(temp)
        #ans.reverse()        
    
    return render_template("data_show.html", ans=ans) #ans=ans printing in sep lines 

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5656, debug=True)  #host changes localhost to '0.0.0.0'

