import hashlib
import jwt
import re
import os
import screens as screen
import constants

dirname = os.path.dirname(os.path.realpath(__file__))


# Register event
  
def event_register(
    root,
    canvas,
    username,
    password,
    elements,
    menu,
    ):

    # check if user already exist in Database.txt

    fileDatabaza = open(dirname + '/Database.txt', 'r')

    while True:
        line = fileDatabaza.readline()
        if not line:
            fileDatabaza.close()
            break
        txt = line.strip()
        x = re.search('^' + username + "\|\|\|", txt)
        if x:
            screen.show_info('User already exist!')
            return False
        if (password_check(password)):
            screen.show_info('Enter a valid password!\nPassword length must be at least 6,should contain at least one numeral\nPassword must contain at least one uppercase and one lowercase letter\nPassword should have at least one of the symbols $@#')
            return False
    
    Hashpassword = hashlib.sha256(password.encode()).hexdigest()
    f = open(dirname + '/Database.txt', 'a+')
    f.write('\n' + username + '|||' + Hashpassword)
    f.close()
    screen.clear_elements(elements)
    screen.online_screen(root, canvas, username, menu)

def event_logout(root, canvas, elements):
    screen.clear_elements(elements)
    menu = screen.menu(root, canvas)
    screen.loginP(root, canvas, menu)

def copy_to_clipboard(root, text):
    root.clipboard_clear()
    root.clipboard_append(text)

#login Event

def loginE(
    root,
    canvas,
    username,
    password,
    elements,
    menu,
    ):

    #check if the Hash Value is in the database

    Hashpassword = hashlib.sha256(password.encode()).hexdigest()
    fileDatabaza = open(dirname + '/Database.txt', 'r')
    while True:
        line = fileDatabaza.readline()
        if not line:
            fileDatabaza.close()
            screen.show_info('Wrong Username or Password!')
            break
        txt = line.strip()
        x = re.search('^' + username + "\|\|\|" + Hashpassword, txt)
        if x:
            screen.clear_elements(elements)
            screen.online_screen(root, canvas, username, menu)
            break

def event_register_handler(root, canvas):
    canvas.delete('all')
    menu = screen.menu(root, canvas)
    screen.regjisterP(root, canvas, menu)

def loginE_handler(root, canvas):
    canvas.delete('all')
    menu = screen.menu(root, canvas)
    screen.loginP(root, canvas, menu)

def Token_event_handler(root, canvas):
    canvas.delete('all')
    menu = screen.menu(root, canvas)
    screen.tokenL(root, canvas, menu)

# token event 

def token_event(
    root,
    canvas,
    token,
    elements,
    menu,
    ):

    try:
        TokenDecoded = jwt.decode(token.strip(), constants.TOKEN_CODE,
                                  algorithms=[constants.ALGORITHM])
        screen.clear_elements(elements)
        screen.online_screen(root, canvas, TokenDecoded['Username'],
                             menu)
    except jwt.ExpiredSignatureError:
        screen.show_info("Token expired. Get new one")

    except jwt.InvalidTokenError:
        screen.show_info("Invalid Token")

#Function for checking if user types the coorect password

def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = False
      
    if len(passwd) < 6:
        val = True
          
    if not any(char.isdigit() for char in passwd):
        val = True
          
    if not any(char.isupper() for char in passwd):
        val = True
          
    if not any(char.islower() for char in passwd):
        val = True
          
    if not any(char in SpecialSym for char in passwd):
        val = True
    
    return val
