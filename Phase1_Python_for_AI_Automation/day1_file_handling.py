import os 

files = ["report_1.txt", "report_2.txt", "report_3.txt"] 

# with open("report_1.txt", "r") as file: 
#     content = file.read() 
#     print(content)  

# with open("report_2.txt", "r") as file: 
#     for line in file: 
#         print(line.strip())  

with open("report_3.txt", "w") as file: 
    file.write("Hello, this is a 3rd report.\n") 
    file.write("This is the second line of the report.\n") 

with open("report_3.txt", "a") as file: 
    file.write("This line is appended to the report.\n") 
    file.write("This is another line added to the report.\n") 

if os.path.exists("report_4.txt"): 
    os.remove("report_4.txt") 
else: 
    try: 
        with open("report_4.txt", "x") as file: 
            file.write("This is a new report file.\n") 
            print("File created successfully.") 
    except FileExistsError: 
        print("File already exists.") 

