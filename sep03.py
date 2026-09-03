'''
# wap to display pairs of given target value

l1=[2,1,5,6,7,8,4,3,2,5,8,9,1,2,4,5]
target=6

for i in range(len(l1)):
  for j in range(i+1,len(l1)):
    if l1[i]+l1[j]==target:
      print((l1[i],l1[j]))


(2, 4)
(2, 4)
(1, 5)
(1, 5)
(1, 5)
(5, 1)
(4, 2)
(4, 2)
(2, 4)
(5, 1)
(1, 5)
(2, 4)
--------------------------------------------------------------
'''
'''
input:
l1=[1,7,2,4,6,17,19,5,8,12,45,23,18,19,21]

output:92

def is_prime(n):
  if n<=1:
    return False
  for j in range(2,int(n**0.5)+1):
    if n%j==0:
      return False
  return True

l1=[1,7,2,4,6,17,19,5,8,12,45,23,18,19,21]
sum=0
for i in l1:
  if is_prime(i):
    sum+=i

print(sum)


--------------------------------------------------------------
'''
'''
l1=[1,2,3,4,5,6,7,8,9,10]

print(
l1[len(l1)//2:][::-1]+l1[:len(l1)//2]
)


output:
[10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
'''

'''
--------------------------------------------------------------
wap to return nth largest element
l1=[2,13,7,61,1,25,70,24,19,45]
n=5

def selection_sort(l1):
  for i in range(len(l1)):
    min_ele=i
    for j in range(i+1,len(l1)):
      if l1[min_ele]>l1[j]:
        min_ele=j
    l1[i],l1[min_ele]=l1[min_ele],l1[i]

selection_sort(l1)

print(l1)
if n<=len(l1):print(l1[-n])
else:
  print(-1)

output:---

[1, 2, 7, 13, 19, 24, 25, 45, 61, 70]
24
----------------------------------------------------------
'''

'''
def nth_largest(l1,n):
  if len(l1)==0:
    return "list is empty"
  elif n<=0 or n>len(l1):
    return -1
  l2=l1


l1=[2,13,7,61,1,25,70,24,19,45]
n=0
print(nth_largest(l1,n))
-----------------------------------------------------------
'''

'''

def nth_largest (l1,n):
  if len(l1)==0:
    return "list is empty"
  
  elif n<=0 or n>len(l1):
    return -1

  for i in range(n):
    max_val=l1[0]
    idx=0

    for j in range(1,len(l1)):
      if l1[j]>max_val:
        max_val=l1[j]
        idx=j

    if i==n-1:
      return max_val
      
    del l1[idx]

l1=[1, 2, 7, 13, 19, 24, 25, 45, 61, 70]
n=10

print(nth_largest(l1,n))

1

'''