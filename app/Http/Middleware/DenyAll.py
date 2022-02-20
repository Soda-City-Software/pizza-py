from flask_restful import abort
from functools import wraps

class DenyAll:

    def handle(self,func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            abort(400)
        return wrapper

class With400:

    def handle(self,func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            abort(400)
        return wrapper

        
class With422:

    def handle(self,func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            abort(422)
        return wrapper

class DenyAll2:

    def handle(self):
        abort(400)