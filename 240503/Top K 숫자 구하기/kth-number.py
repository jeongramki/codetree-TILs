num, seq = tuple (map(int, input().split())) #튜플?
arr = list(map(int, input().split())) 

arr.sort()

print(arr[seq-1])