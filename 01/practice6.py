'''
리스트
'''
subway = [10,20,30]
print(subway)

subway = ["찌니10","찌니20", "찌니30"]
print(subway)

print(subway.index("찌니20"))
subway.append("찌니40")
print(subway) # ['찌니10', '찌니20', '찌니30', '찌니40']

subway.insert(1, "찌니0")
print(subway) # ['찌니10', '찌니0', '찌니20', '찌니30', '찌니40']

print(subway.pop())
print(subway) # ['찌니10', '찌니0', '찌니20', '찌니30']

num_list = [5,2,4,1,3]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list) # []

num_list = [5,2,4,3,1]
mix_list = ["찌니", 26, True]

num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, '찌니', 26, True]