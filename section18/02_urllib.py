# urllib 모듈
# 1. 표준 모듈이다.
# 2. 웹 페이지의 소스(html)를 가져온다.
# 3. 사용법이 다른 모듈에 비해서 약간 어렵다.
# 4. 오픈 API에서 많이 사용된다.

# request
# 1. 요청
# 2. 사용자가 서버에게 요청하는 것

# response
# 1. 응답
# 2. 서버가 사용자에게 응답하는 것


import urllib.request


def f1():
    url = 'https://www.daum.net/'
    request = urllib.request.Request(url)
    print(request)
    print(request.full_url)
    print(request.host)


def f2():
    url = 'https://www.daum.net/'
    response = urllib.request.urlopen(url)
    data = response.read(500)  # 500byte 읽어 오기
    print(data)


def f3():
    url = 'https://www.daum.net/'
    response = urllib.request.urlopen(url)
    byte_data = response.read(500)  # 500바이트 읽기
    text_data = byte_data.decode()  # 읽어 들인 바이트 데이터 -> 텍스트 데이터, 디폴트 utf-8
    print(text_data)


def f4():
    url = 'https://www.daum.net/'
    response = urllib.request.urlopen(url)
    source = response.read().decode()  # 모두 읽어서 텍스트로 변경
    f = open('daum.html', 'wt', encoding='utf-8')
    f.write(source)
    f.close()
    print('daum.html 페이지가 생성되었다.')


def f5():
    search_word = 'autumn'
    url = f'https://search.daum.net/search?q={search_word}'
    response = urllib.request.urlopen(url)
    source = response.read().decode()  # 모두 읽어서 텍스트 데이터로 저장하고 있음. (파일 모드 : 텍스트 모드)
    f = open(f'{search_word}_daum.html', 'wt', encoding='utf-8')
    f.write(source)
    f.close()
    print(f'{search_word}_daum.html 페이지가 생성되었다.')


f5()


def f5():
    search_word = 'autumn'
    url = f'https://search.daum.net/search?q={search_word}'
    response = urllib.request.urlopen(url)
    source = response.read()  # 모두 읽어서 바이트 데이터로 저장하고있음. (파일 모드 : 텍스트 모드)
    f = open(f'{search_word}_daum.html', 'wb')
    f.write(source)
    f.close()
    print(f'{search_word}_daum.html 페이지가 생성되었다.')
