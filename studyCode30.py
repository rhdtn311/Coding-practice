# 코드업 4021 홀수의 합 구하기 문제 

array = map(int,input().split())
result = []


for i in array : 
    if i % 2 == 1 :
        result.append(i)

if bool(result) == True : 
    print(sum(result))
else : 
    print(-1)