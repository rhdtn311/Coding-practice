# 코드업 2602 성적표 출력하기 문제

import sys

array1 = list(map(int,sys.stdin.readline().split()))
array2 = list(map(int,sys.stdin.readline().split()))
array3 = list(map(int,sys.stdin.readline().split()))
sum1,sum2,sum3 = 0, 0, 0

for i in array1 :
    print(i,end=" ")
    sum1 += i
print(sum1)

for j in array2 : 
    print(j,end=" ")
    sum2 += j
print(sum2)

for k in array3 : 
    print(k,end= " ")
    sum3 += k
print(sum3)

for l in range(3) : 
    print(array1[l] + array2[l] + array3[l],end=" ")
print(sum1+sum2+sum3)