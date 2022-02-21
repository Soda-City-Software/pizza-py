from flask import Flask
from flask_restful import Api
from foundation.Http.Router import Router
from waitress import serve
import foundation.Config as config


class Application:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.router = Router(self.api)
        # print('Resources:',self.api.add_resource())
        # self.config = config
        # self.middleware = middleware

    def run(self):
        if config.get('env') is 'production': 
            serve(self.app, host='0.0.0.0', port=80)
        else:
            self.app.run(host='0.0.0.0',port=80)