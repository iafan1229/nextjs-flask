from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    # 라우트 등록
    from .auth import auth as auth_blueprint
    # from .routes.main import main as main_blueprint

    app.register_blueprint(auth_blueprint)
    # app.register_blueprint(main_blueprint)

    return app

