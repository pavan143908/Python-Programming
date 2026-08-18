n=1234
print(str(n)[::-1])

#reverse of a number without using string slicing
n=int(input('enter a number:'))
rev=0
while n>0:
  rem=n%10
  rev=rev*10+rem
  n//=10
print(rev)
