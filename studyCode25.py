# 코드업 4037 소인수 분해 문제

n = int(input())
s = 2 
array = [] 

while n>1 :
    if n % s != 0 :
        s += 1 
        continue

    if n % s == 0 :
        n /= s 
        array.append(s)
    
    s = 2 
     
for i in array : 
    print(i,end= " ")