'''
for
'''

for waiting_no in [0,1,2,3,4]:
    print("대기번호: {0}".format(waiting_no))

# for waiting_no in range(5): # 0,1,2,3,4
#     print("대기번호: {0}".format(waiting_no))

starbucks = ["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
   

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102 ...
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Thor", "I am groot", "Iron man"]
students = [len(i) for i in students]
print(students)