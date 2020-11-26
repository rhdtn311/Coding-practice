# 백준 19941번 한국정보올림피아드 KOI 2020 1차대회 고등부 2번 문제 햄버거 분배
n,k = map(int,input().split())
array = list(input())  # 햄버거들
count = 0

for i in range(len(array)) : 
    if array[i] == "P" :  # 사람이 나왔을 경우에만 수행
        check = 0
        for j in range(k,0,-1) :  # 우선 뒤로 가는 경우 먼저 해야 최대값을 구할 수 있다.
            if i-j >= 0 :
                if array[i-j] == "H" :  
                    array[i-j] = 0 
                    check = 1  # 만약 햄버거를 먹었다면 check를 1로 바꿔서 앞으로 가는 경우를 수행하지 않게 한다.
                    break
            continue  # 앞으로 가는 for문 먼저 수행
            
        if check == 0 :  # 앞쪽 위치에 있는 햄버거를 먹지 못했다면 
            for l in range(1,k+1) : # 뒤에있는 햄버거를 먹기 위에 찾음
                if i+l < len(array) : 
                    if array[i+l] == "H" :
                        array[i+l] = 0  # 햄버거를 먹었다면 H를 0으로 수정
                        break
                continue

for k in array : 
    if k == 0 : 
        count += 1 

print(count)