# DAY 24 PROJECT OF 100 DAYS OF CODE
# PROJECT NAME: MAIL MERGE
# THINGS I IMPLEMENTED: STRING FUNCTIONS, FILE PROCESSING, PATHS

# Retrieve the template
with open(".\\Project\\Input\\Letters\\letter_template.txt") as letter_template_file:
    letter_template = letter_template_file.read()
# Retrieve the names
with open(".\\Project\\Input\\Names\\names.txt") as name_file:
    names = name_file.read().split("\n")

# Create Mail
for name in names:
    # Create a mail name
    mail_name = "letter_to_"+name.strip().lower()+".txt"
    # Create the mail content
    mail = letter_template.replace("[name]", name.strip())
    # Write into text file
    with open(".\\Project\\Output\\"+mail_name, "w") as mail_text:
        mail_text.write(mail)