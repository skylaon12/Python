# csv
# comma separated values
# 콤마로 분리된 값들

# 처리방법
# 1. 문자열 메소드 split(',')
# 2. csv 모듈 import

def f1():
    f = open('./file/학생명단.csv', 'rt')
    f.readline()  # 제목 읽어 들이기
    names = []
    while True:
        line = f.readline()  # line = '10101,김승별,서울시 영등포구,010-1111-1111\n'
        if line == '':
            break
        line = line.strip()  # line = '10101,김승별,서울시 영등포구,010-1111-1111'
        line = line.split(',')  # line = ['10101', '김승별', '서울시 영등포구', '010-1111-1111']
        names.append(line[1])  # names = ['김승별']
    f.close()

    print(names)


import csv


def f2():
    f = open('./file/학생명단.csv', 'rt')
    students = csv.reader(f, delimiter=',')
    # students = [
    #     ['학번', '이름', '주소', '연락처'],
    #     ['10101', '김승별', '서울시 영등포구', '010-1111-1111'],
    #     ...
    # ]
    names = []
    for student in students:
        names.append(student[1])

    names.pop(0)
    print(names)
    f.close()


def f3():
    f = open('./file/회원명단.csv', 'rt')
    members = csv.reader(f, delimiter=',', quotechar='"')
    # delimiter=',' : 데이터는 콤마(,)로 구분되어 있다.
    # quotechar='"' : 콤마(,)로 연결되어 있으나 구분하면 안 되는 데이터는 큰 따옴표(")로 묶여 있다.
    for member in members:
        print(member)
    f.close()


def f4():
    # cctv.csv
    # 마포구에 설치된 전체 cctv 몇 대인가?
    f = open('./file/cctv.csv', 'rt')
    contents = csv.reader(f, delimiter=',', quotechar='"')
    contents = list(contents)  # contents를 리스트로 변경
    contents.pop(0)  # 제목은 제거
    total = 0
    for content in contents:
        total += int(content[4])
    print(f'마포구 전체 cctv는 {total}대입니다.')  # 2167대


f4()
