# 코드업  1098번 문제. 


h,w = map(int,input().split())
n = int(input())

array = [[0 for row in range(w)] for col in range(h)]

for i in range(n) :
    l,d,x,y = map(int,input().split())
    if d == 0 :
        for num1 in range(l) :
            if array[x-1][y-1+num1] == 0 :
                array[x-1][y-1+num1] = 1
            else :
                array[x-1][y-1+num1] == 0    

    elif d == 1 :
        for num1 in range(l) :
            if array[x-1+num1][y-1] == 0 :
                array[x-1+num1][y-1] = 1
            else :
                array[x-1+num1][y-1] = 0

for row in array :
    for col in row : 
        print(col, end=" ")
    print()