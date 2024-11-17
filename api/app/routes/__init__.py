from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    # 라우트 등록
    from .auth import auth as auth_blueprint
    from .getContent import getContent as getContent_blueprint

    app.register_blueprint(auth_blueprint)
    # app.register_blueprint(getContent_blueprint)

    return app

