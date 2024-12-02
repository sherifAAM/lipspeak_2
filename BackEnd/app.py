from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from routes.auth import auth_blueprint
from routes.lessons import lessons_blueprint
from routes.progress import progress_blueprint
import os

app = Flask(__name__)

# Load configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/lipspeak.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET", "your_jwt_secret")

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(lessons_blueprint, url_prefix='/lessons')
app.register_blueprint(progress_blueprint, url_prefix='/progress')

if __name__ == "__main__":
    app.run(debug=True)
