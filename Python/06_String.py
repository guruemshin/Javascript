# 문자열 인덱싱
a="Life is too short, You need Python"
print(a[0])              # L
print(a[-1])            # n
print(a[12])           # s

# 문자열 슬라이싱 : 범위 [begin:end:step]
b="GoodMorning"
print(b[0:4])               # 0~3    Good
print(b[0:8:2])            # GoMr
print(b[0:8:3])             #Gdr 
print(b[:4])                  # 0~3    Good
print(b[4:])                  # 4~end   Morning
print(b[4:11])              # 4~10
print("\n\n")

# 문자열 포맷들
name="홍길동"
age=23
print("이름:", name, "\t 나이:",  age)

print("이름:%s 나이:%d" %(name, age))
print("이름:{} 나이:{}".format(name, age))
print("나이:{1} 이름:{0}".format(name, age))
print(f"나의 이름은 {name} 입니다. 나이는 {age} 입니다.")
print("\n\n")

# 출력서식 지정
print("%10s" %"hi")                # ^^^^^^^^hi     오른쪽 정렬
print("%-10s" %"hi")               # hi^^^^^^^^    왼쪽 정렬
print("%-10sapple" %"hi")      # hi^^^^^^^^apple
print("%0.4f" %3.42135234)    # 3.4214
print("%10.4f" %3.42135234)   # ^^^^3.4214






