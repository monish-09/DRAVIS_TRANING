# Question12 check whether a person is eligible to vote

age = int(input("Enter age: "))

if age in range(18, 200):
    print("Eligible")
else:
    print("Not Eligible")