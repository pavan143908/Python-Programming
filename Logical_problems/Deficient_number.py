'''
In number theory, a deficient number (or defective number) is a positive integer n
for which the sum of its proper divisors is strictly less than the
number itself.In other words, if you add up all positive factors of n excluding n, 
the total is less than n.

numbers: 8
'''

n=int(input('num:'))
sum=0
for i in range(1,(n//2)+1):
  if n%i==0:
    sum+=i
if sum<n:
  print('Deficient no')
else:
  print('not a Deficient no')
