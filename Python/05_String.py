# 문자열
# 문자열 사용방법 : ',  ",  """,  '''
a="Hello World"
b='안녕하세요'
c="""Life is too short, You need Python"""
d='''인생은 너무 짧으니, 파이썬이 필요함'''
print(a, "\t" , b , "\t", c, "\t", d, "\n")

# 여러줄인 무자열을 변수 대입하고 싶을때
x="Hello \n World"
y='''어서와
파이썬은
처음이지?'''
print(x) 
print(y) 

# 문자열 안에 따옴을 포함하고 싶을때
food="Python's favorite food is perl"
say='"Python is very easy". hs says'
backSay="\"Python is very easy\". hs says"
print(food)
print(say)
print(backSay, "\n\n")

# 문자열 연산 (+, *)
head="Python"
tail="is fun"
print(head + tail)
print(head * 3)

# 형변환
su=55.5
print(su, type(su))      # 55.5, float

x=su                          # x 55.5 =su 55.5
print(x, type(x))          # 55.5, float

y=int(su)                   # 형변환 
print(y, type(y))
print("\n\n")

strNum=input("숫자입력하세요:")
print(strNum, type(strNum))

num=int(strNum)
print(num, type(num))

val=int(input("숫자 또 입력해:"))
print(val, type(val))

