arr = list(map(int,input().split())) 

for elem in arr :
    if elem == 999 or elem == -999 : arr.remove(elem)

print(max(arr), min(arr))