Number1=int(input("enter the number:"))
Number2=int(input("enter the number:"))
Number3=int(input("enter the number:"))
if(Number1 > Number2) and (Number1 > Number3):
   Number1 = largest
elif(Number2 > Number1) and (Number2 > Number3):
   Number2 = largest 
else:
   Number3 = largest
print ("the largest number is:",largest)


