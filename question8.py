# 8. Keyword Search Tool 
# Ask user for a keyword and return all lines from file containing that keyword
# user se keyword lo
keyword = input("Enter keyword to search: ")

# file open karo
with open("sample1.txt", "r") as file:
    found = False
    
    for line in file:
        # case-insensitive search ke liye lower()
        if keyword.lower() in line.lower():
            print(line.strip())
            found = True

# agar keyword nahi mila
if not found:
    print("Keyword not found in file.")
