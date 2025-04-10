import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_secret_key")

# Configure SQLite database
db_path = os.path.join(os.path.dirname(__file__), 'inventory.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Import routes after the app is initialized to avoid circular imports
from routes import *  # noqa: E402, F403

# Create database tables
with app.app_context():
    logger.info("Creating database tables...")
    db.create_all()
    logger.info("Database tables created successfully.")
