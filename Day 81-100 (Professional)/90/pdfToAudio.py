# Day 90 of 100 Days of Python
# Project name: PDF to Audio Converter
# Things I implemented: Tkinter, Text-To-Speech, PDF Reader

# Import modules
from tkinter import Tk, Label, Button, PhotoImage, Canvas, StringVar
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileReader
from gtts import gTTS

# I can't find any Online API that fit my preferences
# Therefore I decided to use a Module instead

# Global variables
file = None
pdf_file = None
audio_content = None
lang_dict = {
    'English':'en',
    'Indonesia':'id',
}

# Functions
def browse_pdf():
    '''Get PDF File'''
    global pdf_file, file
    filename = askopenfilename(
        initialdir = "/",
        title = "Select a File",
        filetypes=[('PDF Files', '*pdf')]
    )
    if file is not None:
        file.close()
    file = open(filename, 'rb')
    pdf_file = PdfFileReader(file)  
    pdf_label.config(text=filename.split('/')[-1])
    convert_button.config(state='normal')

def pdf_to_audio():
    '''Convert PDF to Audio'''
    global pdf_file, audio_content
    # Convert to text file
    pdf_to_text = ''
    for page_num in range(pdf_file.numPages):
        page = pdf_file.getPage(page_num)
        pdf_to_text += page.extractText()
    # Convert to audio file using HTTP Request
    audio_content = gTTS(pdf_to_text, lang=lang_dict.get(languages.get()))
    audio_label.config(text=pdf_label.cget('text').split('.')[0].strip() +'.mp3')
    download_button.config(state='normal')

def download_audio():
    '''Download Audio'''
    global audio_content
    file_name = './audio/'+ pdf_label.cget('text').split('.')[0].strip() +'.mp3'
    audio_content.save(file_name)

# UI
## Config Screen
screen = Tk()
screen.title('PDF to Audiobook Converter')
screen.config(padx=40, pady=30)

## Config PhotoImage
logo_image1 = PhotoImage(file='./images/pdf.png')
logo_image2 = PhotoImage(file='./images/audio.png')

## Config Canvas
logo_canvas1 = Canvas(width=150, height=150)
logo_canvas1.create_image(75,75, image=logo_image1)
logo_canvas2 = Canvas(width=150, height=150)
logo_canvas2.create_image(75,75, image=logo_image2)

## Config Label
pdf_label = Label(text='No File Chosen', bg='white')
audio_label = Label(text='No File Converted', bg='white')
language_label = Label(text='Select Language')

## Config Button
browse_button = Button(text='Browse', command=browse_pdf)
convert_button = Button(text='Convert to Audio', state='disabled', command=pdf_to_audio)
download_button = Button(text='Download', state='disabled', command=download_audio)

## Config Combobox
n = StringVar()
languages = Combobox(screen, textvariable=n)
languages['values']=('English', 'Indonesia')
languages.current(0)

## Layout
logo_canvas1.grid(row=0, column=0, sticky='EW')
logo_canvas2.grid(row=0, column=1, sticky='EW')
pdf_label.grid(row=1, column=0, sticky='EW') 
browse_button.grid(row=1, column=1, sticky='EW')
language_label.grid(row=2, column=0, sticky='EW', pady=5)
languages.grid(row=2,column=1, sticky='EW', pady=5)
convert_button.grid(row=3, column=0, columnspan=2, sticky='EW', pady=5)
audio_label.grid(row=4, column=0, sticky='EW') 
download_button.grid(row=4, column=1, sticky='EW')

# Driver code
screen.mainloop()