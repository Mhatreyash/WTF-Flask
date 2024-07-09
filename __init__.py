from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('wtf.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    from wtf.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from wtf.main.routes import bp as main_bp
    app.register_blueprint(main_bp)

    from wtf.auth.routes import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    print("Blueprints registered", main_bp, auth_bp)
    print(f"App routes: {app.url_map}")

    @app.errorhandler(404)
    def page_not_found(e):
        print(f"404 error: {request.url}")
        print(f"Request method: {request.method}")
        print(f"Request headers: {request.headers}")
        return render_template('404.html'), 404

    return app
