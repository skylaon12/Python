n1 = int(input('정수1 입력 >>> '))
n2 = int(input('정수2 입력 >>> '))
n3 = int(input('정수3 입력 >>> '))
if n1 >= n2 and n1 >= n3:
    print('가장 큰 수는 {}입니다.'.format(n1))
elif n2 >= n1 and n2 >= n3:
    print('가장 큰 수는 {}입니다.'.format(n2))
else:
    print('가장 큰 수는 {}입니다.'.format(n3))
