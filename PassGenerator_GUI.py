from tkinter import *
import random

window = Tk()
window.geometry("625x400")
window.title("PasswordMaker v0.1")
window.minsize(625,400)
window.maxsize(625,400)


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "`~!@#$%^&*()-_=+[{]}\|;:,<.>/?"

# Chanage the font according your liking
myfont = 'CaskaydiaCove Nerd Font'
button_fsize = 15

def main(use_for, PassLen=0):
    passwd = "".join(random.sample(use_for, int(PassLen)))
    # print("\nThe generated password: ", passwd)
    showPasswd.delete(0,END)
    showPasswd.insert(0, passwd)

def CheckForCheck(myPassLen):
    use_for = ""
    if a.get() == 1:
        use_for = use_for + lower_case
    if b.get() == 1:
        use_for = use_for + upper_case
    if c.get() == 1:
        use_for = use_for + numbers
    if d.get() == 1:
        use_for = use_for + symbols
    main(use_for, myPassLen)

def SubButton():
    myPassLen = PLength.get()
    CheckForCheck(myPassLen)

myLabel = Label( window,
                 text="Enter the length of the password : ",
                 font=(myfont,15),
                )
myLabel.pack()
            
PLength = Entry(    window,
                    width=5,
                    font=(myfont,15)
                )
PLength.pack()

submit_button = Button( window,
                        text="submit",
                        command=SubButton,
                        font=(myfont,0)
                        )
submit_button.place(x=250,y=200)

# Defining variable type
a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()

lcase_button = Checkbutton(  window,
                             text="Lowercase",
                             variable=a,
                            #  command=CheckForCheck,
                             font=(myfont,button_fsize),
                            )
lcase_button.place(x=0,y=60)

ucase_button = Checkbutton(  window,
                             text="Uppercase",
                             variable=b,
                             font=(myfont,button_fsize)
                            )
ucase_button.place(x=0,y=90)

num_button = Checkbutton(   window,
                            text="Numbers  ",
                            variable=c,
                            font=(myfont,button_fsize),    
                        )
num_button.place(x=0,y=120)

sym_button = Checkbutton(   window,
                            text="Symbols  ",
                            variable=d,
                            font=(myfont,button_fsize)
                        )
sym_button.place(x=0,y=150)

showPasswd = Entry(window,font=(myfont,15), width=50)
showPasswd.place(x=10,y=250)

window.mainloop()