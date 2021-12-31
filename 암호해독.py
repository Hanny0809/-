# 암호 해독하여 문자열로 출력하기

# 암호를 배열(Array)로 변경
text = ['   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ']

# for을 이용하여 text 출력
l = []
for i in text:
    l.append(chr(int(i.strip().replace(' ','').replace('+', '1').replace('-','0'),2)))
print(''.join(l))

'''
앞, 뒤 공백제거 --> strip()
중간 공백 제거 replace(' ', '')
+ -> 1 , - -> 0 으로 대체 replace() 이진수로 변경
이진법으로 인식하게 하고 십진법으로 변경 (int 와 끝에 2를 추가)
숫자를 문자열로 바꾸기 chr()
l을 리스트로 선언하고 append()함수를 이용 
''.join(리스트)을 이용하여 문자열로 출력
'''


# 한줄로 출력
result = ''.join([chr(int(i.strip().replace(' ','').replace('+', '1').replace('-','0'),2)) for i in text])
print(result)

# 함수를 이용하여 해결하기
# 1. 람다 함수 이용
arr1 = [i.strip().replace(' ','').replace('+', '1').replace('-','0') for i in text]
print(arr1)  # ['1001010', '1000101', '1001010', '1010101']

result2 = list(map(lambda x : chr(int(x, 2)), arr1))
print(result2)  # ['J', 'E', 'J', 'U']
'''
map()사용
lambda 함수 : int형을 바꿔주고 문자열을 바꿔주도록 함  
'''

# def로 정의하기
def fun(x):
    return chr(int(x, 2))
''.join(list(map(fun, arr1)))
