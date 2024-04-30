a=1
b=int(input())

print(a,b,end=' ')


while True:
    c=a+b
    print(c,end=' ')
    a,b= b,c
    if (c>=100) : break