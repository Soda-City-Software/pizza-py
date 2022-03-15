from flask_restful import Resource
from flask import request
from foundation.Mock.InMemoryDB import students
from foundation.Http.Controller import Controller


class Student(Controller):

    def get(self,name):
        return {"name":name}
    
    def post(self,name):
        data = request.get_json()
        record = {'name': name, 'class': data['class']}
        students.append(record)
        return record
