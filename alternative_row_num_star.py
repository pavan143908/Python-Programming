n=5
for i in range(1,n-1):
  for j in range(n):
    print(i,end=' ')
  print()
  if i!=3:
    for k in range(n):
      print('*',end=' ')
    print()


# 1 1 1 1 1 
# * * * * * 
# 2 2 2 2 2 
# * * * * * 
# 3 3 3 3 3