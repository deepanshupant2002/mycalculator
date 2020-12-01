import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk()
root.title("Calculator")

v= tk.StringVar()
root.geometry("400x300")

screen=""
def cmd(sign):
        global screen
        screen = screen + str(sign)
        v.set(screen)

def equal():
        try:
                global screen
        
                total = str(eval(screen))
        
                v.set(total)
        
                # screen = ""
        
        except:
                v.set("Abe Saale")

                screen =""

def clear():
        global screen
        display_screen.delete(0,END)
        screen = ""
        display_screen.insert(0,"0")

def fundelete():
        global screen
        vr=display_screen.get()
        vr=vr[0:len(vr)-1]
        # length = len(display_screen.get())
        display_screen.delete(0,END)
        screen = vr
        display_screen.insert(0,vr)

display_screen = ttk.Entry(root,font=("verdana",23),justify=RIGHT,textvariable= v)
display_screen.grid(row=0,columnspan=40,ipady=5)
display_screen.insert(0,"0")

seven_button = Button(root,text="7",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(7))
seven_button.grid(row=3,column=0,pady=5)

eight_button = Button(root,text="8",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(8))
eight_button.grid(row=3,column=1,pady=5)

nine_button = Button(root,text="9",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(9))
nine_button.grid(row=3,column=2,pady=5,padx=5)

ac_button = Button(root,text="AC",height=2,width=12,relief="solid",activebackground="brown",activeforeground="white",command=lambda:clear())
ac_button.grid(row=3,column=3,pady=5)

four_button = Button(root,text="4",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(4))
four_button.grid(row=4,column=0,pady=5)

five_button = Button(root,text="5",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(5))
five_button.grid(row=4,column=1,pady=5)

six_button = Button(root,text='6',height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(6))
six_button.grid(row=4,column=2,pady=5,padx=5)

divide_button = Button(root,text="÷",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd("/"))
divide_button.grid(row=4,column=3,pady=5)

one_button = Button(root,text="1",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(1))
one_button.grid(row=5,column=0,pady=5,padx=5)

two_button = Button(root,text="2",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(2))
two_button.grid(row=5,column=1,pady=5)

three_button = Button(root,text="3",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(3))
three_button.grid(row=5,column=2,pady=5,padx=5)

multiply_sign = Button(root,text="×",height=2,width=12,relief="solid",activebackground="brown",activeforeground="white",command=lambda:cmd("*"))
multiply_sign.grid(row=5,column=3,pady=5)

zero_button = Button(root,text="0",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd(0))
zero_button.grid(row=6,column=1,pady=5)

clear_button = Button(root,text="Clear",height=2,width=12,relief="solid",activebackground="brown",activeforeground="white",command=lambda:fundelete())
clear_button.grid(row=6,column=2,pady=5,padx=5)

decimal_button = Button(root,text=".",height=2,width=12,relief="solid",activebackground="orange",activeforeground="white",command=lambda:cmd("."))
decimal_button.grid(row=6,column=0,pady=5)

sub_button = Button(root,text="-",height=2,width=12,relief="solid",activebackground="brown",activeforeground="white",command=lambda:cmd("-"))
sub_button.grid(row=6,column=3,pady=5)

equal_button = Button(root,text="=",height=2,width=12,relief="solid",activebackground="cyan",activeforeground="white",command=lambda:equal())
equal_button.grid(row=7,column=2)

add_button = Button(root,text="+",height=2,width=12,relief="solid",activebackground="brown",activeforeground="white",command=lambda:cmd("+"))
add_button.grid(row=7,column=3) 

per_button = Button(root,text="%",height=2,width=12,relief="solid",activebackground="brown",activeforeground="white",command = lambda:cmd("%"))
per_button.grid(row=7,column=0)


root.mainloop()
