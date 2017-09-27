from flask import Blueprint
from flask import request
import json

from models.records import RecordModel

app = Blueprint('record', __name__)


@app.route('/records', methods=['GET'])
def get__records():
    '''
    複数のレコードを取ってくる
    オプションで絞り込みが可能
    - デフォルト: 全件
    - user_id: 指定のユーザ
    - course_id: 指定のコース
    '''
    user_id = request.args.get('user_id') if request.args.get('user_id') is not None else -1
    course_id = request.args.get('course_id') if request.args.get('course_id') is not None else -1

    with RecordModel() as Record:
        records = Record.get_records_all(user_id=user_id, course_id=course_id)

    return to_json(records)


@app.route('/records/<int:record_id>', methods=['GET'])
def get_record_by_id(record_id):
    '''
    idで指定した結果を返す
    '''
    with RecordModel() as Record:
        record = Record.get_records_by_id(record_id)

    return to_json(record)


@app.route('/records', methods=['POST'])
def post_record():
    sent_data = request.json
    if 'date' not in sent_data:
        sent_data['date'] = None
    with RecordModel() as Record:
        record_data = Record.register_record(
            user_id=sent_data['user_id'],
            course_id=sent_data['course_id'],
            time=sent_data['time'],
            date=sent_data['date'],
        )
        added_record = to_json(record_data)
    return added_record


def to_json(records_list):
    records = []
    for record in records_list:
        records.append({
            'id': record.id,
            'user_id': record.user_id,
            'course_id': record.course,
            'time': record.time,
            'date': str(record.date),
            'created_at': str(record.create_at),
        })
    return json.dumps(records)
