n = int(input('정수를 입력하세요 >>> '))
if n % 3 == 0 and n != 0:
    print('{}는 3의 배수입니다.'.format(n))
else:
    print('{}는 3의 배수가 아닙니다.'.format(n))
