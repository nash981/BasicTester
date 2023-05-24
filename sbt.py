import os, sys

c_sourcepath = input("C source file path: ")# Take the input of path/name file
test_filepath = input("Test file directory path: ")# Take the input of path/name to the directory conataining test cases
test_filepath = test_filepath.split("/")
c_sourcepath = c_sourcepath.split("/")
# Finding the absolute filepath of test folder
res = os.popen("cd ~; find \"./\" -type d -name \""+test_filepath[-1].strip()+"\"")
dir_list = res.readlines()

# try:
absolute_testfilepath = dir_list[-1].strip() # Filepath for the test_folder
# Finding the absolute filepath of C file
res = os.popen("cd ~; find \"./\" -type f -name \""+c_sourcepath[-1].strip()+"\"")
dir_list = res.readlines()
# except IndexError:
#     print("File not found")


# try:
absolute_csourcepath = dir_list[-1].strip() # filepath for the c file.
absolute_csourcepath = absolute_csourcepath.split("/")
filename = c_sourcepath[-1]
absolute_csourcepath = "/".join(absolute_csourcepath[:-1])
# Create a list of test folders. 
res = os.popen("cd ~; cd "+absolute_testfilepath+"; ls -d */")
folder_list = res.readlines()
#print(folder_list)
# except IndexError:
#      print("Directory not found")

#print(absolute_testfilepath)

# Compiling the C code
res = os.popen("cd ~; cd " +absolute_csourcepath+"; gcc -Wall -Werror -std=c11 "+filename+" -lm")
outp = res.readlines()
if outp != []:
    print("failed to complie your code")
for folders in sorted(folder_list):
    res = os.popen("cd ~; "+ absolute_csourcepath +"/./a.out < ./" + absolute_testfilepath +"/"+folders.strip()+"input.txt")
    pop = res.readlines();
    res= os.popen("cd ~; cat ./" + absolute_testfilepath + "/" +folders.strip()+"output.txt")
    pop2 = res.readlines()
#    print(pop2)
#    print(pop)
    for i in range(len(pop)):
        status = True
        if pop[i].strip() != pop2[i].strip():
            print("#### Test: "+folders.strip()+" failed! ####")
            print("#### EXPECTED TO SEE:")
            print("".join(pop2))
            print("#### INSTEAD GOT:")
            print("".join(pop))
            status = False
            break
    if(status):
        print("#### Test: "+folders.strip()[:-1]+" passed! ####")

