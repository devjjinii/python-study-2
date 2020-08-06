'''
사전
'''
cabinet = {3:"찌니", 100: "짜니"} # key:value
print(cabinet[3])
print(cabinet.get(3))
# print(cabinet[5]) # error
#print(cabinet.get(5)) # None
#print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

del cabinet[100]
print(cabinet) # {3: '찌니'}

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet) # {}

'''
튜플
'''
menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스") # error

name = "찌니"
age = 2
print(name, age)

(name, age) = ("찌니", 2)
print(name, age)

'''
집합 (set) : 중복 안됨, 순서 없음
'''
my_set = {1,2,3,3,3}

java = {"찌니", "짜니"}
python = set(["찌니", "탄"])

print(java & python) # {'찌니'}
print(java.intersection(python))

print(java | python)
print(java.union(python))

# 자바는 할 수 있지만, python은 할 줄 모르는
print(java - python)
print(java.difference(python))

python.add("콩")
print(python)

# java.remove("짜니")

'''
자료구조의 변경
'''
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu)) # {'쥬스', '우유', '커피'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['커피', '쥬스', '우유'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('우유', '커피', '쥬스') <class 'tuple'>
