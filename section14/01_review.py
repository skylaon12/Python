# ./file/학생명단.csv

f = open('./file/학생명단.csv', 'rt')

line = f.readline()  # 제목을 쓸 게 없다.
print(line)

while True:
    line = f.readline()
    if line == '':
        print('학생명단.csv 모든 데이터를 읽었습니다.')
        break
    print(line)

f.close()

f = open('./file/학생명단.csv', 'rt')
line = f.readline()
print(line)
