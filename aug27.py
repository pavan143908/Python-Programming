'''
input:[10,20,30,10,4,5,7]
10
output:2

'''

# l1=eval(input("list:"))
# n=int(input("number:"))
# count=0
# for i in l1:
#   if i==n:
#     count+=1
# print(count)

# # list:[10,20,30,4,5,7,10,10]
# # number:10
# # 3

#------------------------------------------------------

'''

Right rotation:with in built method

input:[10,20,30,40,50]
n=1
output:[50,10,20,30,40]

n=2
output:[40,50,10,20,30]

'''

# l1=[10,20,30,40,50]
# n=int(input('n:'))
# while n!=0:
#   ele=l1.pop()
#   l1.insert(0,ele)
#   n-=1

# print(l1)


#-------------------------------------------------
'''

Right rotation:without in built method

input:[10,20,30,40,50]
n=1
output:[50,10,20,30,40]

n=2
output:[40,50,10,20,30]

'''

# l=[10,20,30,40,50]
# n=int(input('no of times to right shift elements:'))%len(l)
# for val in range(n):
#   temp=l[-1]
#   for i in range(len(l)-1,0,-1):
#     l[i]=l[i-1]
#   l[0]=temp

# print(l)

#-------------------------------------------------

'''

left rotation:with in built method

input:[10,20,30,40,50]
n=1
output:[20,30,40,50,10]

n=2
output:[30,40,50,10,20]

'''

# l=[10,20,30,40,50]
# n=int(input('number:'))%len(l)
# while n!=0:
#   l.append(l.pop(0))

#   n-=1

# print(l)


#-------------------------------------------------

'''

left rotation:without in built method

input:[10,20,30,40,50]
n=1
output:[20,30,40,50,10]

n=2
output:[30,40,50,10,20]

'''

# l=[10,20,30,40,50]
# n=int(input('number:'))%len(l)
# for val in range(n):
#   temp=l[0]

#   for i in range(len(l)-1):
#     l[i]=l[i+1]

#   l[-1]=temp
# print(l)

#-------------------------------------------------
# l1=[10,20,30,40,50]
# l2=[]
# l2+=[l1[0]]
# print(l2)



#-------------------------------------------------
# l1=[10,20,30,40,50]
# l2=[]

# for i in l1:

#   l2+=[i]
# print(l2)

#-------------------------------------------------
# l1=[10,20,30,40,50]
# l2=[x for x in l1]
# print(l2)

# #------------------------------------------------

# def fun(l1):
#   l1[0]=1000
#   print(id(l))

# l=[10,20,30]
# print(l,id(l))
# fun(l)
# print(l)

#------------------------------------------------

# d1={1:10,2:20,3:30}
# print(d1)
# d1[4]=40
# print(d1)
#------------------------------------------------

d1={1:10,2:20,3:30}
d2={}
for i in d1:
  d2[i]=d1[i]
print("d2 dict",d2)
print("d1 dict",d1)