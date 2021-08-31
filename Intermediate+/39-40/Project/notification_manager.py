import smtplib
class NotificationManager:
    '''Sending Notifications through email about cheap flight deals'''
    def __init__(self):
        '''Notification Manager Constructor'''
        self.email = 'dummy124635789@gmail.com'
        self.password = 'dummy@1234'

    def sendmail(self,details, name, email):
        '''Send Mail Function'''
        message = '\n'.join([f"Dear {name}",
            f"We found cheap flight tickets from {details.city_from} to {details.cityTo}!",
            f"Here are the details of the flight:",
            f"- Departure Airport Code: {details.dep_airport}",
            f"- Arrival Airport Code: {details.arr_airport}",
            f"- Destination: {details.cityTo}, {details.countryTo}",
            f"- Price: {details.price} pound sterling",
            f"- Local Departure Time: {details.dep_date}, {details.dep_time}",
            f"- Local Arrival Time: {details.arr_date}, {details.arr_time}",
            "", "Copy the link below and paste it in the browser to buy a ticket!",
            "", f"{details.link}","","Regards,""","Flight Club Team"])
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user = self.email, password=self.password)
            conn.sendmail(from_addr=self.email, to_addrs=email, msg=f"Subject: Flight Club Notifications\n\n{message}")