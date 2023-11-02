from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your database connection (you'll need to replace 'your_database_uri')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:P$wrdmgr99@localhost/PasswordManager'

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'cursorclass': 'pymysql.cursors.DictCursor'}}

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

try:
    # Test the connection by executing a simple query, like fetching the count of users
    user_count = db.session.query(User).count()
    print(f"Database connection successful. Total users in database: {user_count}")
except Exception as e:
    print(f"Database connection failed: {str(e)}")
    
# Import your routes (we'll create them later)
from . import routes