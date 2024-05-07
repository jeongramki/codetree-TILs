x,y = 0,0

n = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]


for i in range(n) : 
    direc, distance = input().split()
    distance = int(distance)
    for j in range(distance): 
        if direc == 'E': x += dx[0]; y += dy[0];
        elif direc == 'S' : x += dx[1]; y += dy[1];
        elif direc == 'W' : x += dx[2]; y += dy[2];
        else : x += dx[3]; y += dy[3];

   

print(x,y)