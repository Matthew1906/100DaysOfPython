from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width = 500, height=400)

label = Label(text="This is a new text", font = ['Arial',12,'normal'])

button = Button(text="Click Me")

text_input = Entry()
text_input.insert(END, string = 'Some text to input')

# END -> index

text_area = Text(width = 30, height = 5) #text area
text_area.focus()
text_area.insert(END, 'Example of text area')

def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_= 0, to=10, command = spinbox_used) # counter

# scale = Slider
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)

# Checkbutton = checkbox
def checkbox_checked():
    print(checked_state.get())
checked_state = IntVar()
checkbox = Checkbutton(text="is on?", variable = checked_state, command = checkbox_checked)

# Radiobutton = radio button
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radio1 = Radiobutton(text = "Option 1", value = 1, variable = radio_state, command = radio_used)
radio2 = Radiobutton(text = "Option 2", value = 2, variable = radio_state, command = radio_used)

# Listbox = well you get the point
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ['Apple','Pear','Orange','Banana']
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>", listbox_used)

# Pack the components
label.pack()
button.pack()
text_input.pack()
text_area.pack()
spinbox.pack()
scale.pack()
checkbox.pack()
radio1.pack()
radio2.pack()
listbox.pack()

# Loop the window
window.mainloop()