from models.model_parent import *
import datetime


class RecordModel():

    def __init__(self):
        self.closed = False
        self.session = Session()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    def close(self):
        if self.closed:
            return
        self.session.closed = True
        self.session.close()

    def get_records_all(self, user_id=-1, course_id=-1):
        '''
        レコードすべてをリストで返す
        :return: [Record1, Record2, ...]
        '''
        records_data = self.session.query(Record)
        if user_id != -1:
            records_data = records_data.filter_by(user_id=user_id)
        if course_id != -1:
            records_data = records_data.filter_by(course=course_id)
        records_data = records_data.all()
        self.session.flush()
        return records_data

    def get_records_by_id(self, id):
        '''
        idで指定したレコード1件を返す
        :return: Record
        '''
        record_data = self.session.query(Record).filter_by(id=id).first()
        return [record_data]

    def register_record(self, user_id, course_id, time, date=None):
        '''
        記録の登録
        '''
        if date:
            tdate = datetime.datetime.strptime(date, '%Y-%m-%d')
            date = datetime.date(tdate.year, tdate.month, tdate.day)
        new_record = Record(user_id=user_id,course=course_id, time=time, date=date)
        self.session.add(new_record)
        self.session.flush()
        self.session.commit()
        return [new_record]
