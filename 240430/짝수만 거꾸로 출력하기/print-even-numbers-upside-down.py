arr = list(map(int, input().split()))
new_arr=[]
count=0
for elem in arr : 
    if (elem%2==0) : 
        new_arr.append(elem)
        count += 1

if new_arr == [] : print(0)

for i in range(count) :
    print(new_arr[count - i -1] ,end = ' ' )