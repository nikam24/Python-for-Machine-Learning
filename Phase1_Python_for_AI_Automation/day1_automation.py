import os 

files = ["report1.txt", "report2.txt", "report3.txt"] 

for index, file in enumerate(files, start=1): 
    new_name = f"report_{index}.txt" 
    os.rename(file, new_name) 