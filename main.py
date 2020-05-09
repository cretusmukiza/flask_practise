from flask import Flask,jsonify
from flask_jwt_extended import JWTManager
import logging
from api.config.config import ProductionConfig,TestingConfig,DevelopmentConfig
from api.utils.database import db
from api.utils.responses import response_with
from flask_migrate import Migrate
import api.utils.responses as resp
from api.routes.authors import author_routes
from api.routes.books import book_routes
from api.routes.users import user_routes
import os
env = os.environ.get('WORK_ENV')
if env == 'PROD':
    app_config = ProductionConfig
elif env == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app = Flask(__name__)
app.config.from_object(app_config)
db.init_app(app)
jwt = JWTManager(app)
Migrate(app,db)
with app.app_context():
    db.create_all()
app.register_blueprint(author_routes,url_prefix='/api/authors')
app.register_blueprint(book_routes,url_prefix= '/api/books')
app.register_blueprint(user_routes,url_prefix="/api/users")


# Global http configurations
@app.after_request
def add_header(response):
    return response

@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)
@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)

@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)

if __name__ == "__main__":
    app.run()

