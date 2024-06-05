n=int(input())

for i in range(1, 2*n+1) : 
    if i%2 ==1 : 
        for _ in range(int(n-(i-1)/2)) : print('*',end=' ')
        print('')

    else : 
        for _ in range(int(i/2)) :print('*',end=' ')
        print('')