# ----- 문제 -----
# 제목 : 달팽이는 올라가고 싶다
# 번호 : 2869번
# 사용 언어 : Python
# 문제 링크 : https://www.acmicpc.net/problem/2869

import sys
input = sys.stdin.readline

A, B, V = map(int,input().split())
day = (V - A) / (A - B) + 1
day = int(day) if day == int(day) else int(day)+1
print(day)