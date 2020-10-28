# 코드업 4042 격자값 계산 문제 

array = []

for i in range(5) :
    array.append(list(map(int,input().split())))

row_array = [] 
temporary = []
col_array = []

for row in range(5) : 
    row_array.append(max(array[row]))

for col in range(5) : 
    for j in range(5) : 
        temporary.append(array[j][col])    
    col_array.append(max(temporary))
    temporary=[]

print(abs(sum(row_array)-sum(col_array)))