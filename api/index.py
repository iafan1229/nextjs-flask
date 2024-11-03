# #이슈1: 인증되지 않은 경우 코드 보내야되는데 어떻게 할 것인가
from app.routes import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
