# ----- 문제 -----
# 제목 : 직각삼각형
# 번호 : 4153번
# 사용 언어 : Python
# 문제 링크 : https://www.acmicpc.net/problem/4153

while(True) :
    num = list(map(int,input().split()))
    
    if(not all(num)) :
        break
    
    num.sort()
    if(num[0]**2+num[1]**2==num[2]**2) :
        print("right")
    else :
        print("wrong")