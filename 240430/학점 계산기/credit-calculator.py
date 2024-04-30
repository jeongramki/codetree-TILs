num = int(input())

arr = map(float,input().split())

sum = 0
for elem in arr : 
    sum += elem 


avr = sum/num

print(f"{avr:.1f}")

if avr >= 4.0 : print('Perfect')
elif (4> avr >= 3) : print('Good')
else : print('Poor')