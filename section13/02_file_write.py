# 파일 출력 스트림 생성


def f1():
    f = open('first.txt', mode='wt')  # f = open('first.txt', 'wt')
    f.write('hello\n')  # 출력 메소드 : write()
    f.write('python')
    f.close()


def f2():
    f = open('../second.txt', 'wt')
    f.write('hello\npython')
    f.close()


def f3():
    f = open('./storage/third.txt', 'wt')
    f.write('안녕\n파이썬')
    f.close()


def f4():
    file_name = input('생성할 파일명을 입력하세요 >>> ')
    f = open('./storage/' + file_name + '.txt', 'wt')
    contents = input('파일에 기록할 내용을 입력하세요 >>> ')
    f.write(contents)
    f.close()


def f5():
    f = open('./storage/20210823.txt', mode='wt', encoding='utf-8')  # 인코딩 변경 (utf-8)
    f.write('오늘은 20210823입니다.')
    f.close()


f3()
