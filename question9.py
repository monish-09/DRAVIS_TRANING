#question9 print all even numbers between 1 to N

# create list
l=[]
num= int(input("Enter number: "))
for i in range(2,num+1,2):
    l.append(i)  #list ma append kiya i
print(l)    