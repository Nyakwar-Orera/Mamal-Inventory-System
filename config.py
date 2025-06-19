import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'  # Use a secret key for sessions and CSRF protection
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///assets.db'  # Database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to save resources

    # Flask-Mail Configuration for sending emails
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'  # Default to Gmail
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)  # Default to 587 (Gmail SMTP)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True') == 'True'  # Defaults to True if not set
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False') == 'True'  # Defaults to False if not set
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  # Email username
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Email password (use environment variable for security)
    ADMINS = [os.environ.get('ADMIN_EMAIL')]  # List of admin emails (for error notifications, etc.)

    # Pagination settings
    ITEMS_PER_PAGE = 20  # Adjust based on your needs

    # Threshold for low stock items (example)
    LOW_STOCK_THRESHOLD = {
        'A4': 100,
        'A3': 50,
        'A5': 50,
        'photo_paper': 20
    }
