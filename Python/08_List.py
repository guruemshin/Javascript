# 리스트 : 데이터의 목록을 다루는 자료형 
su=[1, 2, 3, 4, 5]
print(su, type(su))

# indexing
data=[1, "AB", 'apple', 24.5]
print(data[0])            # 1
print(data[-1])           # 24.5

# 리스트 내에 리스트 있는 경우
val=[1, 2, 3, ['a', 'b', 'c']]
print(val[0])           # 1
print(val[-1])         #  ['a', 'b', 'c']
print(val[3])           #  ['a', 'b', 'c']

print(val[-1][0])
print(val[-1][-3])
print(val[3][0])
print(val[3][-3])

# Slicing
num=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(num[0:5])            #  [10, 20, 30, 40, 50]
print(num[:3])              #  [10, 20, 30]
print(num[5:])              #  [60, 70, 80, 90, 100]
print(num[0:8:2])         #   [10, 30, 50, 70]  == for(i=0;i<8;i+=2)
print()

num[0]=77                 # [77, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(num)

num[2:5]=['apple', 'banana', 'melon']      # [77, 20, apple, banana, melon, 60, 70, 80, 90, 100]
print(num)

del num[1]                              #  [77, apple, banana, melon, 60, 70, 80, 90, 100]
print(num)

del num[5:]                              #  [77, apple, banana, melon, 60]
print(num)
print()

# 리스트 연산
a=[1, 2, 3]
b=[4, 5, 6]
c=a+b
d=b+a
print(c)
print(d)
print(a*3)

# 45분 휴식