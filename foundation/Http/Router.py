from routes import *
from foundation.Http.Route import routes

class Router:
    def __init__(self,api):
        self.api = api
        self.routes = routes
        self.register()
    
    def register(self):
        registered = set()
        for route in self.routes:
            if route.endpoint in registered:
                raise Exception("Route Registry Conflict: Duplicate entries for endpoint '{}'.".format(route.endpoint))
            self.api.add_resource(route.controller,route.endpoint)
            registered.add(route.endpoint)

    
    
