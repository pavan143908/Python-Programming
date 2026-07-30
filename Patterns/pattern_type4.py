n=4
star=n*2-1
space=0
for i in range(n):
  for j in range(space):
    print(' ',end=' ')
  for k in range(star):
    print('*',end=' ')
  print()
  space+=1
  star-=2
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 
print('-------------------------------------')

n=4
val=1
for i in range(n):
  print('  '*(i)+('* ')*(2*(n-i)-1))

  
# * * * * * * * 
#   * * * * * 
#     * * * 
#       * 
print('-------------------------------------')


n=4
val=1
for i in range(n):
  for j in range(i):
    print(' ',end=' ')
  for k in range(2*(n-i)-1):
    if val==n:val=1
    print(val,end=' ')
  print()
  val+=1

# 1 1 1 1 1 1 1 
#   2 2 2 2 2 
#     3 3 3 
#       1 
print('-------------------------------------')

n=4
for i in range(n):
  val=1
  for j in range(i):
    print(' ',end=' ')
  for k in range(2*(n-i)-1):
    print(val,end=' ')
    val+=1
  print()

# 1 2 3 4 5 6 7 
#   1 2 3 4 5 
#     1 2 3 
#       1
print('-------------------------------------')

n=4
val=ord('A')+n-1
for i in range(n):
  for j in range(i):
    print(' ',end=' ')
  for k in range(2*(n-i)-1):
    print(chr(val),end=' ')
  val-=1
  print()

# D D D D D D D 
#   C C C C C 
#     B B B 
#       A
print('-------------------------------------')

n=4
val=ord('Z')
for i in range(n):
  for j in range(i):
    print(' ',end=' ')
  for k in range(2*(n-i)-1):
    print(chr(val),end=' ')
    val-=1
  print()

# Z Y X W V U T 
#   S R Q P O 
#     N M L 
#       K
print('-------------------------------------')

n=4
val=1
for i in range(n):
  character=ord('A')
  print('  '*(n-i-1),end='')
  for k in range(2*i+1):
    if i%2==0:
      print(val,end=' ')
    else:
      print(chr(character),end=' ')
      character+=1
  print()
  if i%2==0:val+=1

#       1 
#     A B C 
#   2 2 2 2 2 
# A B C D E F G
print('-------------------------------------')

n=4
val=ord('A')
for i in range(n):
  for j in range(i):
    print(' ',end=' ')
  for k in range(2*(n-i)-1):
    print(chr(val),end=' ')
  val+=1
  print()

# A A A A A A A 
#   B B B B B 
#     C C C 
#       D 
print('-------------------------------------')


n=4
for i in range(n):
  val=ord('A')
  for j in range(i):
    print(' ',end=' ')
  for k in range(2*(n-i)-1):
    print(chr(val),end=' ')
    val+=1
  print()

# A B C D E F G 
#   A B C D E 
#     A B C 
#       A 
print('-------------------------------------')

n=4
val=1
p=True
for i in range(n):
  for j in range(i):
    print(' ',end=' ')
  for k in range(2*(n-i)-1):
    if p:
      print(val,end=' ')
      val+=1
      p=False
    else:
      print('*',end=' ')
      p=True
  print()

# 1 * 2 * 3 * 4 
#   * 5 * 6 * 
#     7 * 8 
#       *