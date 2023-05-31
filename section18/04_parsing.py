# parsing
# 웹 페이지 소스코드 분석하기
# 문자열 처리하는 방식으로 접근

import requests


def f1():
    site = 'https://www.daum.net/'
    source = requests.get(url=site)
    if source.status_code == 200:
        contents = source.text  # 웹 페이지 소스코드는 contents에 문자열로 저장됨
        contents = contents.split('link_favorsch')  # contents는 이제 리스트
        # contents 리스트의 첫 2개 요소는 필요가 없음
        contents.pop(0)  # 첫 요소 제거, 이후에는 두 번째 요소가 첫 번째 요소로 옮겨감.
        contents.pop(0)
        favor_list = []  # 인기 검색어 모아 둘 리스트
        for content in contents:
            begin = content.find('">')
            end = content.find('</a>')
            favor_list.append(content[begin + 2:end])
        print(favor_list)


f1()
