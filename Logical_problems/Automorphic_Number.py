'''
An automorphic number (also known as a circular number) is a number 
whose square ends with the exact same digits as the number itself.

example:5,6,25,76,376,625

 '''

n=int(input('num:'))
res=n**2
if n==res//int(str(res)[-len(str(n)):]):
  print('Automorphic number')
else:
  print('not an Automorphic number')
