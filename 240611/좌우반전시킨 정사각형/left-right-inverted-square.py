n=int(input())

for i in range(1,n+1,1) :
    for j in range(0,n) : 
        print((n-j)*i, end= ' ')
    print()