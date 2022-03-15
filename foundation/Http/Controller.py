from flask_restful import Resource
from 

class Controller(Resource):

    middleware = {
        "all":      [],
        "get":      [],
        "post":     [],
        "put":      [],
        "delete":   [],
    }

    method_decorators = middleware
    