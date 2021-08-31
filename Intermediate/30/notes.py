# with open('a_file.txt') as file:
#     file.read() #error since there is no such file
# not great, since when there is an error, then the program stops

# Index error -> accessing wrong index

# Type Error -> wrong data type

# Need to plan for the worst -> Murphy's Law

# 1. Catch Exceptions
# -> try, except, else, finally
# try -> executing something that might cause an exception
# except -> do this if something went wrong
# else -> do this if there were no exceptions
# finally -> carry out this whatever happens

# file not found

try:
    file = open("a_file.txt",'r')
    a_dictionary = {"key":"value"}
    print(a_dictionary['sdfsdfsdf'])
except FileNotFoundError:
    # never use a bare except
    # without bare exception, every error will just go through here
    file = open("a_file.txt",'w')
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    raise KeyError("This is a raise trial") #get an error
# Custom exception raise exception
