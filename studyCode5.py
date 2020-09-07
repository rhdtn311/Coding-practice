# 코드업 1099번 문제

array = []

for i in range(10) :
    i = list(map(int,input().split()))
    array.append(i)
x, y = 1,1

while True : 
    if array[x][y] == 2 :
        array[x][y] = 9 
        break
    if array[x+1][y] == 1 and array[x][y+1] == 1 :
        array[x][y] = 9
        break
        
    elif array[x][y+1] == 0 or array[x][y+1] == 2 :
        array[x][y] = 9
        y += 1
    
    elif array[x][y+1] == 1 :
        array[x][y] = 9
        x += 1
        if array[x][y] == 2 :
            array[x][y] = 9
            break
    if array[x][y] == 2 :
        array[x][y] = 9
        break
    
  
for j in array :
    for k in j :
        print(k,end = " ")
    print()