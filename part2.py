with open("remove.txt", "r") as f:  # first open file
    lines = f.readlines()  # read line by line

unique_lines = []   #append  unique line
seen = set()   # create empty set

for line in lines:  # for loop chalaya lines sa
    if line not in seen:    #agr set ma nahi ha  
        unique_lines.append(line)   # append kra list ma 
        seen.add(line)  #set me line add kr di 

with open("article.txt", "w") as f:   # file open kri

    f.writelines(unique_lines)  #write mode ma

print("Duplicate lines removed (order preserved)!")