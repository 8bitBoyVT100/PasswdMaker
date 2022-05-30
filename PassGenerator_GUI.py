from tkinter import *
import random

window = Tk()

app_width = 625
app_height = 400

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight() 
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)

window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
window.title("PasswordMaker v1.0")
window.minsize(app_width,app_height)
window.maxsize(app_width,app_height)


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "`~!@#$%^&*()-_=+[{]}\|;:,<.>/?"

# Chanage the font according your liking
myfont = 'CaskaydiaCove Nerd Font'
button_fsize = 15

def main(use_for, PassLen):
    passwd = "".join(random.sample(use_for, PassLen))
    # print("\nThe generated password: ", passwd)
    showPasswd.delete(0,END)
    showPasswd.insert(0, passwd)

def doubleCheck(use_for, myPassLen):
    if myPassLen == "":
        showMsg.config(text="Plz enter a length")
    if not use_for:
        showMsg.config(text="Plz choose an option")
    elif int(myPassLen) < 1 or int(myPassLen) > 50:
        showMsg.config(text="passwd range is between 1 - 50") 
    else:
        showMsg.config(text="")
        main(use_for, int(myPassLen))

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
    doubleCheck(use_for, myPassLen)

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
                        text="Generate",
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

showMsg = Label(window,font=(myfont,15),fg="red")
showMsg.place(x=10,y=300)

window.mainloop()