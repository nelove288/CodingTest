# ----- 문제 -----
# 제목 : 소수
# 번호 : 1312번
# 사용 언어 : Python
# 문제 링크 : https://www.acmicpc.net/problem/1312

A,B,N = map(int, input().split())

for i in range(N) :
    A = (A%B)*10
    answer = A//B
    
print(answer)