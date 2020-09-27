a = int(input())
b = map(int,input().split())

c= []

for j in b :
    c.append(j)

for i in range(1,a) :
    if c[0] > c[i] : 
        c[0] = c[i]
    else :
        c[0] = c[0]

print(c[0])
