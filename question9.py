# question9  find longest line
# identify the longest line in a file and print its lengths and content
# file open karo
with open("sample.txt", "r") as file:
    longest_line = ""
    
    for line in file:
        # newline remove karne ke liye strip use kar rahe hain
        line = line.rstrip("\n")
        
        if len(line) > len(longest_line):
            longest_line = line

# result print karo
print("Longest Line Length:", len(longest_line))
print("Longest Line Content:", longest_line)