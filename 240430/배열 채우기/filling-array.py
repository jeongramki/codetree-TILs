arr = list(map(int,input().split()))
sum = 0
count = 0
for elem in arr : 
    if elem == 0 : break
    sum += elem
    count += 1

for i in range(count) : 
    print(arr[count-i-1],end = ' ')