from flask import Flask
from flask_cors import CORS
from database import init_db
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    init_db()

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
