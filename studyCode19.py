# 코드업 문제 2623 최대공약수 구하기

a,b = map(int,input().split())
result = 0
problem = 0

if a < b :
    for i in range(1,a+1) : 
        if a % i == 0 and b % i == 0 : 
            result = i
        else : continue
elif a>b :
    for j in range(1,b+1) : 
        if a % j == 0 and b % j == 0 : 
            result = j
        else : continue

print(result)