
#count of even numbers ,odd numbers excluding 0
#  l1=[10,2,15,5,3,24,81,0,0,0]
# even_count,odd_count=0,0
# for i in l1:
#   if i==0:
#     continue
#   elif i%2==0:
#     even_count+=1
#   else:
#     odd_count+=1

# print(even_count,odd_count,sep='\n')

# 3
# 4
#______________________________________________________

#sum of even numbers,sum of oddnumbers

# l1=[10,2,15,5,3,24,81]
# even_count,odd_count=0,0
# for i in l1:
#   if i==0:
#     continue
#   elif i%2==0:
#     even_count+=i
#   else:
#     odd_count+=i

# print(even_count,odd_count,sep='\n')

# 36
# 104


#______________________________________________________


# l1=[300,40,500,1,-8,-4]

# print(max(l1))
# print(min(l1))

# 500
# -8
#______________________________________________________


# l1=[300,40,500,1,-8,-4]
# l1.sort()
# print(l1[-1])
# print(l1[0])

# 500
# -8
#______________________________________________________
 #finding maximum element without using max() inbuilt method

# l1=[300,40,500,1,-8,-4]
# Max=l1[0]

# for i in l1:
#   if i>Max:
#     Max=i


# print(Max)

#______________________________________________________
#finding minimum element without using min() inbuilt method

# l1=[300,40,500,1,-8,-4]
# Min=l1[0]

# for i in l1:
#   if i<Min:
#     Min=i


# print(Min)

# -8

#______________________________________________________

# l1=[300,40,500,1,-8,-4]
# Min=l1[0]
# Max=l1[0]

# for i in l1:
#   if i<Min:
#     Min=i
#   if i>Max:
#     Max=i


# print(Min)
# print(Max)
# -8
# 500

#______________________________________________________
#reverse a list 
# l1=[10,5,3,4,2]
# l1.reverse()
# print(l1)

# [2, 4, 3, 5, 10]
#______________________________________________________

# l1=[10,5,3,4,2]
# print(l1)
# res=l1[::-1]
# print(res)

# [2, 4, 3, 5, 10]
# [10, 5, 3, 4, 2]
# [2, 4, 3, 5, 10]

#______________________________________________________

# l1=[10,5,3,4,2]
# print(l1,id(l1))
# res=l1[::]
# print(res,id(res))

# [2, 4, 3, 5, 10]
# [10, 5, 3, 4, 2] 2254656267072
# [10, 5, 3, 4, 2] 2254654257088

#______________________________________________________

# l1=[10,5,3,4,2]
# print(l1,id(l1))
# res=l1[::] #deep copy
# print(res,id(res))

# [2, 4, 3, 5, 10]
# [10, 5, 3, 4, 2] 2254656267072
# [10, 5, 3, 4, 2] 2254654257088

#______________________________________________________

# l1=[10,5,3,4,2]
# print(l1,id(l1))
# res=l1[::-1]
# print(res,id(res))
# [2, 4, 3, 5, 10]
# [10, 5, 3, 4, 2] 3109042807616
# [2, 4, 3, 5, 10] 3109040142272

# #______________________________________________________

# l1=[10,5,3,4,2]
# print(l1)
# res=[]
# for i in range(len(l1)-1,-1,-1):
#   res.append(l1[i])
# print(res)

# [10, 5, 3, 4, 2]
# [2, 4, 3, 5, 10]


# #______________________________________________________

# l1=[10,5,3,4,2]
# print("before:",l1)
# i,j=0,len(l1)-1
# while i<j:
#   l1[i],l1[j]=l1[j],l1[i]
#   i+=1
#   j-=1

# print("after:",l1)
# before: [10, 5, 3, 4, 2]
# after: [2, 4, 3, 5, 10]
#______________________________________________________
#to pointer approach

l1=[10,5,3,4,2]
print("before:",l1)
i,j=0,len(l1)-1
while i<j:
  l1[i],l1[j]=l1[j],l1[i]
  i+=1
  j-=1

print("after:",l1)