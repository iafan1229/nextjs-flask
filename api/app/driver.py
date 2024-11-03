from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# 전역 드라이버 변수
driver = None

def start_driver():
    global driver
    if driver is None:
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.set_window_size(800, 600)
    return driver

def stop_driver():
    global driver
    if driver is not None:
        driver.quit()
        driver = None

