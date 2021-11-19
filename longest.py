list1=['piyush','abc','df']
list2=[]
dict1={}
for str in list1:
    list2.append(len(str))
    dict1[str]=len(str)
print(max(list2))
for word,lenght in dict1.items():
    if(max(list2)):
        print(word,length)