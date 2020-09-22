# 코드업 1096번 문제

a = int(input())
array = [[0 for row in range(19)] for col in range(19) ]


for num in range(a) :
    x,y = map(int,input().split())
    array[x-1][y-1] = 1

for i in array :
    for j in i :
        print(j,end = " ")
    print()
