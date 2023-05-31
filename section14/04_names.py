# yob1880.txt
# yob1881.txt
# ...
# yob2015.txt
#############
# 'yob' + year + '.txt'

# 파일의 존재 여부를 검사하는 기능을 제공하는 os 모듈 포함
import os
import csv


for year in range(1880, 2016):

    filename = f'./file/names/yob{year}.txt'

    # 존재하지 않으면 열지 않겠다.
    if not os.path.exists(filename):
        continue

    # 파일 열기
    f = open(filename, 'rt', encoding='utf-8')

    # 파일 내용 읽기
    contents = csv.reader(f, delimiter=',')

    # contents = [
    #     ['Mary', 'F', '7065'],
    #     ['Anna', 'F', '2604'],
    #     ...
    # ]

    # 여아/남아 이름 저장할 세트
    girl_names = set()
    boy_names = set()

    # 여아/남아 인원수
    girl_count = 0
    boy_count = 0

    for content in contents:
        # content = ['Mary', 'F', '7065']
        # content[0] : 'Mary', content[1] : 'F', content[2] : '7065'
        if content[1] == 'F':
            girl_names.add(content[0])
            girl_count += int(content[2])
        elif content[1] == 'M':
            boy_names.add(content[0])
            boy_count += int(content[2])

    print(f'{year}년도 여아: {girl_count}명, 남아: {boy_count}명')
    print(f'{year}년도 여아 이름 수: {len(girl_names)}개, 남아 이름 수: {len(boy_names)}')
