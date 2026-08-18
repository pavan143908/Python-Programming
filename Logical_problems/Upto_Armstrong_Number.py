#armstrong numbers
n=int(input('num:'))
for val in range(1,n+1):
  p=len(str(val))
  res=0
  temp=val
  while val>0:
    res+=(val%10)**p
    val//=10
  if temp==res:
    print(temp,end=' ')

#upto n armstrong numbers
n=int(input('num:'))
cnt=0
val=1
while cnt!=n:
  p=len(str(val))
  res=0
  temp=val
  while val>0:
    res+=(val%10)**p
    val//=10
  if temp==res:
    print(temp,end=' ')
    cnt+=1
  val=temp
  val+=1