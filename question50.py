# Question50 Create a function to calculate simple interst
# create a simple_interest function
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

interest = simple_interest(principal, rate, time)

# Output
print("Simple Interest:", interest)