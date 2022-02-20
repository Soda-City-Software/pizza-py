
from app.Http.Middleware.DenyAll import With400
from app.Http.Middleware.DenyAll import With422

routes = []

class Route:
    def __init__(self, endpoint:str, controller, middleware:set = {}):
        self.setEndpoint(endpoint)
        self.controller = controller
        self.middleware = middleware
        self.setControllerMiddleware()
        self.define()

    def define(self):
        global routes
        routes.append(self)

    def setControllerMiddleware(self):
        print('middleware:',self.controller.middleware)
        self.controller.middleware = {'get':[]}
        print('middleware:',self.controller.middleware)

    def setEndpoint(self, endpoint):
        if len(endpoint) <= 0:
            raise Exception("Route Registry Conflict: the endpoint must be atleast one character. (ex: '/')")
        if endpoint[-1] == '/':
            endpoint = endpoint[0:-1]
        self.endpoint = endpoint

    @staticmethod
    def group(prefix:str = '', middleware:set = {}, routes:list = []):
        for route in routes:
            route.extend(prefix,middleware)

    def extend(self,prefix:str,middleware:set):
        if prefix:
            endpoint = prefix + self.endpoint
            self.setEndpoint(endpoint)
        if middleware:
            self.middleware.union(middleware)
            
    