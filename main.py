import tkinter as tk
from tkinter import *
import webbrowser


root = tk.Tk()
root.title("Regular Expression Converter/Checker")

canvas = tk.Canvas(root, height=700, width=1200, bg='#A57B75')
canvas.pack()

click_btn = PhotoImage(file='submit.gif')
dfa_btn1 = PhotoImage(file='dfabutton.png')
cfg_btn1 = PhotoImage(file='cfgbutton.png')
pda_btn1 = PhotoImage(file='pdabutton.png')
chk_btn1 = PhotoImage(file='checkbutton.GIF')
smb_btn1 = PhotoImage(file='submitbutton.GIF')


def clearFrame():
    for widget in canvas.winfo_children():
        widget.destroy()

    frame.pack_forget()

Fonttext = ("Helvetica", 14, "bold")

dog = tk.Entry(root,font = ('Helvetica 14'))
dog.pack()
dog.place(x=50,y=330, width=300,height=30)

cat = tk.Entry(root,font = ('Helvetica 14'))
cat.pack()
cat.place(x=550,y=290, width=450,height=100)

dog2 = tk.Entry(root,font = ('Helvetica 14'))
dog2.pack()
dog2.place(x=50,y=520, width=300,height=30)

cat2 = tk.Entry(root,font = ('Helvetica 14'))
cat2.pack()
cat2.place(x=550,y=480, width=450,height=100)


#Image section for the converted DFA,CFG,PDA
def img1():
    r = Toplevel()
    r.title("PDA")

    canvas = Canvas(r,  height=500 , width=1000, bg='#A57B75')
    canvas.pack()

    dfa_image = PhotoImage(file='dfa1.gif')
    canvas.create_image(20 , 20 , anchor=NW, image=dfa_image)
    canvas.dfa_image = dfa_image
    r.mainloop()

def img2():
    r = Toplevel()
    r.title("CFG")

    canvas = Canvas(r, height=250, width=600, bg='#A57B75')
    canvas.pack()

    dfa_image = PhotoImage(file='cfg1.gif')
    canvas.create_image(20 , 20 , anchor=NW, image=dfa_image)
    canvas.dfa_image = dfa_image
    r.mainloop()

def img3():
    r = Toplevel()
    r.title("PDA")

    canvas = Canvas(r, height=1000, width=1000, bg='#A57B75')
    canvas.pack()

    dfa_image = PhotoImage(file='pda1.gif')
    canvas.create_image(20 , 20 , anchor=NW, image=dfa_image)
    canvas.dfa_image = dfa_image
    r.mainloop()

def img4():
    r = Toplevel()
    r.title("DFA")

    canvas = Canvas(r, height=700, width=1000, bg='#A57B75')
    canvas.pack()

    dfa_image = PhotoImage(file='dfa2.gif')
    canvas.create_image(20 , 20 , anchor=NW, image=dfa_image)
    canvas.dfa_image = dfa_image
    r.mainloop()

def img5():
    r = Toplevel()
    r.title("CFG")

    canvas = Canvas(r, height=225 , width=625, bg='#A57B75')
    canvas.pack()

    dfa_image = PhotoImage(file='cfg2.gif')
    canvas.create_image(20 , 20 , anchor=NW, image=dfa_image)
    canvas.dfa_image = dfa_image
    r.mainloop()

def img6():
    r = Toplevel()
    r.title("PDA")

    canvas = Canvas(r,  height=700 , width=1000, bg='#A57B75')
    canvas.pack()

    dfa_image = PhotoImage(file='pda2.gif')
    canvas.create_image(20 , 20 , anchor=NW, image=dfa_image)
    canvas.dfa_image = dfa_image
    r.mainloop()

def string_checker1():
    s = dog.get().lower()
    count = 0
    if s[:2] == 'aa' or s[:2] == 'bb':
        count = count + 1

    if s[-2:] == 'aa':
        count = count + 1
        if any(x in s[2:-2] for x in ['a', 'b', 'a', 'ba']):
            count = count + 1

    elif s[-1] == 'a' or s[-1] == 'b':
        count = count + 1
        if any(x in s[2:-1] for x in ['a', 'b', 'a', 'ba']):
            count = count + 1

    if count == 3:
        for widget in canvas.winfo_children():
            widget.destroy()
        cat.delete(0, END)
        cat.insert (INSERT, f'Your string {s}, is valid')
        return f'Your string is {s}, is valid'
    else:
        for widget in canvas.winfo_children():
            widget.destroy()
        cat.delete(0, END)
        cat.insert (INSERT, f'Your string {s}, is not valid')
        return f'Your string is {s}, is not valid'


def random_string(length, letters):
    return ''.join(random.choice(letters) for i in range(length))

def clearEntryInput():
    dog.delete(0, END)
    cat.delete(0, END)
    dog2.delete(0, END)
    cat2.delete(0, END)

def string_checker2():
    s = dog2.get().lower()
    count = 0
    if s[:3] == '101' or s[:3] == '100' or s[:3] == '111' or s[0] == '1' or s[0] == '0' or s[:2] == '11':
        count = count + 1

    if s[-3:] == '111' or s[-3:] == '000' or s[-3:] == '101' or s[-1] == '1' or s[-1] == '0':
        count = count + 1

    if count == 2:
        if any(x in s for x in ['111', '000', '101']):
            for widget in canvas.winfo_children():
                widget.destroy()
            cat2.delete(0, END)
            cat2.insert(INSERT, f'Your string {s}, is valid')
            return f'Your string is {s}, is valid'
        else:
            for widget in canvas.winfo_children():
                widget.destroy()
            cat2.delete(0, END)
            cat2.insert(INSERT, f'Your string {s}, is not valid')
            return f'Your string {s}, is not valid'

#texts
word1 = tk.Label(root, font = Fonttext, text = "1.) REGULAR EXPRESSION: ( aa + bb ) ( a + b )* ( a + b + ab + ba ) ( a + b + ab + ba )* ( aa + bab )* ( a + b + aa ) ( a + b + bb + aa )* ", bg='#A57B75', fg='#ffffff').place(x=5,y=25)
word2 = tk.Label(root, font = Fonttext, text = "2.) REGULAR EXPRESSION: ( ( 101 + ( 111 )* + 100 ) + ( 1 + 0 + 11 )* ) ( 1 + 0 + 01 )* ( 111 + 000 + 101 ) ( 1 + 0 )*", bg='#A57B75', fg='#ffffff').place(x=5,y=150)
word3 = tk.Label(root, font = Fonttext, text ="1. Input strings to check for first regular expression ", bg='#A57B75', fg='#ffffff').place(x=10,y=290)
word4 = tk.Label(root, font = Fonttext, text ="2. Input strings to check for second regular expression", bg='#A57B75', fg='#ffffff').place(x=10,y=480)


#Buttons for the converter for dfa,cfg,pda
reg1convert1= Button(root, image=dfa_btn1, text = "DFA",command= img1).place(x=125,y=65)
reg1convert2= Button(root, image=cfg_btn1, text = "CFG",command= img2).place(x=350,y=65)
reg1convert3= Button(root, image=pda_btn1, text = "PDA",command= img3).place(x=575,y=65)

reg2convert1= Button(root, image=dfa_btn1, text = "DFA",command= img4).place(x=125,y=200)
reg2convert2= Button(root, image=cfg_btn1, text = "CFG",command= img5).place(x=350,y=200)
reg2convert3= Button(root, image=pda_btn1, text = "PDA",command= img6).place(x=575,y=200)

#button for string checker 1
but = Button(root, image=chk_btn1, text="Check1", command=string_checker1)
but.pack()
but.place(x=50,y=380)

but2 = Button(root, image=chk_btn1, text="Check2", command=string_checker2)
but2.pack()
but2.place(x=50,y=570)

clear_output = Button(root, image=smb_btn1, text="Clear", command=clearEntryInput)
clear_output.pack()
clear_output.place(x=170,y=380)

clear_output2 = Button(root, image=smb_btn1, text="Clear", command=clearEntryInput)
clear_output2.pack()
clear_output2.place(x=170,y=570)

def open_url(url):
   webbrowser.open_new_tab(url)


Label1 = Label(root, font=Fonttext,text="ANGBABANAL © Software 2022", bg='#A57B75', fg='#ffffff')
Label1.pack()
Label1.place(x=600,y=680, anchor='c')
url = 'https://www.youtube.com/watch?v=o-YBDTqX_ZU&ab_channel=MusRest'
Label1.bind("<Button-1>", lambda e:open_url(url))

Label2 = Label(root, font=Fonttext,text="Click to check User Manual", bg='#A57B75', fg='#ffffff')
Label2.pack()
Label2.place(x=1200,y=700, anchor='se')
url2 = 'https://docs.google.com/document/d/1Qtg_yIyBJtAJk6NxsUDbT2RnpCJV5YWwKSKscXjKbTY/edit?usp=sharing'
Label2.bind("<Button-1>", lambda e:open_url(url2))
root.mainloop()