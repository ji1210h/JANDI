'''
38번: 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
'''
a = int(input("정수 1개를 입력해주세요: "))
b = int(input("정수 1개를 더 입력해주세요: "))
print(a+b)

'''
39번: 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input("정수 두개를 공백을 두고 입력해주세요: ").split())
print(a+b)

'''
40번: 입력된 정수의 부호를 바꿔 출력해보자.
'''

a = int(input("정수 1개를 입력해주세요: "))
print(-a)

'''
41번: 영문자 1개를 입력받아 그 다음 문자를 출력해보자.
영문자 'A'의 다음 문자는 'B'이고, 영문자 '0'의 다음 문자는 '1'이다.
'''
a = ord(input("영문자 1개를 입력해주세요: "))
print(chr(a+1))

'''
42번: 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.
'''
a, b = map(int, input("정수 두개를 공백을 두고 입력해주세요: ").split())
print(a/b)

'''
43번: 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
'''
a, b = map(float, input("정수 두개를 공백을 두고 입력해주세요: ").split())
print(a % b)

'''
44번: 정수를 1개 입력받아 1만큼 더해 출력해보자.
'''
a = int(input("정수 1개를 입력해주세요: "))
print(a+1)

'''
45번: 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
'''
a, b = map(int, input("정수 두개를 공백을 두고 입력해주세요: ").split())
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)
print(a, "/", b, "=", round(float(a/b), 2))
print(a, "%", b, "=", float(a % b))

'''
46번: 정수 3개를 입력받아 합과 평균을 출력해보자.
'''
a, b, c = map(int, input("정수 3개를 공백을 두고 입력해주세요: ").split())
print(a, "+", b, "+", c, a+b+c)
print("평균은 ", round(float(a+b+c)/3, 2))