# l=[10,20,30,40,40,50]
# key=int(input('key:'))
# res=[]
# for i in l:
#   if i!=key:
#     res.append(i)
# print(res)

# key:10
# [20, 30, 40, 40, 50]
# PS C:\Users\DELL\Desktop\Programming> py aug28.py
# key:40
# [10, 20, 30, 50]

#----------------------------------------------------

# l=[10,20,10,10,10,30,40,40,80]
# key=int(input('key:'))
# p=0
# while p<len(l):
#   if l[p]==key:
#     for i in range(p,len(l)-1):
#       l[i]=l[i+1]
#   # l.pop()
#     del l[-1] #alternative 
#   else:
#     p+=1

# print(l)


# key:40
# [10, 20, 10, 10, 10, 30, 80]

# key:10
# [20, 30, 40, 40, 80]

#----------------------------------------------------

# l=[1,2,1,4,8,3,7,2,4]
# res=[]

# for i in l:
#   if i not in res:
#     res.append(i)

# print(res)


# [1, 2, 4, 8, 3, 7]


#----------------------------------------------------
# l=[1,2,1,4,8,3,7,2,4]

# p=0
# while p<len(l):
#   j=p+1
#   while j<len(l):
#     if l[j]==l[p]:
#       del l[j]
#     else:
#       j+=1

#   p+=1
# print(l)
#----------------------------------------------------

# l=[1,2,1,4,8,3,7,2,4]
# print(list(dict.fromkeys(l)))

#----------------------------------------------------


l=[1,2,1,4,8,3,7,2,4]
l=list(dict.fromkeys(l))
print(l)
