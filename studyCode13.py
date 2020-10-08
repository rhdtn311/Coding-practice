#코드업 1093번 문제

a = int(input())
b = map(int,input().split())

array = [0] * a
n = 1

for i in b :
    array[a-n] = i
    n = n+1
    
for j in array : 
    print(j, end= " ")


