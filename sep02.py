# #------------------------------------------------------


# l1=['7','l','@','2','u','8','H','2','$','a','r','1','r']

# # op=['r','1','@','r','a','2','H','8','$','u','2','l','7']

# print(l1)
# cnt=0
# for i in l1:
#   if i>='a' and i<='z' or i>='A' and i<='Z' or i>='0' and i<='9':
#     cnt+=1

# #create new list which accepts total number of values in cnt
# l2=[None]*cnt
# # print(l2)

# #store only numbers and chars to new list
# j=0
# for i in range(len(l1)):
#   if l1[i]>='a' and l1[i]<='z' or l1[i]>='A' and l1[i]<='Z' or l1[i]>='0' and l1[i]<='9':
#     l2[j]=l1[i]
#     j+=1
# #print(l2)
# #reverse the list

# l2=l2[::-1]
# # print(l2)

# #assign the 12 elements to l1 if  it is char or numbers
# j=0
# for i in range(len(l1)):
#   if l1[i]>='a' and l1[i]<='z' or l1[i]>='A' and l1[i]<='Z' or l1[i]>='0' and l1[i]<='9':
#     l1[i]=l2[j]
#     j+=1

# print(f'after replacing{l1}')


#------------------------------------------------------

l1=['7','l','@','2','u','8','H','2','$','a','r','1','r']

# op=['r','1','@','r','a','2','H','8','$','u','2','l','7']

print(l1)

def is_char_or_num(i):
  if i>='a' and i<='z' or i>='A' and i<='Z' or i>='0' and i<='9':
    return True
  else:
    return False

i=0
j=len(l1)-1
while i < j:
    if not is_char_or_num(l1[i]):
        i += 1
    elif not is_char_or_num(l1[j]):
        j -= 1
    else:
        # Swap when both i and j are alphanumeric characters
        l1[i], l1[j] = l1[j], l1[i]
        i += 1
        j -= 1
print(l1)



'''
['7', 'l', '@', '2', 'u', '8', 'H', '2', '$', 'a', 'r', '1', 'r']
['r', '1', '@', 'r', 'a', '2', 'H', '8', '$', 'u', '2', 'l', '7']
'''