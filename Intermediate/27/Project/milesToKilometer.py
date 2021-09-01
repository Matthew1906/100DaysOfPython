# import modules
from tkinter import Tk, Label, Button, Entry

# set window, labels, buttons, entries
window = Tk()
window.title("Mile to Km")
window.minsize(width = 250, height = 60)
window.config(padx = 15, pady = 15)

equal_label = Label(text= "is equal to", font = ['Arial', 12, 'normal'])
mile_label = Label(text= "Miles", font = ['Arial', 12, 'normal'])
km_label = Label(text= "Km", font = ['Arial', 12, 'normal'])
km_result = Label(text = "0", font = ['Arial', 12, 'normal'])
km_result.config(padx=10)

mile_input = Entry(width = 15)
mile_label.config(padx=10)

def calculate():
    miles = int(mile_input.get())
    km_result['text'] = round(miles*1.609,1)

calculate_button = Button(text = "Calculate", command = calculate)

# set position
mile_input.grid(row = 0, column = 1)
mile_label.grid(row = 0, column = 2)
equal_label.grid(row = 1, column =0)
km_result.grid(row = 1, column = 1)
km_label.grid(row = 1, column = 2)
calculate_button.grid(row = 2, column = 1)

window.mainloop()