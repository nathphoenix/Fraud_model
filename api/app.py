import os
from flask import Flask, jsonify, Blueprint, request, abort, Response
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
from flask_sieve import Sieve
import socket


from datetime import timedelta



def create_app():
    load_dotenv(".env", verbose=True)

    
    from .resources.fraud import FraudDetection, Fraud_web
    

    app = Flask(__name__, instance_relative_config=True, static_url_path='', static_folder='static/')
    Sieve(app)

    app.url_map.strict_slashes = False


    api = Api(app)

    '''
    ALL THE AVAILABLE ROUTES OR VIEWS
    '''
    
    api.add_resource(FraudDetection, '/fraud_prediction')
    api.add_resource(Fraud_web, '/fraud_predict')
    

    @app.route('/500')
    def error500():
        abort(500)

    
    @app.route('/home_V2')
    def v2_home():
        welcome = 'INTERSWITCH API'
        return welcome, 200

    @app.route('/v1')
    def v1_home():
        return jsonify({
            "message": "WELCOME TO INTERSWITCH API v1 API!"
        }), 200

    @app.route('/')
    def home():
        server_id = socket.gethostname()

        return render_template("index.html", server_response = server_id)
    

    return app


app = create_app()


from api.app_settings.app_config import *

