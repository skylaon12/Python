# selenium 모듈
# 1. 완성된 웹 페이지의 동작을 검증(테스트)하는 모듈
# 2. 설치 방법
#    1) pip install selenium
#    2) webdriver 다운로드 후 section18 디렉터리에 둠
# 3. webdriver
#    1) 파이썬(프로그램)과 웹 브라우저(크롬)의 통신을 위한 프로그램
#    2) https://chromedriver.chromium.org/downloads
#    3) 설치된 크롬과 버전을 맞춰서 다운로드
#       - C:/Program Files/Google/Chrome/Application 디렉터리에서 버전 확인 (92.)


from selenium import webdriver

# 엔터 등 특수문자 사용하기 위해서
from selenium.webdriver.common.keys import Keys

# 각 과정 사이의 시간 끌기
import time


def f1():
    driver = webdriver.Chrome('chromedriver.exe')  # 소스코드와 동일한 경로에 배치한 chromedriver.exe

    driver.get('https://www.naver.com')  # 네이버 열기

    search_window = driver.find_element_by_id('query')  # 검색창 알아내기
    search_window.send_keys('이번 주말 날씨')  # 검색창에 검색어 입력하기
    search_btn = driver.find_element_by_id('search_btn')  # 검색버튼 알아내기
    search_btn.click()  # 검색버튼 클릭하기


def f2():
    # 다음 자동로그인

    driver = webdriver.Chrome('chromedriver.exe')

    driver.get('https://www.daum.net/')  # 다음 열기

    link_login = driver.find_elements_by_class_name('link_login')  # Kakao아이디, Daum 아이디로 로그인
    link_login[1].click()  # 2번째 Daum 아이디로 로그인 클릭
    
    time.sleep(2)  # 2초 가만히 있기

    # 방법1
    # user_id = driver.find_element_by_id('id')  # 아이디 입력창
    # user_id.send_keys('본인의 아이디 작성하는 자리')

    # 방법2 (방법1이 막히는 경우)
    # 자바스크립트 코드 직접 넣기
    driver.execute_script('document.getElementById("id").value="본인아이디작성"')

    time.sleep(2)

    # 방법1
    # user_pw = driver.find_element_by_id('inputPwd')  # 비밀번호 입력창
    # user_pw.send_keys('본인의 비밀번호 작성하는 자리')

    # 방법2
    driver.execute_script('document.getElementById("inputPwd").value="본인비밀번호작성"')

    time.sleep(2)

    btn = driver.find_element_by_id('loginBtn')  # 로그인 버튼
    btn.send_keys(Keys.ENTER)  # 로그인 버튼 엔터 누르기


f2()
