# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("찌니", 2, "자바")
# profile("짜니", 2, "파이썬")

# def profile(name, age=16, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("찌니")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="찌니",  main_lang="파이썬", age=2)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end="")
    for lang in language:
        print(lang, end= " ")
    print()
profile("찌니", 2, "python", "java", "javascript" )    