class Pokemon :
    name = "피카츄"
    type = "전기"
    def info(self):
        print("이름 : ", self.name) #self:현재 클래스 자신
        print("타입 : ", self.type)
        print("--------")

#똑같은 Pokemon클래스를 통해서 만들어진 객체지만
#pika객체는 피카츄가, ggobugi객체는 꼬부기로써의 역할을 수행할 수 있도록
#생성되는 클래스의 구조를 '다형성' 이라고 한다
pika = Pokemon()
pika.info()

ggobugi = Pokemon()
ggobugi.name = "꼬부기"
ggobugi.type = "물"
ggobugi.info()

#클래스의 특징
# 원하는대로 데이터를 커스터마이징 할 수 있다
# 같은 클래스로 만든 객체라고 해도 서로 독립적으로 동작














