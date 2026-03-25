user=int(input("How high pyramid?: "))
for i in range (1,(user+1)):
   print(" "*i, end="" )
   for j in range (1,(user-i)+2):
      print(j, end=" ")
   print()