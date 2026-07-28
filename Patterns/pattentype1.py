# n=5
# for i in range(n):
#   val=ord('A')
#   for j in range(n):
#     print(chr(val),end=' ')
#     val+=1
#   print()

# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E 
# A B C D E

# row=int(input('row:'))
# col=int(input('col:'))
# for i in range(row):
#   val=1
#   for j in range(col):
#     if j%2==0:
#       print(val,end=' ')
#       val+=1
#     else:
#       print('*',end=' ')
#   print()
# row:5
# col:5
# 1 * 2 * 3 
# 1 * 2 * 3 
# 1 * 2 * 3 
# 1 * 2 * 3 
# 1 * 2 * 3

# row=int(input('row:'))
# col=int(input('col:'))
# val=1
# p=True
# for i in range(row):
#   for j in range(col):
#     if p:
#       print(val,end=' ')
#       val+=1
#       if val>9:val=1
#       p=False
#     else:
#       print('*',end=' ')
#       p=True
#   print()

# row:5
# col:5
# 1 * 2 * 3 
# * 4 * 5 * 
# 6 * 7 * 8 
# * 9 * 1 * 
# 2 * 3 * 4 

n=4
for i in range(n):
  for j in range(n):
    if i<=j:
      print("*",end=' ')
    else:
      print(' ',end=' ')
  print()
