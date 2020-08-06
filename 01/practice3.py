'''
연산자
'''
print(2**3) # 2^3
print(5 % 3) # 5/3 나머지
print(5//3) # 5/3 몫
print(4 >= 7) #False
print(3 == 3) #True
print(3 + 4 == 2) # False
print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True &
print((3 > 0) or (3 > 5)) # True |

print((5 > 4 > 3)) # True
print((5 > 4 > 7)) # False

number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2 # 18
print(number)

number %= 2
print(number)

'''
숫자처리함수
'''
print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

from random import *
print(random()) # 난수 0.0 ~ 1.0 미만의 임의의 값
print(random() * 10) # 0.0 ~ 10.0
print(int(random() * 10))
print(int(random()* 10) + 1) # 1~ 10이하의 정수

# 로또 숫자
print(int(random() * 45) + 1)
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하
