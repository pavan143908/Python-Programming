
# n=int(input("row:"))
# i=0
# while(i<n):
#   print('*',' ','*')
#   i+=1
# *   *
# *   *
# *   *
# *   *
# *   *


# row=int(input("row:"))
# for i in range(row):
#   print('* *')


# row=int(input("row:"))
# col=int(input('co:'))
# for i in range(row):
#   for j in range(col):
#     print('*',end=' ')
#   print()
# row:3
# co:2
# * * 
# * * 
# * * 



# row=int(input("row:"))
# col=int(input('co:'))
# val=1
# for i in range(row):
#   for j in range(col):
#     print(val,end=' ')
#     val+=1
#   print()
# row:3
# co:3
# 1 2 3 
# 4 5 6 
# 7 8 9


# row=int(input("row:"))
# col=int(input('col:'))
# val=1
# for i in range(row):
#   for j in range(col):
#     print(val,end=' ')
#     val+=1
#     if val>9:
#       val=1
#   print()

# row:10
# col:10
# 1 2 3 4 5 6 7 8 9 1 
# 2 3 4 5 6 7 8 9 1 2 
# 3 4 5 6 7 8 9 1 2 3 
# 4 5 6 7 8 9 1 2 3 4 
# 5 6 7 8 9 1 2 3 4 5 
# 6 7 8 9 1 2 3 4 5 6 
# 7 8 9 1 2 3 4 5 6 7 
# 8 9 1 2 3 4 5 6 7 8 
# 9 1 2 3 4 5 6 7 8 9 


# row=int(input("row:"))
# col=int(input('col:'))
# width=len(str(row*col))

# val=1
# for i in range(row):
#   for j in range(col):
#     print(str(val).zfill(width),end=' ')
#     val+=1
#   print()
#zfill is a string inbuilt method that adds given width to prefix of string

# row:10
# col:10
# 001 002 003 004 005 006 007 008 009 010 
# 011 012 013 014 015 016 017 018 019 020 
# 021 022 023 024 025 026 027 028 029 030 
# 031 032 033 034 035 036 037 038 039 040 
# 041 042 043 044 045 046 047 048 049 050 
# 051 052 053 054 055 056 057 058 059 060 
# 061 062 063 064 065 066 067 068 069 070 
# 071 072 073 074 075 076 077 078 079 080 
# 081 082 083 084 085 086 087 088 089 090 
# 091 092 093 094 095 096 097 098 099 100 


# row=int(input("row:"))
# col=int(input('col:'))
# # width=len(str(row*col))
# val=1
# for i in range(row):
#   for j in range(col):
#     # print(str(val).zfill(width),end=' ') 
#     print(val ,end=" ")
  
#   print()
#   val+=1
#   if val>9:
#     val=1

# row:20
# col:10
# 1 1 1 1 1 1 1 1 1 1 
# 2 2 2 2 2 2 2 2 2 2 
# 3 3 3 3 3 3 3 3 3 3 
# 4 4 4 4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 5 
# 6 6 6 6 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 7 7 7 
# 8 8 8 8 8 8 8 8 8 8 
# 9 9 9 9 9 9 9 9 9 9 
# 1 1 1 1 1 1 1 1 1 1 
# 2 2 2 2 2 2 2 2 2 2 
# 3 3 3 3 3 3 3 3 3 3 
# 4 4 4 4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 5 
# 6 6 6 6 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 7 7 7 
# 8 8 8 8 8 8 8 8 8 8 
# 9 9 9 9 9 9 9 9 9 9 
# 1 1 1 1 1 1 1 1 1 1 
# 2 2 2 2 2 2 2 2 2 2 



# row=int(input("row:"))
# col=int(input('col:'))
# # width=len(str(row*col))
# for i in range(row):
#   val=1
#   for j in range(col):
#     # print(str(val).zfill(width),end=' ') 
#     print(val ,end=" ")
#     val+=1
  
#   print()
#   if val>9:
#     val=1

# row:5
# col:5
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 


row=int(input("row:"))
col=int(input('col:'))
for i in range(row):
  val=1
  for j in range(col):
    print(val ,end=" ")
    val+=1
  print()





