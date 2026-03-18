# Question42 check whether a person is eligible to vote
age = int(input("Enter your age: "))

print("Eligible" * (age >= 18) + "Not Eligible" * (age < 18))