# JSON
# JavaScript Object Notation
# 자바스크립트 객체 표기법

# 처리방법
# json 모듈을 import 한다.
# json.loads() 함수를 사용한다. 그러면 json 데이터가 파이썬의 딕셔너리로 변환된다.


import json


f = open('./file/cctv.json', 'rt', encoding='utf-8')

# cctv.json 데이터를 모두 읽어 들인다.
contents = f.read()

# contents를 딕셔너리(파이썬의 데이터)로 바꾼다.
contents = json.loads(contents)

for content in contents:
    print(content['소재지지번주소'])
