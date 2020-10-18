# 코드업 3004 데이터 재정렬 문제 (시간초과)

n = int(input())
array = list(map(int,input().split()))
array_copy = []

for l in range(n) :
    array_copy.append(array[l])

array_copy.sort()
dic = dict()

for i in range(n) :
    dic[i] = array_copy[i]

for j in range(n) : 
    for k in range(n) : 
        if array[j] == dic[k] : 
            array[j] = list(dic.keys())[k]

for z in array : 
    print(z,end = " ")

