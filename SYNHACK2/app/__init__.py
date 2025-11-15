from flask import Flask
from flask_cors import CORS
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    from app.routes import auth, complaints, admin, worker
    app.register_blueprint(auth.bp)
    app.register_blueprint(complaints.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(worker.bp)
    
    return app
