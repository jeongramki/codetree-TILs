import sys
N = int(input())

A = list(map(int, input().split()))

#모든 케이스 중 최소를 구하는 상황

ans =  8000000 # 큰 값으로 초기화 해주기

for i in range(N) :
    dist = 0 
    for j in range(N) : 
        dist +=abs(i-j) * A[j]
    ans = min(ans, dist)
print(ans)