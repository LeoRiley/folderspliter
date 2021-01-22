import os
import shutil
path = input("enter path:")

path = r'C:\Users\leori\source\repos\folderspliter'
os.chdir(path)
list_of_files = os.listdir()
number_of_files = len(list_of_files) + 1
number_of_folders = number_of_files//100+1
i=1
for x in range(number_of_folders):
    newpath = f"{x+1}" 
    if not os.path.exists(newpath):
        os.makedirs(newpath)



i = 1
j = 0
for eachitem in list_of_files:
    stringj = str(j)
    print(i,j)
    # shutil.copy2(eachitem,stringj)
    i+=1
    if i//100 > j:
        j += 1



    
    
