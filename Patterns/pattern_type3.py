n=4
space=n-1
star=1
for i in range(n):
  for j in range(space):
    print(' ',end=' ')
  for k in range(star):
    print('*',end=' ')
  print()
  space-=1
  star+=2

#       * 
#     * * * 
#   * * * * * 
# * * * * * * *
print('------------------------------------')
n=4
for i in range(n):
  for j in range(n-1-i):
    print(' ',end=' ')
  for k in range(2*i+1):
    print('*',end=' ')
  print()

#       * 
#     * * * 
#   * * * * * 
# * * * * * * *

print('------------------------------------')

n=4
for i in range(n):
  print('  '*(n-i-1)+'* '*(2*i+1))
  print()

#       * 
#     * * * 
#   * * * * * 
# * * * * * * *

print('------------------------------------')

n=4
val=1
for i in range(n):
  print('  '*(n-1-i)+(str(val)+' ')*(2*i+1))
  val+=1

#       1 
#     2 2 2 
#   3 3 3 3 3 
# 4 4 4 4 4 4 4

print('------------------------------------')

n=4
val=1
for i in range(n):
  for j in range(n-1-i):
    print(' ',end=' ')
  for k in range(2*i+1):
    print(val,end=' ')
  print()
  val+=1

#       1 
#     2 2 2 
#   3 3 3 3 3 
# 4 4 4 4 4 4 4
print('------------------------------------')

n=4
for i in range(n):
  val=1
  for j in range(n-1-i):
    print(' ',end=' ')
  for k in range(2*i+1):
    print(val,end=' ')
    val+=1
  print()

#       1 
#     1 2 3 
#   1 2 3 4 5 
# 1 2 3 4 5 6 7 
print('------------------------------------')

n=4
val=n
for i in range(n):
  for j in range(n-1-i):
    print(' ',end=' ')
  for k in range(2*i+1):
    print(val,end=' ')
  print()
  val-=1

#       4 
#     3 3 3 
#   2 2 2 2 2 
# 1 1 1 1 1 1 1
print('------------------------------------')


n=4
for i in range(n):
  val=n
  for j in range(n-1-i):
    print(' ',end=' ')
  for k in range(2*i+1):
    print(val,end=' ')
    val-=1
    if val<0:val=n
  print()

#       4 
#     4 3 2 
#   4 3 2 1 0 
# 4 3 2 1 0 4 3
print('------------------------------------')


n=4
val=ord('A')
for i in range(n):
  for j in range(n-1-i):
    print(' ',end=' ')
  for k in range(2*i+1):
    print(chr(val),end=' ')
    if val<0:val=n
  print()
  val+=1

#       A 
#     B B B 
#   C C C C C 
# D D D D D D D

print('------------------------------------')

n=4
val=ord('A')+n-1
for i in range(n):
  for j in range(n-1-i):
    print(' ',end=' ')
  for k in range(2*i+1):
    print(chr(val),end=' ')
    if val<0:val=n
  print()
  val-=1

#       D 
#     C C C 
#   B B B B B 
# A A A A A A A

print('------------------------------------')

n=4
val=1
for i in range(n):
  for j in range(n-1-i):
    print(' ',end=' ')
  for k in range(2*i+1):
    print(val,end=' ')
    val+=1
    if val>9:val=1
  print()

#       1 
#     2 3 4 
#   5 6 7 8 9 
# 1 2 3 4 5 6 7
print('------------------------------------')

n=4
val=ord('A')
for i in range(n):
  for j in range(n-i-1):
    print(' ',end=' ')
  for k in range(2*i+1):
    print(chr(val),end=' ')
    val+=1
  print()

#       A 
#     B C D 
#   E F G H I 
# J K L M N O P

print('------------------------------------')

n=4
val=1
p=True
for i in range(n):
  for j in range(n-i-1):
    print(' ',end=' ')
  for k in range(2*i+1):
    if p:
      print(val,end=' ')
      val+=1
      p=False
    else:
      print('*',end=' ')
      p=True
  print()

#       1 
#     * 2 * 
#   3 * 4 * 5 
# * 6 * 7 * 8 *

print('------------------------------------')

n=4
val=1
for i in range(n):
  for j in range(n-i-1):
    print(' ',end=' ')
  for k in range(2*i+1):
    if i%2==0:
      print(val,end=' ')
    else:
      print('*',end=' ')
  print()
  if i%2==0:val+=1

#       1 
#     * * * 
#   2 2 2 2 2 
# * * * * * * * 

print('------------------------------------')
