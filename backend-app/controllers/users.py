from flask import Blueprint
from flask import request
import json

from models.users import UserModel

app = Blueprint('user', __name__)


@app.route('/users', methods=['GET'])
def get_all_users():
    with UserModel() as User:
        users = User.get_users_all()
    print(users)
    return to_json(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    '''
    指定IdのUserオブジェクト１つのリストを返す
    '''
    with UserModel() as User:
        user = User.get_user_by_id(user_id)
    return to_json(user)


@app.route('/user', methods=['POST'])
def post_user():
    '''
    jsonを受け取ってデータを登録
    '''
    with UserModel() as User:
        user_data = User.register_user(request.json['name'])
        add_user = to_json(user_data)

    return add_user


def to_json(users):
    '''
    Userオブジェクトのリストを受け取ってjsonにして返す
    '''
    users_map = []
    for user in users:
        users_map.append({
            'id': user.id,
            'name': user.name,
            'created_at': str(user.created_at),
        })
    return json.dumps(users_map)
