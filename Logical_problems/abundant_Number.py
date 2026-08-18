'''An abundant number (or excessive number) is a positive integer 
for which the sum of its proper divisors (all positive divisors excluding the number itself) 
is greater than the number itself.'''

n=int(input('num:'))
sum=0
for i in range(1,(n//2)+1):
  if n%i==0:
    sum+=i
if sum>n:
  print('Abundant no')
else:
  print('not a abundant no')
