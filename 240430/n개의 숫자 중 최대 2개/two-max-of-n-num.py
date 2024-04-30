num = int(input())

arr= list(map(int, input().split()))
arr.sort()

print(arr[num-1],arr[num-2])