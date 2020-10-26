n = int(input())

array = [] 
array2 = []
array3 = []

for _ in range(n) : 
    array.append(input().split())

min_index = 0
for i in range(1,n) : 
    if array[min_index][0] > array[i][0] :
        min_index = i

for j in range(n) : 
    array2.append(int(array[j][2]))

for k in range(n) : 
    array3.append(int(array[k][3]))

array2.sort()
array3.sort()

for l in range(n) :
    for l2 in range(n) :
        if array2[l] == int(array[l2][2]) : 
            array[l2][2] = l+1

for m in range(n) :
    for m2 in range(n) :
        if array3[m] == int(array[m2][3]) : 
            array[m2][3] = m+1
print(array)