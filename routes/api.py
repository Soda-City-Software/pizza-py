from foundation.Http.Route import Route
from app.Http.Controllers.Student import Student
from app.Http.Controllers.StudentList import StudentList


var = 9

Route.group(prefix='/students', routes=[
    Route(endpoint='/<string:name>', controller=Student),
    Route('/', StudentList),
])
