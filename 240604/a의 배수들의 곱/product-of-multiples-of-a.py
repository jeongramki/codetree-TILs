a,b=map(int,input().split())

base =1 
for i in range(1,b+1): 
    if i % a == 0 : base *= i
print(base)