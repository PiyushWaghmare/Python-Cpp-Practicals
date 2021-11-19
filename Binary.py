n=int(input('Enter no of students'))
s=[]
for in range(n):
    r=int(input('Enter numbers'))
    s.append(r)

def binary(arr,x):
    low=0
    high=len(arr-1)
    mid=0
    
    while low<=high:
        mid=(high+low)//2
        if arr[mid]<x:
            low = mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
    return-1
keyf=int(input('Enter element to  be found'))
index=binary(s,keyf)
print('Element is found at',index)
