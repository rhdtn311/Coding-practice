# 코드업 4072번 폭염 문제

n = int(input())
array = list(map(float,input().split()))

print(max(array))

if max(array) >= 33 and max(array) < 35 : 
    print("yellow")
elif max(array) >= 35 : 
    print("red")
else : 
    print("green")