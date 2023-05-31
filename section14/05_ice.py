# 바이너리 파일

# 주의.
# 1. 모드 : b
# 2. read() 메소드
#    1) 텍스트 모드  : read(1) -> 1글자를 읽는다.
#    2) 바이너리 모드 : read(1) -> 1바이트를 읽는다.

# 저장 단위
# (비트) -> 바이트(8비트) -> KB(킬로) -> MB(메가) -> GB(기가) -> TB(테라) -> PB(페타)
#           문자           1024바이트   1024KB     1024MB     1024GB      1024TB

# ice.mp4 파일의 복사
# 1. ice.mp4 파일의 일부를 읽는다. (파일 읽기)
# 2. 읽은 내용을 변수에 저장한다.
# 3. 변수의 내용을 이용해서 ice2.mp4 파일을 만든다. (파일 쓰기)

import datetime


f1 = open('./file/ice.mp4', 'rb')
f2 = open('./file/ice2.mp4', 'wb')

start = datetime.datetime.now()
while True:
    buffer = f1.read(1024)
    if not buffer:  # buffer가 비어 있다 = f1의 모든 내용을 읽었다.
        print('ice2.mp4 파일이 복사되었습니다.')
        break
    f2.write(buffer)
end = datetime.datetime.now()

f1.close()
f2.close()

elapse = end - start
print(f'복사에 걸린 시간: {elapse.total_seconds()}초')
