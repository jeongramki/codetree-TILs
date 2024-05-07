x,y = 0,0
dir_num = 0 
dx=[0,1,0,-1]
dy=[1,0,-1,0]

inp = input()
if inp == 'LF' :
    dir_num -=1
    x += dx[dir_num]
    y+= dy[dir_num]
else :
    dir_num +=1
    x += dx[dir_num]
    y+= dy[dir_num]

print(x,y)