list=[]
n=int(input('Enter no of elemnts in the list'))
for i in range(n):
    a=int(input('Enter values'))
    list.append(a)
for i in range(0,len(list)):
    temp=list[i]
    n=i
    while temp<list[n-1] and n>0:
        list[n]=list[n-1]
        n=n-1
    list[n]=temp
print({list})