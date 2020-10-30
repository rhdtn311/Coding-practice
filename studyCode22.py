# 코드업 2650 : 디지털 도어락 문제

n,m,k = map(int,input().split())
small = 0 
array = []
result = 0 

array.append(n)
array.append(m)
array.append(k)
array.sort()

small = array[0]

i = 1
while i <= small :
    if n % i == 0 and m % i == 0 and k % i == 0 :
        result = i 

    i+=1 

print(result)

