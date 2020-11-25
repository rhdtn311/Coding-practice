# 백준 4153번 직각삼각형 문제

array = []
result = []
while True :
    a,b,c = map(int,input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    else : 
        array.append([a,b,c])

for a in array : 
    a.sort()

for i,j,k in array :
    if k*k == (i*i) + (j*j) :
        print("right")
    else : 
        print("wrong")