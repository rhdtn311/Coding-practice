# 프로그래머스 문자열 내 p와 y의 개수 문제 

def solution(s):
    answer = True

    p_count = 0
    y_count = 0

    for i in s : 
        if i == "p" or i =="P" : 
            p_count += 1 
        elif i == "y" or i== "Y" : 
            y_count += 1
    
    print(y_count,p_count)
    
    if p_count == y_count : 
        return True 
    else : 
        return False




