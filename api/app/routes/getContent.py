from flask import Flask, abort, request, Blueprint, jsonify
from app.driver import start_driver, stop_driver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


getContent = Blueprint('getContent', __name__)

def scroll_and_collect_posts(driver, user):
    driver.get(f'https://www.instagram.cp.kkl/{user}/')
    time.sleep(5)
    
    # 페이지 스크롤을 통해 모든 게시물 로드
    last_height = driver.execute_script("return document.body.scrollHeight")
    posts = set()

    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        new_posts = soup.select('div._aagw a')
        for post in new_posts:
            posts.add('https://www.instagram.com' + post['href'])
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    return list(posts)

def scrape_post_data(driver, url, n):
    driver.get(url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # 게시물 이미지 URL 추출
    try:
        img_url = soup.select_one('.x5yr21d img')['src']
    except TypeError:
        print(f"No image found in {url}")
        return None
    
    # 좋아요 수 추출
    try:
        likes = soup.select_one('div._aacl span').text
    except AttributeError:
        likes = 'No likes'
    
    # print(f"Post {n}: Likes: {likes}\nImage URL: {img_url}\n")
    
    # 이미지 저장
    # save_image(img_url, n)
    return {'likes': likes, 'img_url': img_url}


@getContent.route('/api/getContent', methods=['GET'])
def getContent():
    driver = start_driver()
    
    try:
        query = request.args.get('userId')
        if query:
            user = query  # 크롤링할 유저명 입력
            post_urls = scroll_and_collect_posts(driver, user)
            
            # print(f"Found {len(post_urls)} posts.")
            dataSet = set()
            for n, url in enumerate(post_urls, 1):
                eachData = scrape_post_data(driver, url, n)
                dataSet.set(eachData)
                time.sleep(2)  # 과부하 방지를 위해 대기 시간 추가
            return list(dataSet)
    
    except Exception as e:
        stop_driver()
        return jsonify({'status': 'fail', 'message': '', 'error': str(e)}), 500

    finally:
        stop_driver()
        # print("Driver closed.")