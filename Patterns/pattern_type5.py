# n=4
# for i in range(n-1,-n,-1):
#   for j in range(n-abs(i)):
#     print('*',end=' ')
#   print()

# * 
# * * 
# * * * 
# * * * * 
# * * * 
# * * 
# * 

# n=4
# for i in range(n-1,-n,-1):
#   print('* '*(n-abs(i)))

# * 
# * * 
# * * * 
# * * * * 
# * * * 
# * * 
# *


# n=4
# for i in range(n-1,-n,-1):
#   print('  '*abs(i)+'* '*(n-abs(i)))

#       * 
#     * * 
#   * * * 
# * * * * 
#   * * * 
#     * * 
#       *

# n=4
# for i in range(n-1,-n,-1):
#   print(' '*abs(i)+'* '*(n-abs(i)))

n=4
val=1
p=True
for i in range(2*n-1):
  stars=n-abs(n-i-1)
  for j in range(n-stars):
    print(' ',end=' ')
  for k in range(stars):
    if p:
      print(val,end=' ')
      val+=1
      if val>9:val=1
      p=False
    else:
      print('*',end=' ')
      p=True
  print()
