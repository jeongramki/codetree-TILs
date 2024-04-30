a,b = map(int,input().split())

print(a,b,end=' ')
for i in range(8) : 
    c=b+2*a
    print(c,end=' ')
    a,b=b,c