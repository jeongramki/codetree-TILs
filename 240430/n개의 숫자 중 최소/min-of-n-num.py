num = int(input())
arr = list(map(int,input().split()))

low = min(arr)
cnt=0
for i in arr : 
    if i == low : cnt+=1

print(low, cnt)