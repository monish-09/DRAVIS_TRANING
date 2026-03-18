#question 29 print all even numbers between 1 to N
l=[]
num= int(input("Enter number: "))
for i in range(2,num+1,2):
    l.append(i)
print(l)    