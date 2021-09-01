# Import modules
from tkinter import Tk, Button, Label, Canvas, Entry
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Setup functions
def browse_image():
    '''Search for images'''
    global logo_img, img
    filename = askopenfilename(
        initialdir = "/",
        title = "Select a File",
        filetypes=[('Image Files', '*png')]
    )
    img = Image.open(str(filename))
    img = img.resize((150,150), Image.ANTIALIAS)
    logo_img = ImageTk.PhotoImage(image = img)
    logo_canvas.itemconfigure(logo_image, image=logo_img)
    file_input.config(text=filename.split('/')[-1])

def add_watermark():
    '''Add text watermark to the image'''
    global logo_img, img, watermarked
    watermarked = img.copy()
    draw = ImageDraw.Draw(watermarked)
    font = ImageFont.truetype("./assets/font.ttf", 15)
    draw.text((5, 125), f"©{caption_input.get().strip()}", (0, 0, 0), font=font)
    logo_img = ImageTk.PhotoImage(image = watermarked)
    logo_canvas.itemconfigure(logo_image, image=logo_img)

def save_image():
    '''Save image into folder'''
    global logo_img, watermarked
    new_file =  file_input.cget("text")
    showinfo(title='Image successfully saved', message= f'{new_file} successfully saved')
    watermarked = watermarked.save(f'./images/wm_{new_file}')

# Setup Screen
window = Tk()
window.title('Watermarking App')
window.config(padx=30, pady=20)

# Setup Photoimages
img = Image.open('./assets/logo.png')
img = img.resize((150,150), Image.ANTIALIAS)
logo_img = ImageTk.PhotoImage(image = img)

# Setup Canvas
logo_canvas = Canvas(width=150, height=150)
logo_image = logo_canvas.create_image(75, 75, image=logo_img)

# Setup Label
file_label = Label(text="Insert file: ")
file_input = Label(text='logo.png', bg = 'white', width=20)
caption_label = Label(text='Insert text: ')

# Setup Entry
caption_input = Entry(width=24)

# Setup Button
file_button = Button(text="Browse", command=browse_image)
watermark_button = Button(text='Add Watermark', command=add_watermark)
save_button = Button(text='Save Image', command=save_image, width=24)

# Setup Layout
logo_canvas.grid(row=0, column=1)
file_label.grid(row=1, column=0, sticky='EW')
file_input.grid(row=1, column=1, padx=10)
file_button.grid(row=1, column=2, sticky='EW')
caption_label.grid(row=2, column=0, sticky='EW')
caption_input.grid(row=2, column=1, padx=10)
watermark_button.grid(row=2, column=2, sticky='EW')
save_button.grid(row=3, column=1, pady=10)

# Driver code
window.mainloop()