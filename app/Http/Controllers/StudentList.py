from flask_restful import Resource
from foundation.Mock.InMemoryDB import students

class StudentList(Resource):

    middleware = {}
    
    def get(self):
        return students
