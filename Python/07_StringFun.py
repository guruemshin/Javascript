# 문자열 함수
s="Hello World"
print("문자 개수를 세는 함수", s.count('o'))
print("문자열 위치를 찾는 함수(앞)", s.find('H'))     # 해당 문자가 없으면 -1
print("문자열 위치를 찾는 함수(뒤)", s.rfind('r'))
print("문자열 위치를 찾는 함수", s.index('H'))           # 해당 문자가 없음 ERROR
print("문자열 대문자", s.upper())
print("문자열 소문자:", s.lower())
print("문자열 치환", s.replace("World", "한국"))
print()

i="                안녕하세요"
j="안녕하세요                           "
k="                안녕하세요           "
print("문자열 왼쪽 공백제거", i.lstrip)
print("문자열 오른쪽 공백제거", j.rstrip)
print("문자열 양쪽 공백제거", k.strip)
print()

x="ABCDefg"
y="1234"
z="1234ABC"
print("문자열로 이루어져 있는가", x.isalpha())
print("숫자로만 이루어졌 있는가?", y.isnumeric())
print("숫자와 문자로 이루어져있는가:", z.isalnum())
print()

ch="Apple Oragne Kiwi"     # 공백을 기준으로 문자열 나눔
print("문자열", ch, type(ch))

chList=ch.split(" ")
print(type(chList), chList)
print("해당 index 값:", chList[0], chList[1], chList[2])

strCh=" ".join(chList)
print(strCh, type(strCh))

