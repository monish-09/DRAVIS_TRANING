while True:  # jab tak chalaga jab tak 75 marks sa kam na ho
    print("1: Enter student data")
    print("0: Exit")

    n = int(input("Enter choice (1/0): "))   #enter the user input 

    if n == 0:  # condition agar nuser input 0 ka equal ha to program yahi ruk jayga aga run  nahi karaga
        break

    if n == 1:   # agr 1 press kiya to aga process hoga 
        name = input("Enter student name: ")     # enter the name
        marks = int(input("Enter student marks: "))   # enter the marks 
        city = input("Enter student city: ")  # enter the city name 


        #  create the dictionary
        student = {
            "name": name,
            "marks": marks,
            "city": city
        }

        if marks > 75:   # agr marks greater then 75 ha 
            with open("student.txt", "a") as f:      #student  name ki file banagi 
                f.write(str(student) + "\n")   # usma code write hoga
        else:
            with open("student1.txt", "a") as f:   # agr marks greater then 75 nahi ha 
                f.write(str(student) + "\n")     #student1  name ki file banagi ,usma code write hoga

        print("Data saved successfully!\n")