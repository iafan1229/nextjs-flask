from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from flask_cors import CORS
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)
CORS(app)

@app.route('/api/open-browser', methods=['GET'])
def open_browser():
    # 브라우저 옵션 설정
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # 드라이버 설정 및 실행
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 웹페이지 이동
    driver.get("https://instagram.com")

    return jsonify({'status': 'Browser opened successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask
# app = Flask(__name__)

# @app.route("/api/python")
# def hello_world():
#     return "Hello, World!"

# @app.route('/')
# def hello():
#     return 'hello hayoung'

# @app.route('/api/home')
