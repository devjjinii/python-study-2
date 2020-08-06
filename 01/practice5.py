'''
문자열포맷
'''
print("a" + "b")
print("a", "b")

#방법 1
print("나는 %d살입니다" % 26) #정수
print("나는 %s을 좋아해요" % "파이썬") #문자열
print("Apple 은 %c로 시작해요." % "A") #문자
# %s
print("나는 %s살입니다" % 26) #정수
print("나는 %s색과 %s색을 좋아해요" % ("파란", "분홍"))

# 방법 2
print("나는 {}살입니다.".format(26))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요" .format(age=26, color="파란"))

# 방법 4(v3.6~)
age = 26
color = "파란"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

'''
탈출 문자
'''
print("백문이 불여일견\n백견이 불여일타") # /n : 줄바꿈
print("저는 \"찌니\"입니다.")

# \\ : 문장 내에서 \
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스
print("Redd\bApple")