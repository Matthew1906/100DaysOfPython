

# Read File
file1 = open("note1.txt") #built in function\
# by default, the setting is read/r
content1 = file1.read()
print(content1)
# takes up some of the resources/storage
file1.close()
# close down means we are not longer using it, therefore not making it a burden to the computer

# with keyword
with open("note1.txt") as file:
    content = file.read()
    print(content1)

# write => need to change the mode into w 
with open("note2.txt",'w') as file:
    file.write("You are the Chosen One Anakin!")
    # rewriting a file completely
    # if the file doesnt exist -> create a new file

# append => need to change the mode into a 
with open("note1.txt",'a') as file:
    file.write("\nYou are the Chosen One Anakin!")

