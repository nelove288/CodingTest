# ----- 문제 -----
# 제목 : 소수 찾기
# 번호 : 1978번
# 사용 언어 : Python
# 문제 링크 : https://www.acmicpc.net/problem/1978

import math

N = int(input())
nums = list(map(int,input().split()))

answer = []
for i in range(N) :
    if(nums[i] == 1) :
        continue
    tmp = math.floor(nums[i]**1/2)
    
    for j in range(2,tmp+1) :
        if(nums[i] % j == 0) :
            break
    else :
        answer.append(nums[i])

print(len(answer))