# 파일 읽기

# 읽기 메소드
# 1. read()  : 모든 내용을 읽는다.
# 2. read(n) : n글자(n바이트)만 읽는다. (텍스트모드: 글자, 바이너리모드: 바이트)
# 3. readline()  : 한 줄만 읽는다.
# 4. readlines() : 모든 내용을 읽는다. 한 줄씩 따로 저장한다.


def f1():
    f = open('./storage/민경태.txt', 'rt')  # rt : 텍스트 읽기 모드
    contents = f.read()  # 다 읽어서 contents에 저장한다.
    print(contents)
    f.close()


def f2():
    f = open('./storage/20210823.txt', 'rt', encoding='utf-8')  # utf-8 인코딩 지정해서 읽기
    contents = f.read()  # 다 읽어서 contents에 저장한다.
    print(contents)
    f.close()


# cp949 : ANSI
# utf-8 : Unicode


def f3():
    f = open('first.txt', 'rt', encoding='utf-8')
    two = f.read(2)  # 2글자만 읽는다. (한글, 영문 구분 없음)
    print(two)
    two = f.read(2)
    print(two)
    f.close()


def f4():
    f = open('first.txt', 'rt', encoding='utf-8')
    while True:
        two = f.read(2)  # 반복문에 넣기, 파일이 끝나면 빈 문자열('')을 읽어 들임
        if two == '':
            break
        print(two)
    f.close()


def f5():
    f = open('./storage/third.txt', 'rt')
    while True:
        line = f.readline()  # line에는 \n이 포함되어 있다.
        if line == '':
            break
        print(line)
    f.close()


def f6():
    f = open('./storage/third.txt', 'rt')
    while True:
        line = f.readline()  # line에는 \n이 포함되어 있다.
        if line == '':
            break
        line = line.strip()  # 좌우 공백문자 제거 : \n 제거
        print(line)
    f.close()


def f7():
    f = open('./storage/third.txt', 'rt')
    contents = f.readlines()  # contents는 리스트이다. 한 줄씩 저장된다.
    print(contents)
    for line in contents:
        print(line)
    f.close()


f7()

