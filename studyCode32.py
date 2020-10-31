# 코드업 4011 : 생년월일 출력 문제

number = input()

if int(number[7]) == 1 :
    print("19"+number[0:2]+"/"+number[2:4]+"/"+number[4:6]+" "+"M")
elif int(number[7]) == 2 : 
    print("19"+number[0:2]+"/"+number[2:4]+"/"+number[4:6]+" "+"F")
elif int(number[7]) == 3 : 
    print("20"+number[0:2]+"/"+number[2:4]+"/"+number[4:6]+" "+"M")
elif int(number[7]) == 4 :
    print("20"+number[0:2]+"/"+number[2:4]+"/"+number[4:6]+" "+"F")