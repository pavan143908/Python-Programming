n=5
val=1
for i in range(n):
  for j in range(n):
    if ((i%2==0 and j%2==0) or (i%2!=0 and j%2!=0)):
      if val>9:val=1
      print(val,end=' ')
      val+=1
    else:
      print('*',end=' ')
  print()

# 1 * 2 * 3 
# * 4 * 5 * 
# 6 * 7 * 8 
# * 9 * 1 * 
# 2 * 3 * 4 