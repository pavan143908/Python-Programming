'''
A Harshad number (or Niven number) is an integer that is evenly divisible by the sum of its digits
in a given number base (typically base 10). 
The word "Harshad" comes from the Sanskrit harṣa (joy) + da (giver), meaning "joy-giver."

Harshad number: 18, 171, 
 '''

n=int(input('num:'))
temp=n
res=0
while n>0:
  res+=n%10
  n//=10
if temp%res==0:
  print('harshads number')
else:
  print('not harshads number')
