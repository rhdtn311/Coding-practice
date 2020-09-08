# 백준 10799 쇠막대기 문제 초반에 맨붕왔다. 알고리즘 공부하는 법을 정리해야 할 것 같다.
stick = 0   # 총 쇠막대기의 개수
end = []
result = 0

array = list(input())

for i in array :
    if i == "(" :
        stick += 1 
        result += 1
        end = "open"
    
    else : 
        if end == "open" :
            stick -= 1
            result -= 1
            result += stick

        else : 
            stick -= 1
        
        end = "close"

print(result)