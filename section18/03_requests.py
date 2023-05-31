# requests 모듈
# 1. 웹 페이지를 가져올 때 사용한다.
# 2. 설치해야 한다.
#    1) Terminal 열기
#    2) pip install requests

import requests


def f1():
    url = 'https://www.daum.net/'
    source = requests.get(url)
    print(f'응답코드: {source.status_code}')
    # 응답코드
    # 200 : 성공
    # 400번대 : 요청한 사용자 측 문제
    # 500번대 : 서버 측 문제
    print(source.text)  # 웹 페이지 소스코드


def f2():
    # 실제 경로
    # https://search.daum.net/search?q=코로나
    # 주소?파라미터=값&파라미터=값
    URL = 'https://search.daum.net/search'
    source = requests.get(url=URL, params={'q': '코로나'})
    if source.status_code == 200:  # 정상 처리되면
        print(source.text)


def naver():
    # 네이버에서 '코로나' 검색한 결과 source 가져오기
    URL = 'https://search.naver.com/search.naver'
    parameter = {
        'query': '코로나'
    }
    source = requests.get(url=URL, params=parameter)
    if source.status_code == 200:
        print(source.text)


# naver()


def google():
    # 구글에서 '코로나' 검색한 결과 source 가져오기
    URL = 'https://www.google.com/search'
    source = requests.get(url=URL, params={'q': '코로나'})
    if source.status_code == 200:
        print(source.text)


google()
