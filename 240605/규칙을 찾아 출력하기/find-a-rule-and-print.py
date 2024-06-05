n=int(input())

for i in range(n) : 
    if i == 0 or i == n : 
        for _ in range(n): print('*',end=' ')

    else : 
        for j in range(n) : 
            if j < i : print('*',end=' ')
            elif i<=j<n-1 : print(' ',end=' ')
            elif j==n-1 : print('*',end=' ')
    print('')