a=[1,2,3]
b=[2,3,4]
print(len(b))
union=[]
for i in range(len(a)):
    union.append==(a[i])
    flag=0
    for j in range(len(b)):
     if(b[j]==union[i]):
         flag=1
         break
         if (flag==0):
          union.append(b[j])
print(union)
