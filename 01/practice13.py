'''
pickle & with
'''
import pickle
# profile_file=open("profile.pickle", "wb") # 바이너리
# profile = {"이름":"찌니", "나이":2, "취미": ["축구","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 파일에 저장한다.
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러온다
# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부중")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())