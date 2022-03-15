# from foundation.Application import Application

# app = Application()

from bootstrap.app import Bootstrapper
from foundation.Application import app

app = Bootstrapper.boot()
print('App:',app)
# app.run()

# import app.Http.Middleware as Middleware

# test = Middleware.DenyAll


# print(test)
# from waitress import serve
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return {'hello':'world'}


# serve(app, host='127.0.0.1',port=8081)

