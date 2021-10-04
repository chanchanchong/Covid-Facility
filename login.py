import tkinter
from window2 import menu

#root=login page
#root1=menu
#rootp=patient form

#variables
root=None
userbox=None
passbox=None
topframe=None
bottomframe=None
frame3=None
login=None
#command for login button
def GET():
    global userbox,passbox,error
    S1=userbox.get()
    S2=passbox.get()
    if(S1=='admin' and S2=='1234567'):
        menu()
    elif(S1=='201012300' and S2=='aaaa'):
        menu()
    else:
        error=tkinter.Label(bottomframe,text="Wrong Id / Password \n TRY AGAIN",fg="red",font = ("Recursive", 11))
        error.pack()


#LOGIN PAGE WINDOW
def Entry():
    global userbox,passbox,login,topframe,bottomframe,image_1
    root = tkinter.Tk()
    root.geometry("280x250")
    topframe = tkinter.Frame(root)
    topframe.pack()
    bottomframe=tkinter.Frame(root)
    bottomframe.pack()
    heading = tkinter.Label(topframe, text="WELCOME TO COVID FACILITY",font = ("Recursive", 14, "bold"))
    username=tkinter.Label(topframe,text="USERNAME",font = ("Recursive", 11, "bold"))
    userbox = tkinter.Entry(topframe,font = ("Recursive", 11))
    password=tkinter.Label(bottomframe,text="PASSWORD",font = ("Recursive", 11, "bold"))
    passbox = tkinter.Entry(bottomframe,show="*",font = ("Recursive", 11))
    login = tkinter.Button(bottomframe, text="LOGIN", command=GET,font = ("Recursive", 11, "bold"))
    heading.pack()
    username.pack()
    userbox.pack()
    password.pack()
    passbox.pack()
    login.pack()
    root.title("DATABASE LOGIN")
    root.mainloop()

Entry()

