# raise
# 1. 파이썬이 인식하지 못하는 예외가 있다.
# 2. 코드를 이용해서 직접 예외를 발생시킬 수 있다.

def f1():
    try:
        print('호프집 입장입니다.')
        age = int(input('나이를 입력하세요 >>> '))
        if age < 0 or age > 150:
            raise Exception  # 일반화 된 예외인 Exception
        if age < 20:
            print('다음에 오세요~')
        else:
            print('어서 오세요~')
    except Exception:
        print('거짓말 하지 마세요~')


def f2():
    try:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(input('확인할 월을 입력하세요 >>> '))
        if month < 1 or month > 12:
            raise RuntimeError  # 실행 중 예외
        print(f'{month}월은 마지막 날이 {days[month - 1]}일이다.')
    except RuntimeError:
        print('1~12 사이로만 입력하세요~')


class Bank:

    # Bank 생성
    # __init__() 메소드
    def __init__(self, no, name, balance):
        self.no = no
        self.name = name
        self.balance = balance

    # 입금 메소드(함수)
    def deposit(self, money):
        if money <= 0:
            raise Exception(f'{money}원 입금 불가')
        self.balance += money

    # 출금 메소드(함수)
    def withdrawal(self, money):
        if money <= 0:
            raise Exception(f'{money}원 출금 불가')
        elif money > self.balance:
            raise Exception(f'{money - self.balance}원 부족')
        self.balance -= money

    # 계좌 조회 메소드(함수)
    def inquiry(self):
        print(f'계좌번호 {self.no} 계좌주 {self.name} 잔액 {self.balance}')


# Bank 객체 생성
me = Bank('010-1234-5678', '민경태', 15000)


# Bank 객체의 메소드는 raise 를 포함하고 있어서
# 예외 처리를 해야 한다.
try:
    me.deposit(5000)
    me.withdrawal(50000)
    me.inquiry()
except Exception as e:  # Exception에 포함된 이유(메시지)를 e로 옮긴다.
    print(e)
