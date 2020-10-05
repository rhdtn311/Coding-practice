money = int(input())
first_money = money
day = int(input())
array=[]
array = list((map(int,input().split())))

for i in range(len(array)) :
    array[i] = array[i] * 0.01

for j in array : 
    money = money+(money*j)

result = round(money-first_money,0)
print(int(result))

if int(result) > first_money : 
    print("good")
elif int(result) == first_money :
    print("same")
elif int(result) < 0 : 
    print("bad")

