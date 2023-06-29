# 연산자
#  산술연산자 : +, -, *, / 등
a=10
b=3
print(a/b)               # 나눗셈
print(a//b)             # 몫
print(a%b)             # 나머지
print(a ** b)           # 거듭제곱
print("\n")

# 관계연산자
x=10
y=3
print(x==y)         # 10 == 3
print(x !=y)          # 10 != 3
print(x > y)          # 10 > 3
print(x < y)
print(x >=y)
print(x <= y)
print("\n")

# 논리연산자
su=10
value=20
result1=su > 0 and su < 20
result2=su == 10 or su == 20
result3=not(su%2==0)
print(result1)
print(result2)
print(result3)

# 대입연산자
num=100             
num +=2      # 102
num -=2      # 100
num *=2      # 200
num //=2    #100
print(num)

# *** 멤버 연산자
my_list=[1, 2, 3]
print(2 in my_list)          # T     항목이 있는지 여부
print(4 not in my_list)    # T     항목이 없는지 여부

# bool
i=True
j=False
print(i)
print(j)




