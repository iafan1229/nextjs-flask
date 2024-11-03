from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import ssl

app = Flask(__name__)
CORS(app)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 전역 변수를 사용하여 드라이버를 재사용
driver = None

@app.route('/api/login', methods=['POST'])
def logn():
    global driver
    data = request.json 
    print("Input received:", data)
    if data:
        username = data.get('userName')  
        password = data.get('password') 

        # Instagram 로그인 호출
        response = instagramLogin(username, password)
        return response

    return jsonify({'status': 'fail', 'message': 'No input received'}), 400

def instagramLogin(username, password):
    global driver

    # 드라이버가 이미 실행 중이라면 재사용
    if driver is None:
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_window_size(800, 600)

    driver.get("https://instagram.com")

    try:
        id_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input"))
        )
     
        password_box = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
        login_button = driver.find_element(By.XPATH, "//div[contains(text(), '로그인')]")

   
        act = ActionChains(driver)
        act.send_keys_to_element(id_box, username)\
            .send_keys_to_element(password_box, password)\
            .click(login_button)\
            .perform()

        time.sleep(2)  
        print("로그인 성공")
        return jsonify({'status': 'success', 'message': 'Logged in successfully'}), 200

    except Exception as e:
        print("로그인 실패:", str(e))
        return jsonify({'status': 'fail', 'message': 'Login failed', 'error': str(e)}), 500

    # 필요시 드라이버 종료 (여기서는 로그인 후 드라이버를 유지)
    # driver.quit()
    

if __name__ == '__main__':
    app.run(debug=True)
