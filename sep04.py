
''''
wap to count the total number of elements in the given list of lists
l1=[[1,3],[4,5,6],[7,8,9,34],[],[1],[2,3]]
cnt=0
for i in l1:
  for j in i:
    cnt+=1 

print(cnt)

# 12

--------------------------------------------------------
'''
'''

#max element in each list
l1=[[1,3],[4,5,6],[7,8,9,34],[2,67],[1,10],[2,3]]


for i in l1:
  print(max(i),end=' ')

3 6 34 67 10 3 
--------------------------------------------------------
'''
'''
wap to find the max element in each list without using max function

l1=[[1,3],[4,5,6],[7,8,9,34],[2,67],[1,10],[2,3]]
for i in l1:
  if len(i)==0:
    continue
  max_val=i[0]
  for j in i:
    if j>max_val:
      max_val=j
  print(max_val)


3
6
34
67
10
3
----------------------------------------------------------
'''

'''
wap to find the
sum of given column n=3
l1= [
  [1,2,3,4,5],
  [2,7,1,9,8],
  [3,6,4,5,6],
  [3,3,4,5,7]
]
n=3
sum=0
for i in l1:
  if 0<n<=len(i):
    sum+=i[n-1]

print(sum)


# output:
12
----------------------------------------------------------------------------
wap to build index grid system based on row and column using user input
'''

'''

row=int(input("row:"))
col=int(input("col:"))
outer=[]
for i in range(row):
  inner=[]
  for j in range(col):
    inner+=[(i,j)]
  outer+=[inner]
print(outer)


print('[')
for i in outer:
  print(' ',i)
print(']')

[[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(3, 0), (3, 1), (3, 2)]]
[
  [(0, 0), (0, 1), (0, 2)]
  [(1, 0), (1, 1), (1, 2)]
  [(2, 0), (2, 1), (2, 2)]
  [(3, 0), (3, 1), (3, 2)]
]

alternative
row=int(input("row:"))
col=int(input("col:"))
print([[(i,j) for j in range(col)] for i in range(row)])

------------------------------------------------------------------------------
# wap to accept the values from user to the given matrix
#  and display it in the form of a matrix

row=int(input("row:"))
col=int(input("col:"))

matrix =[[int(input()) for j in range(col)] for i in range(row)]

print("matrix")
for i in matrix:
  for j in i:
    print(j,end=' ')
  print()
--------------------------------------------------------------


'''
print("enter first matrix")
matrix1=[[int(input()) for col in range(3)] for row in range(3)]
print(matrix1)

print("enter second matrix")
matrix2=[[int(input()) for col in range(3)] for row in range(3)]
print(matrix2)


result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(matrix1)):
  for j in range(len(matrix2)):
    result[i][j]=matrix1[i][j]+matrix2[i][j]

print(result)