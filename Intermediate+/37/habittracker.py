from tkinter import Tk, Button, Label, Entry
import requests, datetime as dt, webbrowser

url = 'https://pixe.la/v1/users/matthew1906/graphs/c7b3r53cur1t7'

graph_headers = {    
    'X-USER-TOKEN':'h4b1ttr4ck3r499'
}

def submit():
    value_params = {
        'date': dt.datetime.now().strftime("%Y%m%d"),
        'quantity':report_entry.get(),
    }
    requests.post(url = url, headers=graph_headers, json = value_params)
    webbrowser.open('https://pixe.la/v1/users/matthew1906/graphs/c7b3r53cur1t7.html')

window = Tk()
window.title("Study Hours")
window.config(padx=25, pady=25)

title_label = Label(text="Study Hours Tracker", font = ['Arial', 18, 'bold'])
report_label = Label(width = 15,text="Total Learning Hours:", font = ['Arial', 10, 'normal'])
submit_button = Button(width = 20, text = "Submit", command=submit, bg = 'red', fg ='white')
report_entry = Entry(width= 35)

title_label.grid(row = 0, column = 0, columnspan = 2)
report_label.grid(row = 2, column = 0, sticky = 'EW')
report_entry.grid(row = 2, column = 1, sticky = 'EW')
submit_button.grid(row = 3, column =0, columnspan = 2)
window.mainloop()