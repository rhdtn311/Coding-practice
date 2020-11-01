# 코드업 4021번 : 홀수의 합 구하기 문제

array = list(map(int,input().split()))
holsu = []

for i in array : 
    if i%2 == 1 :
        holsu.append(i)

if bool(holsu) == False : 
    print(-1)
else : 
    print(sum(holsu))
