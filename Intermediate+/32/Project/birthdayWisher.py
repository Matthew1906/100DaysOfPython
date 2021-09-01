# 1. Import Libraries, Read CSV, Setup Email and Password
import smtplib, datetime as dt, pandas as pd, random 

print("Input your credentials! (make sure it's gmail and you have allowed third party application to send emails")
name = input("Insert your name: ")
user = input("Insert your email: ")
password = input("Insert your password: ")

birthday_df = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv

current = dt.datetime.now()
rows = birthday_df[birthday_df.columns[0]].count()

emails_to_send = []
for row in range(rows):
    if birthday_df.loc[row,'month'] == current.month and birthday_df.loc[row,'day']== current.day:
        name = birthday_df.loc[row,'name']
        email = birthday_df.loc[row,'email']
        emails_to_send.append({
            'name':name,
            'email':email
        })

# 3. pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if len(emails_to_send)>0:
    for email in emails_to_send:
        letter_type = random.randint(1,3)
        letter_name = f"letter_templates/letter_{letter_type}.txt"
        with open(letter_name) as letter_file:
            letter = letter_file.read()
        letter = letter.replace('[NAME]', email['name']).replace('[SENDER]', name)
        print(f"Sending birthday wish to {email['name']}")
# 4. Send the Email
        with smtplib.SMTP('smtp.gmail.com:587') as connection:
            connection.starttls()
            connection.login(user=user, password = password)
            connection.sendmail(from_addr=user, to_addrs=email['email'], msg = "Subject: Hello there:)\n\n"+letter)
        print(f"Birthday Card sent to {email['name']}")
else:
  print("No one is having his/her birthday today..")