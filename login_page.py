from tkinter import *

def entry_box(parent):
    global entry_box
    entry_box=Entry(parent,width=100)
    entry_box.pack(anchor=NW,padx=20)

def entry_box1(parent):
    global entry_box1
    entry_box1=Entry(parent,width=100)
    entry_box1.pack(anchor=NW,padx=20)



def buttonPressed():
    global entry_box
    text1=entry_box.get()
    text2=entry_box1.get()
    print("\nYour ENTRIES are as follows :- ")
    print(f"Username : {text1} \nPassword : {text2}")

    root.quit()


def main():
    global root
    root=Tk()
    root.title("Login Page")
    root.geometry("300x300")
    root.config(bg='yellow')
    root.maxsize(300,300)
    root.minsize(300,300)

    head=Label(root,text="Login Page ",bg='cyan')
    head.config(font=('Helvetica bold',16))
    head.pack(side=TOP,fill=X,ipadx=10)


    user=Label(root,text="Enter your Username :-")
    user.pack(anchor=NW, padx=10,pady=10)
    entry_box(root)




    password=Label(root,text="Enter your Password :- ")
    password.pack(anchor=NW,padx=10,pady=10)
    entry_box1(root)


    #Submit Button 
    submit_button=Button(root,text="Submit",command=buttonPressed)
    submit_button.pack(anchor=CENTER,pady=20)


    root.mainloop()

main()






