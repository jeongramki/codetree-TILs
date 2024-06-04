num = int(input())

result = False
arr = []
for i in range(1,num):
    if num % i == 0 : arr.append(i)

if sum(arr) == num : result = True
if result == True : print('P')
else : print('N')