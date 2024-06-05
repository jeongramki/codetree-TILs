n=int(input())

for i in range(n):
    for j in range(n) : 
        if j < i : print(' ',end = ' ')
        elif j %2 == 0 and j>= i : print('*',end = ' ')
        elif j%2 ==1 and j>=i : print(' ',end=' ')
    print('')