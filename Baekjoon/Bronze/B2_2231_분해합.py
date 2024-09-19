# ----- 문제 -----
# 제목 : 분해합
# 번호 : 2231번
# 사용 언어 : Python
# 문제 링크 : https://www.acmicpc.net/problem/2231

N = int(input())
answer = 0

constructor = []
for num in range(N+1) :
    decomposition_sum = sum(map(int,list(str(num))))
    if num + decomposition_sum == N :
        constructor.append(num)

answer = 0 if len(constructor) == 0 else constructor[0]
print(answer)