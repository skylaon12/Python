# exception
# 1. 예외
# 2. 코드 상 발생하는 문제
# 3. 예외 처리 : 문제 처리 과정

# 예외 처리 방식
# try:
#     코드 작성
# except:
#     예외 처리 코드 작성

# try:
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     month = int(input('확인할 월을 입력하세요 >>> '))
#     print(f'{month}월은 마지막 날이 {days[month - 1]}일이다.')
# except IndexError:
#     print('문제가 발생했습니다.')


try:
    f = open('hello.txt', 'rt')
    contents = f.read()
    print(f)
    f.close()
except FileNotFoundError:
    print('실패했습니다.')
