'''An Armstrong number (also known as a narcissistic number 
or pluperfect digital invariant) 
is a non-negative integer that is equal to the sum of its own digits,
each raised to the power of the total number of digits.'''

n=int(input('num:'))
temp=n
p=len(str(n))
res=0
while n>0:
  rem=n%10
  res+=rem**p
  n//=10
if temp==res:
  print('armstrong')
else:
  print('not armstrong')

