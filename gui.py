from tkinter import *
import os

def check_database():
    username=name.get()
    password=passwd.get()
    Label(window,textvariable=error).place(x=110,y=190)
    if(len(username)<8 or len(password)<8):
        error.set('Username or password length not satisfied')
        
        #error.set('')
        return
    else:
        error.set("")
    cmd = '.\db check %s %s'%(username,password)
    print(cmd)
    result = os.system(cmd)

    login=Tk()
    login.geometry('500x500')
    b = Button(login,bd='1',text='Exit window',command=login.destroy).place(x=0,y=0)
   
    
    if(result==1):
            Label(login,text='Login successfull').place(x=250,y=250)
    else:
        Label(login,text='Login failed').place(x=250,y=250)
    login.mainloop()


def set_database():
    username=name.get()
    password=passwd.get()
    print(username,password)
    cmd = '.\db set %s %s'%(username,password)
    print(cmd)
    result = os.system(cmd)

    sign=Tk()
    sign.geometry('500x500')
    b = Button(sign,bd='1',text='Login',command=sign.destroy).place(x=0,y=0)
    
    
    if(result==1):
        Label(sign,text='Sign Up successfull').place(x=250,y=250)
    elif(result==-1):
        Label(sign,text='Username already exists').place(x=250,y=250)
    else:
        Label(sign,text='Sign Up failed').place(x=250,y=250)
    sign.mainloop()

        

        





    
window = Tk()


login_message=StringVar()
signup_message=StringVar()
signup_error=StringVar()
signup_username=StringVar()
new_password=StringVar()
error = StringVar()
name=StringVar()
passwd=StringVar()

window.geometry('500x500')
b = Button(window,bd='1',text='Exit window',command=window.destroy).place(x=0,y=0)

user_name = Label(window,text='Username : ').place(x=100,y=100)
password = Label(window,text='Password : ').place(x=100,y=130)

username_entry = Entry(window,textvariable=name).place(x=170,y=100)
password_entry = Entry(window,textvariable=passwd,show='*').place(x=170,y=130)

login_button = Button(window,text='Login',command=check_database).place(x=150,y=160)
signup_button = Button(window,text='Sign Up',command=set_database).place(x=210,y=160)


window.mainloop()