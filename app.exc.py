from flask import Flask, request, jsonify

app = Flask(__name__)


my_course =[{"id":1, "name": "Python"}
   {"id":2, "name": "Flask"}
]
def post_courses(course_id):
    my_courses.append({"id": course_id, "name":name})
    return jsonify
   pass

def get_courses(course_id):
    for course in my_course:
        if course["id"] == course_id:
            return jsonify(courses) 
        else:
            return jsonify({"course": None}) 




def post_courses():
    courses_list.append(courses_dict)
    return "OK"

def get_courses():
    return jsonify(courses_list)


@app.route('/courses', methods = ["GET", "POST"])
def courses():        
    if request.method == "POST":
        return post_courses()
    return get_courses()      


@app.route('/courses', methods = ["GET", "POST"])
def courses():        
    if request.method == "POST":
        return post_courses()
    return get_courses()      
           