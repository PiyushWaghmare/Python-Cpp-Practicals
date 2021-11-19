roll=[]
n=int(input('Enter no of students'))
for in range(n):
    a=int(input('ENter roll nos of student'))
    roll.append(a)
def sential(roll,n,x):
    end=roll[n-1]
    roll[n-1]=x
    i=0
    while(roll[i] != x):
        i+=1
    roll[n-1]=end
    if((i<n-1) or (roll[n-1]==x)):
        print(x,'Not found at',i)
    else:
        print('Not found')

n=len(roll)
x=5
sential(roll,n,x)
