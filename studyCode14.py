# 코드업 1092번 문제

a,b,c = map(int,input().split())
n = 0

while True : 
    n+=1
    if n%a == 0 and n%b ==0  and n%c ==0 :
        print(n)
        break
    else :
        continue   
