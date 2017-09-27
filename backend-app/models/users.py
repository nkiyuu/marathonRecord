from models.model_parent import *


class UserModel():

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

    def get_users_all(self):
        '''
        ユーザ全員の情報をリストで返す
        :return: [User1, User2, ...]
        '''
        users_data = self.session.query(User).all()
        self.session.flush()
        return users_data

    def get_user_by_id(self, id=-1):
        '''
        idで指定したユーザ１人を返す
        :param id: int
        :return: User
        '''
        user_data = self.session.query(User).filter_by(id=id).first()
        return [user_data]

    def register_user(self, name):
        '''
        新しいユーザを登録
        :param name: string
        :return: User
        '''
        new_user = User(name=name)
        self.session.add(new_user)
        self.session.flush()
        self.session.commit()
        return [new_user]
