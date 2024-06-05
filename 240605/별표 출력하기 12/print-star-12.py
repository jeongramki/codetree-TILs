n=int(input())

for i in range(n) : 
    if i == 0 : 
        for _ in range(n) : print('*', end = ' ')

    else : 
        for j in range(n) :
            if j < i : print(' ', end = ' ' )
            elif (j>=i) and (j%2==1) : print('*',end=' ')
            elif (j>=i) and (j%2==0) : print(' ',end=' ')
            else : print('')

         
    print('')