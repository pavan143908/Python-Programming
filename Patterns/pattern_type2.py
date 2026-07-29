n=5
for i in range(n):
  for j in range(n):
    print(i+j,end=' ')
  print()

# 0 1 2 3 4 
# 1 2 3 4 5 
# 2 3 4 5 6 
# 3 4 5 6 7 
# 4 5 6 7 8
print('<----------------------------------------------->')

for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      print('*',end=' ')
    else:
      print('',end=' ')
  print()

# * * * * 
# * * *  
# * *   
# * 
print('<----------------------------------------------->')


for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print('*',end=' ')
    else:
      print(' ',end=' ')
  print()

#       * 
#     * * 
#   * * * 
# * * * * 
print('<----------------------------------------------->')

n=5
for i in range(n):
  for j in range(n):
    if i+j==n-1:
      print(i+j,end=' ')
    else:
      print(' ',end=' ')
  print()


#         4 
#       4   
#     4     
#   4       
# 4         
print('<----------------------------------------------->')


n=5
val=1
for i in range(n):
  for j in range(n):
    if i+j==n-1:
      print(val,end=' ')
      val+=1
    else:
      print(' ',end=' ')
  print()


#         1 
#       2   
#     3     
#   4       
# 5        

print('<----------------------------------------------->')

n=5
val=ord('A')
for i in range(n):
  for j in range(n):
    if i+j==n-1:
      print(chr(val),end=' ')
      val+=1
    else:
      print(' ',end=' ')
  print()

#         A 
#       B   
#     C     
#   D       
# E    
print('<----------------------------------------------->')

n=4

val=n
for i in range(n):
  for j in range(n):
    if i+j==n-1:
      print(val,end=' ')
      val-=1
    else:
      print(' ',end=' ')
  print()

#       4 
#     3   
#   2     
# 1  
print('<----------------------------------------------->')


n=4
val=ord('Z')
for i in range(n):
  for j in range(n):
    if i+j==n-1:
      print(chr(val),end=' ')
      val-=1
    else:
      print(' ',end=' ')
  print()

#       Z 
#     Y   
#   X     
# W       
print('<----------------------------------------------->')
n=4
val=ord('A')+n-1
for i in range(n):
  for j in range(n):
    if i+j==n-1:
      print(chr(val),end=' ')
      val-=1
    else:
      print(' ',end=' ')
  print()


#       D 
#     C   
#   B     
# A   
print('<----------------------------------------------->')

n=4
val=1
p=True
for i in range(n):
  for j in range(n):
    if i+j==n-1:
      if p:
        print(val,end=' ')
        val+=1
        p=False
      else:
        print('*',end=' ')
        p=True
    else:
      print(' ',end=' ')
  print()

#       1
#     *
#   2
# *       
print('<----------------------------------------------->')

n=4
val=ord('A')
for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=' ')
    else:
      print(' ',end=' ')
  val+=1
  print()


#      A 
#     B B 
#   C C C 
# D D D D
print('<----------------------------------------------->')


n=4
for i in range(n):
  val=ord('A')
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=' ')
      val+=1
    else:
      print(' ',end=' ')
  print()

#       A 
#     A B 
#   A B C 
# A B C D
print('<----------------------------------------------->')

n=4
val=ord('A')+n-1
for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=' ')
    else:
      print(' ',end=' ')
  val-=1
  print()

#       D 
#     C C 
#   B B B 
# A A A A 
print('<----------------------------------------------->')

for i in range(n):
  val=ord('A')+n-1
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=' ')
      val-=1
    else:
      print(' ',end=' ')
  print()

#       D 
#     D C 
#   D C B 
# D C B A 
print('<----------------------------------------------->')

for i in range(n):
  val=ord('Z')
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=' ')
      val-=1
    else:
      print(' ',end=' ')
  print()

#       Z 
#     Z Y 
#   Z Y X 
# Z Y X W 
print('<----------------------------------------------->')

val=ord('Z')
for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print(chr(val),end=' ')
    else:
      print(' ',end=' ')
  val-=1
  print()

#       Z 
#     Y Y 
#   X X X 
# W W W W 
print('<----------------------------------------------->')

val=1
for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print(val,end=' ')
    else:
      print(' ',end=' ')
  val+=1
  print()

#       1 
#     2 2 
#   3 3 3 
# 4 4 4 4
print('<----------------------------------------------->')

for i in range(n):
  val=1
  for j in range(n):
    if i+j>=n-1:
      print(val,end=' ')
      val+=1
    else:
      print(' ',end=' ')
  print()

#       1 
#     1 2 
#   1 2 3 
# 1 2 3 4
print('<----------------------------------------------->')

val=n
for i in range(n):
  for j in range(n):
    if i+j>=n-1:
      print(val,end=' ')
    else:
      print(' ',end=' ')
  val-=1
  print()

#       4 
#     3 3 
#   2 2 2 
# 1 1 1 1
print('<----------------------------------------------->')

for i in range(n):
  val=n
  for j in range(n):
    if i+j>=n-1:
      print(val,end=' ')
      val-=1
    else:
      print(' ',end=' ')
  print()

#       4 
#     4 3 
#   4 3 2 
# 4 3 2 1
print('<----------------------------------------------->')


val=1
for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      print(val,end=' ')
    else:
      print(' ',end=' ')
  val+=1
  print()

# 1 1 1 1 
# 2 2 2   
# 3 3     
# 4       
print('<----------------------------------------------->')

for i in range(n):
  val=1
  for j in range(n):
    if i+j<=n-1:
      print(val,end=' ')
      val+=1
    else:
      print(' ',end=' ')
  print()

# 1 2 3 4 
# 1 2 3   
# 1 2     
# 1  
print('<----------------------------------------------->')

for i in range(n):
  val=n
  for j in range(n):
    if i+j<=n-1:
      print(val,end=' ')
      val-=1
    else:
      print(' ',end=' ')
  print()

# 4 3 2 1 
# 4 3 2   
# 4 3     
# 4  
print('<----------------------------------------------->')

for i in range(n):
  val=ord('A')
  for j in range(n):
    if i+j<=n-1:
      print(chr(val),end=' ')
      val+=1
    else:
      print(' ',end=' ')
  print()

# A B C D 
# A B C   
# A B     
# A  
print('<----------------------------------------------->')
val=ord('A')
for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      print(chr(val),end=' ')
    else:
      print(' ',end=' ')
  print()
  val+=1

# A A A A 
# B B B   
# C C     
# D  
print('<----------------------------------------------->')

val=ord('Z')
for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      print(chr(val),end=' ')
    else:
      print(' ',end=' ')
  print()
  val-=1
# Z Z Z Z 
# Y Y Y   
# X X     
# W
print('<----------------------------------------------->')
for i in range(n):
  val=ord('Z')
  for j in range(n):
    if i+j<=n-1:
      print(chr(val),end=' ')
      val-=1
    else:
      print(' ',end=' ')
  print()

# Z Y X W 
# Z Y X   
# Z Y     
# Z
print('<----------------------------------------------->')
val=ord('A')+n-1
for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      print(chr(val),end=' ')
    else:
      print(' ',end=' ')
  val-=1
  print()
# D D D D 
# C C C   
# B B     
# A 
print('<----------------------------------------------->')

for i in range(n):
  val=ord('A')+n-1
  for j in range(n):
    if i+j<=n-1:
      print(chr(val),end=' ')
      val-=1
    else:
      print(' ',end=' ')
  print()

# D C B A 
# D C B   
# D C     
# D
print('<----------------------------------------------->')
val=1
p=True
for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      if p:
        print(val,end=' ')
        val+=1
        p=False
      else:
        print('*',end=' ')
        p=True
    else:
      print(' ',end=' ')
  print()

# 1 * 2 * 
# 3 * 4   
# * 5     
# *  
print('<----------------------------------------------->')

val=ord('A')
for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      print(chr(val),end=' ')
      val+=1
    else:
      print(' ',end=' ')
  print()

# A B C D 
# E F G   
# H I     
# J 
print('<----------------------------------------------->')
val=ord('A')
for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      print(chr(val),end=' ')
      val+=1
    else:
      print(' ',end=' ')
  print()

# A B C D 
# E F G   
# H I     
# J
print('<----------------------------------------------->')
