import math


def ceil(target, n):
    return math.ceil(target * (10 ** n)) / (10 ** n)


def floor(target, n):
    return math.floor(target * (10 ** n)) / (10 ** n)


# 소수 1자리 올림
# target : 1.111
# goal   : 1.2
# 과정
# 1) 1.111 * 10 : 11.11
# 2) math.ceil(11.11) : 12
# 3) 12 / 10 :

# 소수 2자리 올림
# target : 1.111
# goal   : 1.12
# 과정
# 1) 1.111 * 100 : 111.1
# 2) math.ceil(111.1) : 112
# 3) 112 / 100 : 1.12

# 소수 n자리 올림
# math.ceil(target * 10의 n제곱) / 10의 n제곱
