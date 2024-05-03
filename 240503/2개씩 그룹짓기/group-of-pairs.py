num = int(input())

arr = list(map(int, input().split()))

arr.sort()

sum = [] 
for i in range(num) : 
    sum.append (arr[i] + arr[2*num-1-i])

print(max(sum))