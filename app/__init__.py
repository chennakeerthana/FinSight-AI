from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config')
    client = MongoClient(app.config['MONGO_URI'])
    app.db = client.get_default_database()
    with app.app_context():
        from .auth import auth_bp
        app.register_blueprint(auth_bp)

    return app
