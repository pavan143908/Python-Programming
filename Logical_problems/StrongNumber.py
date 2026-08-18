'''A Strong Number (also known as a Krishnamurthy Number or Peterson Number)
 is a special number in mathematics where the sum of the factorials of 
 its individual digits equals the number itself.
 Example: 145
 All Strong Numbers: There are only four known Strong Numbers in base 10: 1, 2, 145, and 40585.
 '''

n=int(input('num:'))
temp=n
res=0
while n>0:
  rem=n%10
  fact=1
  for i in range(1,rem+1):
    fact*=i
  res+=fact
  n//=10
if temp==res:
  print('strong number')
else:
  print('not a strong number')
