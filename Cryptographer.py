from tkinter import *

# Functions
def encrypt(string):

    New_Value_Entry.delete(0, END)

    cipher = ''

    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + int(Crypto_Value.get()) - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + int(Crypto_Value.get()) - 97) % 26 + 97)

    New_Value_Entry.insert(0, cipher)

def decrypt(string):

    New_Value_Entry.delete(0, END)

    cipher = ''

    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) - int(Crypto_Value.get()) - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - int(Crypto_Value.get()) - 97) % 26 + 97)

    New_Value_Entry.insert(0, cipher)

# Main Screen
window = Tk()
window.title("Customizable Cryptographer")
window['bg'] = 'Black'

# Frames
Title_Frame = Frame(window, bg="Black")
Title_Frame.pack()

Content_Frame = Frame(window, bg="Black")
Content_Frame.pack()

# Labels
Title_Label = Label(Title_Frame, text="Customizable Cryptographer", bg="Black", fg="White", font=("Arial", 18))
Title_Label.grid(sticky=N)

Number_Label = Label(Content_Frame, text="Number", bg="Black", fg="White", font=("Arial", 16))
Number_Label.grid(row=1, column=0, sticky=W, padx=15)

Original_Value_Label = Label(Content_Frame, text="Original Value", bg="Black", fg="White", font=("Arial", 16))
Original_Value_Label.grid(row=2, column=0, sticky=W, padx=15)

New_Value_Label = Label(Content_Frame, text="New Value", bg="Black", fg="White", font=("Arial", 16))
New_Value_Label.grid(row=3, column=0, sticky=W, padx=15)

# Dummy Label
Top_Dummy_Label = Label(Content_Frame, bg="Black", fg="White")
Top_Dummy_Label.grid(row=0)

Middle_Dummy_Label = Label(Content_Frame, bg="Black", fg="White")
Middle_Dummy_Label.grid(row=4)

Bottom_Dummy_Label = Label(Content_Frame, bg="Black", fg="White")
Bottom_Dummy_Label.grid(row=6)

# Entry
Crypto_Value = StringVar()
Crypto_Value_Entry = Entry(Content_Frame, textvariable=Crypto_Value)
Crypto_Value_Entry.grid(row=1, column=1, sticky=S, ipadx=100, ipady=5, padx=15)

Original_Value = StringVar()
Original_Value_Entry = Entry(Content_Frame, textvariable=Original_Value)
Original_Value_Entry.grid(row=2, column=1, sticky=S, ipadx=100, ipady=5)

New_Value = StringVar()
New_Value_Entry = Entry(Content_Frame, textvariable=New_Value)
New_Value_Entry.grid(row=3, column=1, sticky=S, ipadx=100, ipady=5)

# Buttons
Decryption_Button = Button(Content_Frame, text="Decrypt", bg="Black", fg="White", height=1, width=15, font=("Arial", 16),
                           command=lambda: decrypt(Original_Value.get()))
Decryption_Button.grid(row=5, column=0, sticky=E, padx=15)

Encryption_Button = Button(Content_Frame, text="Encrypt", bg="Black", fg="White", height=1, width=15, font=("Arial", 16),
                           command=lambda: encrypt(Original_Value.get()))
Encryption_Button.grid(row=5, column=1, sticky=E, padx=15)

Content_Frame.mainloop()
