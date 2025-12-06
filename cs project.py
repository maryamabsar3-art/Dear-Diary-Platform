from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

def login():
    username = entry1.get()
    password = entry2.get()
    
    if username == "" and password == "":
        messagebox.showinfo("Login failed", "Blanks are not allowed")
    elif username == "maryam" and password == "1234":
        messagebox.showinfo("Login Successful", "Welcome to Dear Diary!")
        
        window.withdraw()
        home_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")



window = Tk()
window.geometry("420x420")
window.title("Dear Diary,")

icon = PhotoImage(file='scroll.png')
window.iconphoto(True,icon)
window.config(background="#373b4d")

global entry1
global entry2

login_page = Label(window, text='Login Page', bg = "#373b4d", fg = "white", font= ('Times new roman', 15))
login_page.place(relx=0.5, y=20, anchor="center") 

username_label = Label(window, text= "UserName: ", bg = "#373b4d", fg = "white", font= ('Times new roman', 10))
username_label.place(x=70, y=60)
password_label = Label(window, text= "Password: ", bg = "#373b4d", fg = "white", font= ('Times new roman', 10))
password_label.place(x=70, y=80)

entry1 = Entry(window, font=('Times new roman', 10))
entry1.place(x=150, y=60)
entry2 = Entry(window, font=('Times new roman', 10,), show = "●")
entry2.place(x=150, y=85)

login_button = Button(window, text= "Login", bg = "#707bab", fg = "white", font= ('Times new roman', 10), command = login) 
login_button.place(x= 150, y= 125)

def home_page():
    home = Toplevel()
    home.geometry("420x420")
    home.title("Dear Diary,")
    home.configure(bg= "#373b4d")

    def book():
        home.destroy()
        book_page()

    image_path = "plus.png"  # Replace with your image file
    try:
        original_image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        home.destroy()
        exit()

    # Optional: Resize the image
    resized_image = original_image.resize((150 ,140)) # Resize to 300x200 pixels

    # Convert the image for Tkinter
    tk_image = ImageTk.PhotoImage(resized_image)

    # Create a Label widget to display the image
    image_button = Button(home, image=tk_image, bg="#373b4d", activebackground="#373b4d", border=0, highlightthickness=0, highlightbackground="#373b4d", command = book)
    image_button.place(relx=0.0, rely=0.0, anchor="nw")

    # Keep a reference to the image to prevent garbage collection
    image_button.image = tk_image

    new_book = Label(home, text= "New Book", bg = "#373b4d", fg = "white", font= ('Times new roman', 15))
    new_book.place(x=33 , y= 100)

def book_page():
    book = Toplevel()
    book.geometry("420x420")
    book.title("Dear Diary,")
    book.configure(bg= "#373b4d")

    design_page = Label(book, text='Design your book!', bg = "#373b4d", fg = "white", font= ('Times new roman', 15))
    design_page.place(relx=0.5, y=20, anchor="center") 

    options = ['Time new roman', ' arial', 'Calibri', 'Georgia']

    clicked = StringVar()
    clicked.set ('Times New Roman')

    drop = OptionMenu(book, clicked, *options)
    drop.place(relx=0.5, y=100, anchor="center")

    
    options = ['red', ' green', 'yellow', 'blue', 'purple', 'pink', 'white', 'black']

    clicked1 = StringVar()
    clicked1.set ('red')

    drop = OptionMenu(book, clicked1, *options)
    drop.place(relx=0.5, y=135 ,anchor="center") 

    title_label = Label(book, text= "Book Title: ", bg = "#373b4d", fg = "white", font= ('Times new roman', 10))
    title_label.place(x =70, y=60)


    entry3=Entry(book, font=('Times new roman', 10))
    entry3.place(x =150, y = 60)

    preview_label = Label(book, bg="#373b4d")  # will hold preview image
    preview_label.place(relx=0.5, y=250, anchor="center")

    def choose_icon():
        filepath = filedialog.askopenfilename(
            title="Choose Book Icon",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )

        if not filepath:
            return  # user cancelled

        # Load the image
        image = Image.open(filepath)

        # Resize it
        resized = image.resize((120, 120))  # adjust size as needed

        # Convert to Tkinter image
        tk_img = ImageTk.PhotoImage(resized)

        # Display the preview
        preview_label.config(image=tk_img)
        preview_label.image = tk_img  # prevent garbage collection

        # store path globally or inside an object if needed
        window.book_selected_icon_path = filepath

    # Button to choose icon
    icon_button = Button(
        book, text="Choose Book Icon", bg="#ffffff", fg="black",
        font=('Times new roman', 10), command=choose_icon
    )
    icon_button.place(relx=0.5, y=170, anchor="center")

    def design():
        font = clicked.get()
        colour =  clicked1.get()
        title = entry3.get()
        
        if font == "" and colour == "" and title == "":
            messagebox.showinfo( "Save Failed","Blanks are not allowed")
            return

        # save values
        window.saved_title = title
        window.saved_font = font
        window.saved_colour = colour

        messagebox.showinfo("Info Saved", "Curating your diary now.")

        book.destroy()
        diary()   # now calls the real diary()

    save_button = Button(book, text= "Save", bg = "#ffffff", fg = "black", font= ('Times new roman', 10), command = design) 
    save_button.place(x=300, y=250)

    def diary():
        diary_win = Toplevel()
        diary_win.geometry("420x420")
        diary_win.title(window.saved_title)
        diary_win.configure(bg="#373b4d")

        text = tk.Text(diary_win, width=40, height=20)
        text.pack()
        
        text.configure(
            bg=window.saved_colour,
            font=(window.saved_font, 12)
        )


window.mainloop() 