from flask import Flask, Blueprint, jsonify
from app.driver import start_driver, stop_driver
from selenium.webdriver.common.by import By
import re
from bs4 import BeautifulSoup
import time

getContent = Blueprint('getContent', __name__)

@getContent.route('/api/getContent', methods=['GET'])
def get_content():
    driver = start_driver()  # 드라이버 시작
    html = driver.page_source
    soup = BeautifulSoup(html)

    # 현재 페이지 HTML 정보 가져오기
    def select_first(driver):
        insta = soup.select('._ac7v.x1f01sob.xcghwft.xat24cr.xzboxd6')
        print(insta)
        # first = soup.find_element(By.CSS_SELECTOR, 'div._ac7v')  # 첫 번째 게시물 클릭
        # first.click()
        # time.sleep(5)  # 페이지 로딩 대기

    def fetch_img_url(driver):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        try: 
            img = soup.select('div.aagv > img')[0]['src']
            return img
            # content = soup.select('div._a9zr')[0].text  # 본문 내용 추출
        except IndexError: 
            content = ' '  # 본문 내용이 없을 경우 처리
        tags = re.findall(r'#[^\s#,\\]+', content)  # 해시태그 추출
        date = soup.select('time._aaqe')[0]['datetime'][:10]  # 날짜 추출
        data = [content, date, tags]  # 수집한 데이터
        return data

    # 본문 내용 가져오기
    try:
        select_first(driver)  # 첫 번째 게시물 선택
        data = fetch_img_url(driver)  # 콘텐츠 수집
    except Exception as e:
        print("오류 발생:", str(e))
        stop_driver()
        return jsonify({'status': 'fail', 'message': 'Error occurred', 'error': str(e)}), 500

    # 수집한 정보 반환
    return jsonify({'status': 'success', 'data': data}), 200
