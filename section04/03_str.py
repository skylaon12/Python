# 문자열
# 1. + : 문자열을 붙인다. (concatenate)
# 2. * : 문자열을 반복한다. (repeat)

s = 'hello'

print(f'{s + " python"}')
print(f'{s * 3}')


# 참고.
# 리스트도 동일하게 동작한다.
wish_list = ['신발', '외투']
bucket_list = ['스카이다이빙', '번지']
print(wish_list + bucket_list)
print(wish_list * 3)


# 문자열 + 수치 가능한가? No. str끼리만 된다.
print(s + str(7))
print(s + '7')
