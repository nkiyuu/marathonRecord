from models.model_parent import *


class RecordsModel():

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

    def get_records_all(self):
        '''
        レコードすべてをリストで返す
        :return: [Record1, Record2, ...]
        '''
        records_data = self.session.query(Record).all()
        records_data = records_data.filter('id == ')
        self.session.flush()
        return records_data

    def get_records_by_id(self):
        '''
        idで指定したレコード1件を返す
        :return: Record
        '''
        record_data = self.session.query.filter_by(id=id).first()
        return record_data
