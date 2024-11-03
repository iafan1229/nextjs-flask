# 게시글 정보 가져오기
import re
from bs4 import BeautifulSoup
import unicodedata
 
def get_content(driver):
    # 현재 페이지 html 정보 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # 본문 내용 가져오기
    try:
        content = soup.select('div._a9zs')[0].text
        content = unicodedata.normalize('NFC', content)
    except:
        content = ' '
    
    #본문 내용에서 해시태그 가져오기(정규식 활용)
    tags = re.findall(r'#[^Ws#,\\]+', content)
   
    # 작성일자 정보 가져오기
    # time class 안에 datetime이라는 항목(년월일시분초 있음)에서 10개 string만 보겠다라는 뜻
    date = soup.select('time._aaqe')[0]['datetime'][:10] 
    
    # 수집한 정보 저장하기
    data = [content, date, tags]
    return data
 
get_content(driver)