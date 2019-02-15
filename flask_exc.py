from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/varrrrr_hello_world', methods = ["GET", "POST"]) 
def varrrrr_hello_world():
    if request.method == "POST":
        add_to_list()
    get_the_list()

my_list=[]
def add_to_list():
   my_list.append("Item")

def get_the_list():
    return jsonify(my_list)



