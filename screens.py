import tkinter as tk
import jwt
from typing import Literal
import constants
from tkinter import messagebox
import events as event
import tkinter.font as font
from time import time


def loginP(root, canvas, menu):

    myFont = font.Font(family='MS Sans Serif', size=11, weight='bold')
    myFont2 = font.Font(family='MS Sans Serif', size=14)
    myFont3 = font.Font(family='MS Sans Serif', size=14,weight='bold')
    myFont4=font.Font(size=16)
    
    usernameLabel = tk.Label(text='Username:',font=myFont3,bg=root['bg'])
    passwordLabel = tk.Label(text='Password:',font=myFont3,bg=root['bg'])
   
    # Field Entry

    Username = tk.Entry(root, width=17,justify="center",font=myFont2)
    Password = tk.Entry(root, show='*', width=15,justify="center",font=myFont4)
    LoginBTN = tk.Button(text='Login',height=1,font=myFont,borderwidth=5,
                         bg = "#008000", fg = "black",width=20, command=lambda : \
                         event.loginE(
            root,
            canvas,
            Username.get(),
            Password.get(),
            [usernameLabel, passwordLabel, Username, Password,
            LoginBTN],
            menu,
            ))
    root.bind('<Return>', lambda event=None: LoginBTN.invoke())

    # define placeholder

    Username.insert(0, 'Username')
    Password.insert(0, 'Password')

    # UI

    canvas.create_window(345, 180, window=usernameLabel)
    canvas.create_window(345, 250, window=passwordLabel)
    canvas.create_window(515, 180, window=Username)
    canvas.create_window(515, 250, window=Password)
    canvas.create_window(515, 320, window=LoginBTN)
    return [usernameLabel, passwordLabel, Username, Password, LoginBTN]


def regjisterP(root, canvas, menu):

    myFont = font.Font(family='MS Sans Serif', size=11, weight='bold')
    myFont2 = font.Font(family='MS Sans Serif', size=14)
    myFont3 = font.Font(family='MS Sans Serif', size=14,weight='bold')
    myFont4=font.Font(size=16)

    # labels

    usernameLabel = tk.Label(text='Username:',font=myFont3,bg=root['bg'])
    passwordLabel = tk.Label(text='Password:',font=myFont3,bg=root['bg'])

    # Field Entry

    Username = tk.Entry(root, width=17,justify="center",font=myFont2)
    Password = tk.Entry(root, show='*', width=15,justify="center",font=myFont4)
    RegisterBTN = tk.Button(text='Register',height=1,font=myFont,borderwidth=5,
                            bg = "#008000", fg = "black",width=20, command=lambda : \
                            event.event_register(
            root,
            canvas,
            Username.get(),
            Password.get(),
            [usernameLabel, passwordLabel, Username, Password,
            RegisterBTN],
            menu,
            ))
    root.bind('<Return>', lambda event=None: RegisterBTN.invoke())

    # define placeholder

    Username.insert(0, 'Username')
    Password.insert(0, 'Password')

    # UI
    canvas.create_window(345, 180, window=usernameLabel)
    canvas.create_window(345, 250, window=passwordLabel)
    canvas.create_window(515, 180, window=Username)
    canvas.create_window(515, 250, window=Password)
    canvas.create_window(515, 320, window=RegisterBTN)
    return [usernameLabel, passwordLabel, Username, Password,RegisterBTN]


def tokenL(root, canvas, menu):
    
    myFont = font.Font(family='MS Sans Serif', size=10, weight='bold')
    myFont2 = font.Font(family='MS Sans Serif', size=12)
    myFont3 = font.Font(family='MS Sans Serif', size=14,weight='bold')

    # labels

    tokenLabel = tk.Label(text='Token:',font=myFont3)

    # Field Entry

    Token = tk.Text(root, height=7, width=30,font=myFont2)
    TokenBTN = tk.Button(text='Login',height=1,font=myFont,borderwidth=5,
                         bg = "#008000", fg = "black",width=20, command=lambda : \
                         event.token_event(root, canvas, Token.get('1.0'
                         , 'end-1c'), [tokenLabel, Token, TokenBTN],
                         menu))
    root.bind('<Return>', lambda event=None: TokenBTN.invoke())

    # UI
    
    canvas.create_window(310, 170, window=tokenLabel)
    canvas.create_window(515, 217, window=Token)
    canvas.create_window(515, 320, window=TokenBTN)
    return [tokenLabel, Token, TokenBTN]


def menu(root, canvas):
    
    myFont = font.Font(family='Ubuntu', size=12, weight='normal')
    Login_with_password = tk.Button(text='Login with password',height=1,font=myFont,borderwidth=5,
                                    bg = "#248EB5", fg = "black",width=17, command=lambda : \
                                    event.loginE_handler(root,
                                    canvas))
  
    canvas.create_window(345, 90, window=Login_with_password)
    
    Login_with_token = tk.Button(text='Login with token',height=1,font=myFont,borderwidth=5,
                                    bg = "#248EB5", fg = "black",width=17,command=lambda : \
                                    event.Token_event_handler(root,
                                    canvas))

    canvas.create_window(515, 90, window=Login_with_token)
    
    Register_button = tk.Button(text='Register',height=1,font=myFont,borderwidth=5,
                                    bg = "#248EB5", fg = "black",width=17,command=lambda : \
                                    event.event_register_handler(root,
                                    canvas))
  
    canvas.create_window(685, 90, window=Register_button)
    return [Login_with_password, Login_with_token, Register_button]


def clear_elements(array):
    for x in array:
        x.destroy()


def online_screen(
    root,
    canvas,
    username,
    menu,
    ):
    clear_elements(menu)
    Token = jwt.encode({'Username': username,'exp': time() + 300},constants.TOKEN_CODE,
                         algorithm=constants.ALGORITHM)

    # labels

    myFont = font.Font(family='MS Sans Serif', size=10, weight='bold')
    myFont2 = font.Font(family='MS Sans Serif', size=12)
    myFont3 = font.Font(family='MS Sans Serif', size=14,weight='bold')

    usernameLabel = tk.Label(text='Username: ',font=myFont3)
    usernameLabelValue = tk.Label(text=username,font=myFont2)
    tokenLabel = tk.Label(text='Token: ',font=myFont3)
    tokenLabelValue = tk.Label(text=Token, wraplength=300,font=myFont2)

    # Field Entry

    clipboardBTN = tk.Button(text='Copy token',height=1,font=myFont,borderwidth=5,
                             bg = "#008000", fg = "black",width=20,command=lambda : \
                             event.copy_to_clipboard(root, Token))
    LogoutBTN = tk.Button(text='Logout',height=1,font=myFont,borderwidth=5,
                             bg = "#FF0000", fg = "black",width=10, command=lambda : \
                             event.event_logout(root, canvas, [
            usernameLabel,
            tokenLabel,
            tokenLabelValue,
            clipboardBTN,
            LogoutBTN,
            usernameLabelValue,
            ]))

    # UI

    canvas.create_window(330, 150, window=usernameLabel)
    canvas.create_window(550, 150, window=usernameLabelValue)
    canvas.create_window(350, 220, window=tokenLabel)
    canvas.create_window(550, 220, window=tokenLabelValue)
    canvas.create_window(550, 330, window=clipboardBTN)
    canvas.create_window(790, 30, window=LogoutBTN)
    return [usernameLabel,usernameLabelValue,tokenLabel,tokenLabelValue,
            clipboardBTN,LogoutBTN]


def show_info(message):
    messagebox.showerror('Error', message)
    return False