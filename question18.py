# Question18 Calculate electricity bill based on units consumed
# Taking input
units = int(input("Enter electricity units consumed: "))

bill = 0

# Calculating bill based on unit
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

# Output
print("Total Electricity Bill: ₹", bill)
