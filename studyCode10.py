# 코드업 1271번 기부 문제

import sys
k,h = map(int,input().split())

if k % 2 == 0 : 
    a = k//2
    k_result = a*10
elif k % 2 == 1 :
    k_result = k//2 + 1

if h % 2 == 0 : 
    a = h//2
    h_result = a*10
elif h % 2 == 1 :
    h_result = h//2 + 1

print(k_result+h_result)
