
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Blueprint, request, jsonify
from selenium.webdriver.common.action_chains import ActionChains
from app.driver import start_driver
import time


auth = Blueprint('auth', __name__)


@auth.route('/api/login', methods=['POST'])
def logn():
    driver = start_driver()
    data = request.json 
    print("Input received:", data)
    if data:
        username = data.get('userName')  
        password = data.get('password') 

        # Instagram 로그인 호출
        response = instagramLogin(username, password, driver)
        return response

    return jsonify({'status': 'fail', 'message': 'No input received'}), 400

def instagramLogin(username, password, driver):
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

        time.sleep(10)  
        print("로그인 성공")
        loadUserPage(driver)
        return jsonify({'status': 'success', 'message': 'Logged in successfully'}), 200

    except Exception as e:
        print("로그인 실패:", str(e))
        return jsonify({'status': 'fail', 'message': 'Login failed', 'error': str(e)}), 500
    
def loadUserPage(driver):
    # 내비게이션 바 로드 대기
    try:
        print('네비 로딩중')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'nav'))
        )
        print("로그인 성공! 내비게이션 바가 로드되었습니다.")
        return jsonify({'status': 'success', 'message': '로그인 성공!'}), 200
    except Exception as e:
        print("내비게이션 바를 찾지 못했습니다:", str(e))
        return jsonify({'status': 'fail', 'message': '로그인 후 내비게이션 바를 찾지 못했습니다.'}), 401
