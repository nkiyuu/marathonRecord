from models.model_parent import Parent


class UserModel(Parent):

    def __init__(self):
        super().__init__()

    def get_all(self):
        '''
        データベース上のすべてのユーザを取得
        :return: データベース上のすべてのユーザ
                 [{id: 1, name: hogehoge}, {id: 2, name: fugafuga}, ...]
        '''
        users_map = self.cursor.execute('select id, name from users')
        users = []
        for user_data in users_map:
            users.append({"id": user_data[0], "name": user_data[1]})
        return users

    def get_user_by_id(self, id):
        '''
        idで指定したユーザを取得
        :param id: user_id
        :return: idで指定したユーザ
                 {id: 3, name: hoge}
        '''
        user_map = self.cursor.execute('select id, name from users where id == ?', (id,)).fetchone()
        if user_map is None:
            return {}
        return {"id": user_map[0], "name": user_map[1]}

    def post_user(self, name):
        '''
        ユーザ1人を登録
        :param name: ユーザネーム
        :return: 追加したユーザ
                 {id: 4, name: hoge}
        '''
        self.cursor.execute('insert into users (name) values ( ? )', (name,))
        self.connection.commit()
        return {"id": self.cursor.lastrowid, "name": name }
