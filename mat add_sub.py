row=int(input('Enter the row no.'))
col=int(input('Enter column no.'))
matrix1=[[int(input()) for i in range(col)]for j in range(row)]
print('Enter the elements for matrix1')
print('matrix1:')
for i in range (row):
    for j in range(col):
        print(format(matrix1[i][j],'<3'),end='')
    print()

matrix2=[[int(input()) for i in range(col)]for j in range(row)]
print('Enter the elements for matrix1')
print('matrix2:')
for i in range (row):
    for j in range(col):
        print(format(matrix2[i][j],'<3'),end='')
    print()

result=[[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range(row):
    for j in range(col):
        print(format(result[i][j],'<3',end=' '))
        print()

