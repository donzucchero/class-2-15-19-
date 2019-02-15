from flask import Flask, request

app = Flask(__name__)


courses_list=[]


courses_dict = {
    "id": 1, 
    "name": "Python"
}

def post_courses(:
    courses_list.append(courses_dict)
    return "OK"

def get_get_courses():
    return jsonify9courses_list


@app.route('/courses', methods = ["GET", "POST"])
def courses        
    if request.method == "POST":
        return post_courses()
    return get_courses()      
           

# this didnt work out
