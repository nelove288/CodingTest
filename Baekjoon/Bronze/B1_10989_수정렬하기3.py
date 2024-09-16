# ----- 문제 -----
# 제목 : 수 정렬하기 3
# 번호 : 10989번
# 사용 언어 : Python
# 문제 링크 : https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline

answer = [0] * 10001

N = int(input())
for _ in range(N) :
    num = int(input())
    answer[num] += 1

for i in range(10001) :
    if(answer[i]):
        for j in range(answer[i]):
            print(i)