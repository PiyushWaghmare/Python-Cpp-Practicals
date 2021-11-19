list=[]
n=int(input('Enter total no. of students'))
for i in range(0,n):
 a=int(input('Enter roll no.'))
list.append(a)
print(list)
b=int(input('No. to be searched is '))
for i in range(n):
 if (b==list[i]):
   print('No. is at position ',i)
