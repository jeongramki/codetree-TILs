n=int(input())
cnt=1

ans = [
    [0 for _ in range(n)] for _ in range(n)
]
time = 0 
for j in range(n-1,-1,-1) : 
    if time % 2 == 0 :
        for i in range(n-1,-1,-1) : ans[i][j] = cnt; cnt +=1 ;
    else : 
        for i in range(n) : ans[i][j] = cnt; cnt +=1 ;
    time +=1 
    

for i in range(n) :
    for j in range(n) : 
        print(ans[i][j], end = ' ')
    print()