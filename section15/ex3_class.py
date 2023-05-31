#클래스
# -> 데이터를 만들기 위한 설계도
# -> 설계도만 있다고 해서 데이터가 실제로 존재하는 것은 아니므로
# 설계도를 통해서 실제로 데이터(객체)를 만들어줘야 한다

#클래스의 구성요소
# 속성(변수), 메서드(기능)

#클래스를 작성하는 방법
# 1) class키워드로 클래스를 정의
# 2) 클래스 이름은 UpperCamelCase규칙을 따른다

#클래스의 기본 구조
'''
class 클래스명 :
    기능 및 속성1
    기능 및 속성2
        ...
'''
class Cat :
    #고양이들의 기본적인 특징들을 정의
    eye = 2 #눈
    nose = 1 #코
    def sleep(self):
        print("잠을 많이잠")

#클래스를 만들었으니, 이를 토대로 고양이 데이터를 만들어보자
num = 10 # <-- 변수
cat1 = Cat() # <-- 객체
print( type(cat1) )
print( "눈 : " , cat1.eye )
print( "코 : " , cat1.nose )
cat1.sleep()

cat2 = Cat()
print( "눈 : " , cat2.eye )
print( "코 : ", cat2.nose)
cat2.sleep()











































