#클래스 이름의 첫글자는 반드시 대문자로 하자
class Dog:
    #name = "댕댕이"
    def setting(self, name):
        self.name = name

    def info(self):
        print("강아지의 이름을 %s로 정했다!" %self.name)

d1 = Dog()
d1.setting("댕댕이")
d1.info()
