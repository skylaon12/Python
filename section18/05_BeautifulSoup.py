# BeautifulSoup 모듈
# 1. 웹 페이지(태그로 구성된 내용)를 파싱할 때 사용한다.
# 2. 설치해야 한다.
#    1) Terminal 열기
#    2) pip install bs4

from bs4 import BeautifulSoup  # bs4에서 BeautifulSoup만 쓴다.


contents = '''<li><a href="https://www.daum.net/" class="aa">다음</p></li>
<li><a href="https://www.google.com/" class="aa">구글</a></li>
<li><a href="https://www.naver.com/" class="aa">네이버</a></li>'''


# 파서(parser, 분석기)를 이용해서 파싱하기
soup = BeautifulSoup(contents, 'html.parser')  # 기본 파서: html.parser


# 메소드 사용하기
# 1. find() 메소드
#    1) 지정한 요소를 찾는다.
#    2) 검색된 요소가 많으면 첫 번째 요소를 반환한다.
a = soup.find('a')  # <a> 태그 가져온다.
print(a)

# 2. text 필드
#    태그 내부의 텍스트를 반환한다.
b = soup.find('li')  # <li> 태그 가져온다.
print(b.text)

# 3. find_all() 메소드
#    지정한 요소를 모두 찾아서 리스트로 반환한다.
c = soup.find_all('a')
print(c)


# 사이트 이름 3개 뽑아내기
sites = []
for a in soup.find_all('a'):
    sites.append(a.text)
print(sites)


# 4. class 속성 값 찾기
d = soup.find_all('a', class_='aa')  # <a class="aa"> 인 모든 요소를 리스트로 반환
print(d)


# 04_parsing.py 문제 다시 풀기

import requests


site = 'https://www.daum.net/'
source = requests.get(url=site)  # 전체 소스코드 가져오기
if source.status_code == 200:
    soup = BeautifulSoup(source.text, 'html.parser')  # 파서로 분석하기
    favor_list = []
    for a in soup.find_all('a', class_='link_favorsch'):
        favor_list.append(a.text)
    print(favor_list)


# 네이트 실시간 이슈 키워드
site = 'https://www.nate.com/'
source = requests.get(url=site)
if source.status_code == 200:
    soup = BeautifulSoup(source.text, 'html.parser')
    for span in soup.find_all('span', class_='txt_rank'):
        print(span.text)

# 네이트 "베니스영화제" 검색 결과 관련 키워드
site = 'https://search.daum.net/nate'
source = requests.get(url=site, params={'q': '베니스영화제'})
if source.status_code == 200:
    soup = BeautifulSoup(source.text, 'html.parser')
    for a in soup.find_all('a', class_='keyword'):
        print(a.text)
