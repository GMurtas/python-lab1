print('Insert a string')
str=input()
length=len(str)
if length < 2 :
  print(" ")
else :
    print(str[0:2] + str[length-2:length])
