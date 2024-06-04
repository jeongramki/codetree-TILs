num = int(input())
arr=[]
for i in range(num) : 
    arr.append(int(input()))

for i in arr : 
    if i%2==1 and i%3==0 : print(i)