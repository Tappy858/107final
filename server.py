from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, Flask!"

@app.get("/test")
def test():
    return "This is another page"


#this will be the Json endpoints
#this is an API endpoint

@app.get("/api/about")
def about():
    me = {"name": "Darius"}
    return json.dumps(me)



app.run(debug=True)