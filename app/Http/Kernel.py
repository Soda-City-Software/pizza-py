from foundation.Http.Kernel import Kernel as HttpKernel
import app.Http.Middleware.DenyAll

## 
# The application's global HTTP middleware stack.
#
# These middleware are run during every request to your application.
#
# @var array
## 

def GlobalMiddleware():
    return [
        
    ]

## 
# The application's route middleware groups.
#
# @var dictionary
## 
def MiddlewareGroups():
    return {}

## 
# The application's route middleware.
#
# These middleware may be assigned to groups or used individually.
#
# @var dictionary
## 
def RouteMiddleware():
    return {}




class Kernel(HttpKernel):
    def register(self):
        self.Global = GlobalMiddleware()
        self.Groups = MiddlewareGroups()
        self.Routes = RouteMiddleware()
