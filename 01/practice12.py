# 빈자리는 빈공간으로 두고, 오른쪽정렬을 하되 , 총 10자리 공간을 확보
# 양수 일땐 + 로 표시
print("{0: >+10}".format(500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기 양수는 +
print("{0:+,}".format(100000000))
# 소수점 출력
print("{0:f}".format(5/3))

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# # print(score_file.readline()) 줄별로 읽기, 
# score_file.close()

# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()