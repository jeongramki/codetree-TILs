num = int(input())

arr = list(map(int, input().split()))

arr.sort()
sum = [] 
for i in range(num) : 
    sum.append (arr[i-0] + arr[num+1-i])

print(max(sum))