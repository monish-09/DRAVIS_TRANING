# 1. Copy contents of one file into another. 
#  Copy the Contents of one file into another

# source file read mode me open karo
with open("source.txt", "r") as source:
    
    # destination file write mode me open karo
    with open("destination.txt", "w") as dest:
        
        # pura content read karo
        content = source.read()
        
        # destination file me likho
        dest.write(content)

print("File copied successfully!")