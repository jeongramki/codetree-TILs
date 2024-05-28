a,b,c=map(int, input().split())

middle= 0 

if a<=b<=c :print(b)
elif c<=b<=a :print(b)
elif a<=c<=b:print(c)
elif b<=c<=a :print(c)
elif b<=a<=c :print(a)
elif c<=a<=b :print(a)
else : pass