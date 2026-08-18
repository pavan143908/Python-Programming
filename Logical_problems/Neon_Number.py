'''
A Neon number is a number where the sum of digits of its square is equal to the number itself.

Examples

0,1,9
 '''

n=int(input('num:'))
num=n**2
result=0
while num>0:
  rem=num%10
  result+=rem
  num//=10

if result==n:
  print('Neon number')
else:
  print('not a neon number')
