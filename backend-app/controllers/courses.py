from flask import Blueprint
from flask import request
import json

from models.courses import CourseModel

app = Blueprint('course', __name__)


@app.route('/courses', methods=['GET'])
def get_all_courses():
    with CourseModel() as Course:
        courses = Course.get_courses()
    return to_json(courses)


@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    '''
    指定したidのコースの情報をひっぱてくる
    '''
    with CourseModel() as Course:
        course = Course.get_course_by_id(course_id)
    return to_json(course)


@app.route('/courses', methods=['POST'])
def post_course():
    '''
    jsonを受け取ってコースを登録
    '''
    json_data = request.json
    with CourseModel() as Course:
        course_data = Course.register_course(
            url=json_data['url'],
            course_name=json_data['course_name'],
            distance=json_data['distance'],
        )
        added_course = to_json(course_data)
    return added_course


def to_json(courses):
    '''
    Courseオブジェクトのリストを受け取ってjsonを返す
    '''
    courses_map = []
    for course in courses:
        courses_map.append({
            'id': course.id,
            'course_name': course.course_name,
            'url': course.url,
            'distance': course.distance,
            'created_at': str(course.create_at),
        })
    return json.dumps(courses_map)