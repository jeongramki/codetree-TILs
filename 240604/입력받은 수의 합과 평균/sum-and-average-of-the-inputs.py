num = int(input())
arr=[]
for i in range(num) : 
    arr.append(int(input()))

print(sum(arr), format((sum(arr)/num),".1f"))