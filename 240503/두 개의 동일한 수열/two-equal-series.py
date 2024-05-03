num = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()
res = True

for i in range(num) : 
    if A[i-1] != B[i-1] : res = False

if (res == False ) : print('No')
else : print('Yes')