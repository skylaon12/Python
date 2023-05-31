#input()을 통해서 입력받은 데이터는 기본적으로 문자열 이므로
#in1, in2에 들어간 값은 정수형태가 아닌 문자열 구조의 "1", "3"형태가 된다
in1 = input("수1 : ") #1
in2 = input("수2 : ") #3
sum = int(in1) + int(in2)
print( "결과 : ", sum )

print("--------------------------------")

#입력 : 1, 3, 5
#총 합은 9 입니다

#힌트 : 입력받은 데이터를 ,단위로 구분하여 리스트에 저장
#리스트의 저장된 값들을 숫자로 변환하여 for문을 통해 합을 구한다
num = input("입력 : ")
list = num.split(",")
sum = 0
for i in list:
    sum += int(i)

print("총 합은 %d 입니다" %sum)
print("총 합은 ", sum, "입니다")












