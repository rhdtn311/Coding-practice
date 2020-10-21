#코드업 1090번 문제

a,r,n = map(int,input().split())
count = 1

while count <= n-1 : 
    a= a*r
    count+=1

print(a)