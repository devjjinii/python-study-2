'''
continue & break
'''
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡
for student in range(1, 11): # 1-10
    if student in absent:
        continue   # 2,5은 실행하지 않고 
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

