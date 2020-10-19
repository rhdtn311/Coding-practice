# 코드업 2621 약수의 합 문제

n = int(input())
array = []
sum = 0 
i = 1

while i <= n : 
    if n % i == 0 : 
        array.append(n//i)
    i+=1

for j in array : 
    sum += j 

print(sum)