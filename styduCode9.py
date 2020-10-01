# 코드업 1261번 문제

import sys

array = list(map(int,sys.stdin.readline().split()))
count = 0 

for i in array :
    if i % 5 == 0 :
        print(i)
        count += 1 
        break
    
if count == 0 :
    print(0)