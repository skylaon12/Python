# 1부터 더하기를 한다. ( 1 + 2 + 3 + ... )
# 누적된 합계가 500 보다 커지면 그만하겠다.

# 합계 : sum, total, hapgye 등
# total = 0
# total += 1
# total += 2
# total += 3
# ...


# 초기화
total = 0
n = 1

# 합계(total)가 500보다 크면 그만
# 합계(total)가 500보다 작거나 같으면 계속
while total <= 500:
    total += n
    n += 1

print(f'1부터 {n - 1}까지 더한 합계는 {total}이다.')


# while문은 반복 횟수가 명확하지 않을 때 사용하면 좋다.
