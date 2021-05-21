# FUNCTIONS WITH OUTPUTS

# A. FUNCTIONS WITH OUTPUTS

def format_name1(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"

print(format_name1("MATThew",'aDrianus'))

# B. MULTIPLE RETURN VALUES
def format_name2(first_name, last_name):
    if first_name=='' or last_name=='':
        return "Wrong input!"
    return f"{first_name.title()} {last_name.title()}"

# C. DOCSTRINGS -> documenting a function
def format_name3(first_name, last_name):
    '''Take a first and last name and join them together in title case'''
    if first_name=='' or last_name=='':
        return "Wrong input!"
    return f"{first_name.title()} {last_name.title()}"
print(format_name3("MATThew",'aDrianus'))

# D. PRINT VS RETURN
# E. WHILE LOOPS, FLAGS, AND RECURSION