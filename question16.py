# Question16 A shopkeeper wants to calculate total bill after discount

# Taking input from user
price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))

# Calculating discount amount
discount_amount = (discount * price) / 100

# Final bill
total_bill = price - discount_amount

# Output
print("Discount Amount:", discount_amount)
print("Total Bill after Discount:", total_bill)