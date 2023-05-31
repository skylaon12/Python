# 파일에 내용 추가


def f1():
    f = open('my.txt', 'at')  # at : 텍스트 추가 모드
    f.write('hello\n')
    f.close()


def f2():
    f = open('my.txt', 'at')
    f.write('python\n')
    f.close()


f2()
