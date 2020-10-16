# 코드업 1091번 문제

a,m,d,n = map(int,input().split())
count = 1

while count<=n-1 : 
    a = a*m+d
    count+=1
    

print(a)