# ----- 문제 -----
# 제목 : 웰컴 키트
# 번호 : 30802번
# 사용 언어 : Python
# 문제 링크 : https://www.acmicpc.net/problem/30802

import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

answer = 0
for size in sizes :
    if size > 0 :
        answer += math.ceil(size/T)

print(answer)
print(N//P, N%P)
