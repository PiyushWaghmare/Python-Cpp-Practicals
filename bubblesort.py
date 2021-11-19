list=[]
n=int(input('Enter elements of the list'))
for i in range(n):
    a=int(input('Enter values'))
    list.append(a)
for i in range(len(list)-1):
    if list[i]>list[i+1]:
        list[i],list[i+1]=list[i+1],list[i]
    else:
        pass
    for j in range(i):
        if list[j]>list[i+1]:
            list[j],list[j+1]=list[j+1]+list[j]
            print({list})
        
