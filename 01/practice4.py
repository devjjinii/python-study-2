'''
문자열
'''
sentence = '나는 찌니입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 찌니이고,
파이썬은 쉬워요
"""
print(sentence3) # 줄바꿈 포함 4줄

'''
슬라이싱
'''
jumin = "991111-2234567"
print("성별 : " + jumin[7])
print("년도 : " + jumin[0:2]) # 2번째 직전까지
print("월 : " + jumin[2:4])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " +jumin[7:]) # 7번째부터 끝까지
print("뒤 7자리 (뒤에서부터) : " +jumin[-7:])

'''
문자열처리함수
'''
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # True
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # -1 값이없을때
# print(python.index("Java")) # 오류 error

print(python.count("n"))