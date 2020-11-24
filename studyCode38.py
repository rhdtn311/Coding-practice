# 백준 2884번 알람 시계문제 

h,m = map(int,input().split())

m -= 45 
if m<0 : 
    if h > 0 : 
        h -= 1 
        m += 60
    else : 
        h = 23
        m += 60
print(h,m)