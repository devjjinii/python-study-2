'''
표준입출력
'''
import sys

# print("Python", "Java", sep=" vs ", end=" ? ")  # sep = ,들어가는 부분에 들어감
# print("무엇이 더 재밌을까요?") #Python vs Java ? 무엇이 더 재밌을까요?
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") # 왼쪽정렬로 8공간 만들고
                                #오른쪽 정렬 4칸 띄고
 

for num in range(1,21):
      print("대기번호: " +str(num).zfill(3)) # 3크기만큼 공간 확보하고, 0으로 채운다

answer = input("아무 값이나 입력하세요 : ")
# answer = 10
# print(type(answer))
print("입력하신 값은 " + answer + "입니다.")