# 백준 2912 백설공주와 난장이 문제

array = []
for i in range(7) : 
    array.append(int(input()))

array.sort(reverse = True)

for i in range(2) : 
    print(array[i])