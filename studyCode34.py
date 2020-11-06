#우테코 작년 1번

money = int(input())
array = [0] * 9 

while money > 0 : 
    if money >= 50000 : 
        array[0] = money//50000
        money = money%50000
    elif 50000 > money >= 10000 : 
        array[1] = money//10000
        money = money%10000
    elif 10000> money >= 5000 : 
        array[2] = money //5000
        money = money%5000
    elif 5000 > money >= 1000 : 
        array[3] = money // 1000 
        money = money%1000
    elif 1000> money >= 500 : 
        array[4] = money //500
        money = money % 500
    elif 500>money >= 100 :
        array[5] = money // 100 
        money = money%100
    elif 100>money >= 50 :
        array[6] = money // 50
        money %= 50
    elif 50>money >= 10 : 
        array[7] = money //10
        money%=10
    elif 10>money>=1 : 
        array[8] = money//1
        money %= 1 

print(array)
    