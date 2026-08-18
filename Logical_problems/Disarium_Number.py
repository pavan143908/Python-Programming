'''
A Disarium number is a number where the sum of its digits raised to the 
power of their respective 1-based positions (from left to right) 
equals the number itself.

Example 1: 89,135
 '''
n=int(input('num:'))
p=len(str(n))
temp=n
res=0
while n>0:
  res+=(n%10)**p
  n//=10
  p-=1
print(res)
if res==temp:
  print('Disarium number')
else:
  print('Not an Disarium number')
