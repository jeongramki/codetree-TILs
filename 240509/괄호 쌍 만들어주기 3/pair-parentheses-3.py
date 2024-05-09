"""N=4
A= [1,5,2,6]

ans= 0

for i in range(N):
    for j in range(i+1,N):
        S =0 
        A[i] *=2
        A[j] *=2
        for k in range(N-1):
            S+=abs(A[k]-A[k+1])
        ans = max(ans,S)

        A[i]//=2
        A[j]//=2
print(ans)
"""


ans=0
"""
S= input()

for i in range(len(S)) : 
    for j in range(i+1,len(S)): 
        if S[i] == "(" and S[j] == ")":
            ans +=1"""

cnt=0 # 여는 괄호의 수
for s in input() : 
    if s == "(":
        cnt+=1
    else : 
        ans += cnt
print(ans)