#Basic GUI app

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width = 600, height = 300) #Set window settings 
canvas.grid(columnspan=3, rowspan = 3) #Split window into 3 seperate grids

#Logo
logo = Image.open('logo.png') #Load Image
logo = ImageTk.PhotoImage(logo) #Turn image into a tkinter image
logo_label = tk.Label(image = logo) #Create a display box
logo_label.image = logo #Add image to the display box
logo_label.grid(column = 1, row = 0) #Display the box in a set destination

#Instructions
instructions = tk.Label(root, text = "Select a PDF file on your computer to extract all its text", font = "Raleway") #Create text box
instructions.grid(columnspan = 3, column = 0, row =1) #Display text box
 
def open_file():
    browse_text.set("Loading...") #Change the button text
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")]) #Select the PDF to open
    
    if file: #If a PDF was selected
        read_pdf = PyPDF2.PdfFileReader(file) #Read the pdf in
        page = read_pdf.getPage(0) #Get the first page of the pdf
        page_content = page.extractText() #Get the text of the page
        
        #Textbox
        text_box = tk.Text(root, height = 10, width = 50, padx=15, pady= 15) #Create a text box
        text_box.insert(1.0, page_content) #Add the contents of the PDF to the text box
        text_box.tag_configure("center", justify = "center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column = 1, row = 3) #Display the text box
        
        browse_text.set("Browse")    
    


#browse button
browse_text = tk.StringVar() #Create a variable to hold text
browse_btn = tk.Button(root, textvariable = browse_text, font = "Raleway", bg = "#20bebe", fg="white", height =2, width = 15, command = lambda: open_file()) #Create a button 
browse_text.set("Browse") #Set the text of the button
browse_btn.grid(column = 1, row = 2) #Display the button

canvas = tk.Canvas(root, width = 600, height = 250) #Set window settings 
canvas.grid(columnspan=3) #Split window into 3 seperate grids



root.mainloop()