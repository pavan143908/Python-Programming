'''
row=int(input("row:"))
col=int(input("col:"))
print("enter first matrix")
matrix1=[[int(input()) for i in range(col)] for row in range(row)]
print(matrix1)

print("enter second matrix")
matrix2=[[int(input()) for i in range(col)] for row in range(row)]
print(matrix2)



result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix1)):
  for j in range(len(matrix2[0])):
    for k in range(len(matrix2)):
      result[i][j]+=matrix1[i][k]*matrix2[k][j]


print("result")

for i in result:
  for j in i:
    print(j,end=' ')
  print()

'''
'''
row:3
col:3
enter first matrix
1
2
3
4
2
1
5
7
6
[[1, 2, 3], [4, 2, 1], [5, 7, 6]]
enter second matrix
2
3
1
4
5
4
7
2
2
[[2, 3, 1], [4, 5, 4], [7, 2, 2]]
result
31 19 15 
23 24 14 
80 62 45 '
-------------------------------------------------------------------------

'''

'''

-----------------------------------------------------------------------


l1=[1,2,3,1,4,5,1,3,4,1,4,5,1,1,5,6,1,4,5,1,4,6,6]
l2=[1,4,5]
cnt=0
for i in range(len(l1)-2):
  if [l1[i],l1[i+1],l1[i+2]]==l2:
    cnt+=1
print('count of sub list is:',cnt)


count of sub list is: 3

'''

l1=[1,2,3,1,4,5,1,3,4,1,4,5,1,1,5,6,1,4,5,1,4,6,6]
l2=[1,4,5]
cnt=0
for i in range(len(l1)):
  if l1[i:i+len(l2)]==l2:
    cnt+=1
print('count of sub list is:',cnt)

# count of sub list is: 3