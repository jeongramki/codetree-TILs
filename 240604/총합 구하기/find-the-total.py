a,b=map(int,input().split())
arr=[]
for i in range(a,b+1) : 
    if (i % 6 == 0) and (i%8 != 0) : arr.append(i)
print(sum(arr))