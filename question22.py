# Question22 check whether a person is eligible to vote
age = int(input("Enter age: "))
result = ["Not Eligible", "Eligible"]

print(result[age >= 18])