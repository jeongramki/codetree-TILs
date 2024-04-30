arr = map(int,input().split())

sum=0
count = 0

for elem in arr :
    if elem >= 250 : break
    sum += elem
    count += 1
print(sum, sum/count)