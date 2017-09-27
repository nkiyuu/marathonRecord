from models.model_parent import *


class CourseModel():

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

    def get_courses(self):
        '''
        コース全部返す
        :return:
        '''
        courses_data = self.session.query(Course).all()
        self.session.flush()
        return courses_data

    def get_course_by_id(self, id):
        '''
        idで指定したコースを返す
        '''
        course_data = self.session.query(Course).filter_by(id=id).first()
        return [course_data]

    def register_course(self, url, course_name, distance):
        '''
        新しいコースを登録
        '''
        new_course = Course(url=url, course_name=course_name, distance=distance)
        self.session.add(new_course)
        self.session.flush()
        self.session.commit()
        return [new_course]
