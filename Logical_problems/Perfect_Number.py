'''A perfect number is a positive integer that is equal to the sum of its proper 
positive divisors (excluding the number itself).For example, 6 is a perfect number because 
its proper divisors are 1, 2, and 3:1 + 2 + 3 = 6
 example: 6, 28, 496, 8128, 33550336
 '''


n=int(input('num:'))
res=0
for i in range(1,(n//2)+1):
  if n%i==0:
    res+=i
if n==res:
  print('perfect number')
else:
  print('not a perfect number')

