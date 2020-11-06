# 우테코 7번문제 
string = list(input()) # 암호를 입력받음

def remove(string) :    
    array = []  # 중복되는 인덱스를 저장하는 리스트
    for i in range(1,len(string)) :
        temp=i-1    #중복을 검사하는 인덱스 값을 temp에 저장 
        if string[temp] == string[i] :  # 값이 중복된다면
            if temp not in array :  # + 리스트에 인덱스가 없다면 추가
                array.append(temp) 
            if i not in array :
                array.append(i)            
            else : 
                continue
    
    if len(array) == 0 :    # 재귀함수의 탈출 조건 : 모든 string에 중복 값이 존재하지 않는다면
        return string   # return

    array.sort(reverse=True)    # 뒤의 인덱스부터 삭제해야 out of range 에러를 피할 수 있음
    for j in array : 
        del string[j]
    
    for k in string :   # 중복을 제거한 값을 출력
        print(k,end="")
    print() 
    remove(string)  # 중복값을 제거한 입력값이 매게변수로 함수 선언 
    return string   

remove(string)