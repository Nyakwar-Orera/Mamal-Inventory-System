from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'  # Redirect to login page if not authenticated
mail = Mail()

def create_app(config_class=Config):
    # Initialize the Flask app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize all extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)

    # Register blueprints
    from app.main.routes import bp as main_bp
    from app.auth.routes import bp as auth_bp
    from app.assets.routes import bp as assets_bp
    from app.stationery.routes import bp as stationery_bp
    from app.checkout import bp as checkout_bp
    from app.maintenance.routes import bp as maintenance_bp
    from app.reports import bp as reports_bp  # ✅ Register the reports blueprint
    from app.admin.routes import bp as admin_bp  # ✅ Register the admin blueprint

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(assets_bp, url_prefix='/assets')
    app.register_blueprint(stationery_bp, url_prefix='/stationery')
    app.register_blueprint(checkout_bp, url_prefix='/checkout')
    app.register_blueprint(maintenance_bp, url_prefix='/maintenance')
    app.register_blueprint(reports_bp, url_prefix='/reports')  # ✅ Ensure reports blueprint is registered
    app.register_blueprint(admin_bp, url_prefix='/admin')  # ✅ Ensure admin blueprint is registered

    return app
