num = int(input())


pass_stu = 0
result_arr=[]
for i in range(num) : 
    scores = list(map(int, input().split()))
    avr = sum(scores)/4
    if avr >= 60 : 
        pass_stu += 1
        result_arr.append('pass')
    else :
        result_arr.append('fail')

for i in range(num) : 
    print(result_arr[i])

print(pass_stu)