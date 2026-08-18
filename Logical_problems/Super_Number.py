n=int(input('enter:'))
temp=n
while n>9:#alternative n//10!=0  alternative  n>9
  res=0
  while n>0:
    res+=n%10
    n//=10
  n=res
print(f'super no of {temp} is {res}')
