n=int(input('enter:'))
while len(str(n))>1:#alternative n//10!=0  alternative  n>9
  res=0
  while n>0:
    res+=n%10
    n//=10
  n=res
if res==1:
  print('magic no')
else:
  print('not a magic no')
