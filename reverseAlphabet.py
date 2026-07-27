row=int(input("row:"))
col=int(input("col:"))
for i in range(row):
  val=ord('Z')
  for j in range(col):
    print(chr(val),end=' ')
    val-=1
  print()
#*************************************************************
# row:4
# col:3
# Z Y X 
# Z Y X 
# Z Y X 
# Z Y X