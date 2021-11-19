a=[]
n=int(input('Enter elments in a'))
b=[]
m=int(input('Enter elements in b'))
for i in range(n):
    val1=int(input('Enter values'))
    a.append(val1)

for j in range(m):
    val2=int(input('Enter  value'))
    b.append(val2)

intersection = a & b
print(intersection)

