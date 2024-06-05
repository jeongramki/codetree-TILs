n=int(input())

for i in range(n,0,-1) : 
    for j in range(i) : print('*',end='')

    for k in range(2*(n-i)) : print(' ',end='')
    for m in range(i): print('*',end='')

    print('')