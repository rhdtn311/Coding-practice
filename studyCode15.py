# 코드업 2007 오름차순 ? 내림차순! 1 문제

n = int(input())
array = [] 
array = list(map(int,input().split()))
count = 0 
for i in range(1,n) : 
    if array[i-1] < array[i] :
        count += 1
    elif array[i-1] > array[i] :
        count -= 1

if count == n-1 : 
    print("오름차순")
elif count == -(n-1) :
    print("내림차순")
else : 
    print("섞임")