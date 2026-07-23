# a=int(input("enter a number:"))
# b=int(input("enter b number:"))
# print(f'before swap: {a},{b}')
# a=a+b
# b=a-b
# a=a-b
# print(f'after swap: {a},{b}')

# a=int(input("enter a number:"))
# b=int(input("enter b number:"))
# print(f'before swap: {a},{b}')
# a=a*b
# b=a//b
# a=a//b
# print(f'after swap: {a},{b}')
#this fails for 0 value


a=int(input("enter a number:"))
b=int(input("enter b number:"))
print(f'before swap: {a},{b}')
a=a^b
b=a^b
a=a^b
print(f'after swap: {a},{b}')

# a,b=b,a

# enter a number:25
# enter b number:23
# before swap: 25,23
# after swap: 23,25