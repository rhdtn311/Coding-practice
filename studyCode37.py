# 백준 9012번 괄호 문제 (자료구조, 문자열, 스택)

n = int(input())
array = []
result = []

for i in range(n) :
    count = 0 
    array = list(input())
    for j in array :
        if j == "(" : 
            count += 1
        elif j == ")" :
            count -= 1 
        if count < 0 : 
            result.append("NO")
            break
    if count >= 0 :
        if count == 0 :
            result.append("YES")
        else :
            result.append("NO")

for j in result : 
    print(j)
    
