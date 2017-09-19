from models.model_parent import *


def get_records_all():
    '''
    記録全件を取得
    :return:  データベース上のすべての記録
    '''
    session = Session()
    users = session.query(UserModel).all()
    print(users[0].name)
    session.flush()
    session.close()