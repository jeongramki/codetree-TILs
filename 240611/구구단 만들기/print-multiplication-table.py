a,b = map(int,input().split())

arr = []

for i in range(b,a-1,-1) : 
    if i % 2 == 0 : arr.append(i) 

for i in range(1,10) :
    for j in arr : 
        if j != 2 : 
            print(f'{j} * {i} = {j*i} /' ,end=' ') 
        else : 
            print(f'{j} * {i} = {j*i}' ,end=' ') 
    
    print()