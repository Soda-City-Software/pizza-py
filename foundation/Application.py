from flask import Flask
from flask_restful import Api
from foundation.Http.Router import Router
from waitress import serve

class Application:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.router = Router(self.api)
        # print('Resources:',self.api.add_resource())
        # self.config = config
        # self.middleware = middleware

    def run(self):
        serve(self.app, host='127.0.0.1', port=8011)
        # self.app.run()