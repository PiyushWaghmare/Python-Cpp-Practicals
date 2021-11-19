list=[]
size=int(input('Enter length of the list :: '))
for i in range(size):
    val=int(input('Enter no. '))
    list.append(val)
freq=int(input('Enter no. whose freq is to be displayed '))
count=0
for i in range(size):
    if(list[i]==freq):
        count=count+1
print('Frequency=',count)