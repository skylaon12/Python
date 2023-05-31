class Calcul:
    #num1
    #num2
    def sum(self, num1, num2):
        result = num1 + num2
        print("%d + %d = %d" %(num1, num2, result))

    def sub(self, num1, num2):
        result = num1 - num2
        print("%d - %d = %d" %(num1, num2, result))

    def mul(self, num1, num2):
        result = num1 * num2
        print("%d * %d = %d" % (num1, num2, result))

    def div(self, num1, num2):
        if num2 != 0 :
            result = num1 / num2
            print("%d / %d = %d" % (num1, num2, result))
        else :
            print("0으로는 나눌 수 없어요")

c1 = Calcul()
c1.sum(10, 5)
c1.sub(15, 7)
c1.mul(5, 2)
c1.div(10, 0)

#Calcul 클래스에
#sub로 빼기, mul로 곱하기, div로 나누기가 가능하도록 함수를 만들고 출력
