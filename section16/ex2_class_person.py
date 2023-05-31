'''
사람들의 정보를 저장하기 위한 Person클래스 만들기!
1.클래스명은 Person으로 만든다
2.이름, 나이를 세팅하는 함수 만들기
3.이름, 나이를 출력하는 함수 만들기
'''
class Person:
    #name
    #age
    #job
    #home
    #location
    def setting(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("제 이름은 %s이고, 나이는 %d입니다" %( self.name, self.age ) )

    def isAdult(self):
        if self.age >= 20 :
            print("성인입니다")
        else :
            print("성인이 되려면 %d년 남았습니다" %(20 - self.age))

    def myJob(self, job):
        self.job = job
        print("저의 직업은 %s입니다" %job)

    def myArea(self, home, location):
        self.home = home
        self.location = location
        print( "저의 집은 %s(이)고, 직장은 %s입니다" %(home, location) )

    def myVar(self):
        print("제 이름은 %s(이)고, 나이는 %d입니다" %(self.name, self.age))
        print("제 직업은 %s입니다" %self.job)
        print("저의 집은 %s(이)고, 직장은 %s입니다" %(self.home, self.location))

hong = Person()
hong.setting("홍길동", 17)
hong.intro()
hong.isAdult()
hong.myJob("의사")
hong.myArea("강남", "신촌")
hong.myVar()

print("-------------------------")

kim = Person()
kim.setting("김길동", 30)
kim.intro()
kim.isAdult()

print("-----------------------------------")

'''
문) 위 클래스에 isAdult()함수를 만들고
나이가 20세 이상일 경우 '성인입니다'
그렇지 않을경우 '성인이 되려면 ?년 남았네요'를 출력
'''

#문) myJob()함수를 호출하면 '저의 직업은 xx입니다'를 출력
#문) myArea() 함수를 호출하면 '저의 집은 xx이고, 직장은 xx입니다'를 출력
#문) myVar() 함수를 호출하면 가지고 있는 모든 정보를 보여주기
     #제 이름은 xx(이)고, 나이는 xx입니다
     #제 직업은 xx입니다
     #저의 집은 xx(이)고, 직장은 xx입니다














