# 우테코 2019년 3번 문제

array = input() # 입력값 받기
word = []   # 입력값을 리스트로 변환하기 위한 리스트
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]   # 입력값을 암호로 치환하기 위한 알파벳 리스트 초기화
k=0
n=str()
original = str()    # 대소문자 구분 하기 위한 초기 알파벳 값 

for i in array : 
    word.append(i)

for i in word : 
    if ord(i) == 32 :   # 공백(띄어쓰기)의  아스키 코드인 32를 만족한다면 띄어쓰기하라.
        print("",end=" ")
        continue
    original = i    # 초기 값
    if i.islower() == True :    # alpha 리스트를 대문자로 초기화 했기 때문에 입력값을 모두 대문자로 변경
        i=i.upper()
    for j in range(len(alpha)-1) :  
        if alpha[j] == i :  # 입력 값이 alpha리스트의 몇 번 인덱스인지 확인
            k = -j  # 변수 k에 i 인덱스 부호를 바꿔주고 저장
            n= alpha[k-1]   # 암호는 기존 입력 값의 부호를 바꾸고 -1한 인덱스 값과 같다.
    if original.isupper() == True : # 기존 입력값이 대문자였다면
        n=n.upper() # 대문자로 출력
        print(n,end="")
    else : # 기존 입력 값이 소문자였다면
        n=n.lower() # 소문자로 출력
        print(n,end="")




