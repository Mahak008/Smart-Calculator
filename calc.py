from tkinter import *
import math
from pygame import mixer
import speech_recognition

mixer.init()

def click(value):
    ex = entryField.get()
    ans = ''

    try:
        if(value == 'C'):
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)

        elif(value == 'CE'):
            entryField.delete(0, END)

        elif (value == '√'):
            ans = math.sqrt(eval(ex))

        elif (value == 'π'):
            ans = math.pi

        elif (value == 'cos'):
            ans = math.cos(math.radians(eval(ex)))
        
        elif (value == 'tan'):
            ans = math.tan(math.radians(eval(ex)))

        elif (value == 'sin'):
            ans = math.sin(math.radians(eval(ex)))

        elif (value == '1/x'):
            ans = 1/eval(ex)

        elif (value == 'cosh'):
            ans = math.cosh(eval(ex))
        
        elif (value == 'tanh'):
            ans = math.tanh(eval(ex))

        elif (value == 'sinh'):
            ans = math.sinh(eval(ex))

        elif(value == chr(8731)):
            ans = eval(ex)**(1/3)

        elif(value == 'x\u02b8'):
            ans = entryField.insert(END, '**')
            return
            
        elif(value == 'x\u00b3'): 
            ans = eval(ex)**3

        elif(value == 'x\u00b2'):
            ans = eval(ex)**2

        elif(value == 'ln'):
            ans = math.log2(eval(ex))

        elif(value == 'deg'):
            ans = math.degrees(eval(ex))

        elif(value == 'rad'):
            ans = math.radians(eval(ex))

        elif(value == 'e'):
            ans = math.e
        
        elif(value == 'log'):
            ans = math.log10(eval(ex))

        elif(value == 'x!'):
            ans = math.factorial(eval(ex))

        elif(value == chr(247)):
            entryField.insert(END, '/')
            return 

        elif(value == '='):
            ans = eval(ex)
        
        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, ans)

    except SyntaxError:
        pass

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    l = math.lcm(a,b)
    return l

def hcf(a,b):
    h = math.gcd(a,b)
    return h

operations = {'ADD':add, 'ADDITION': add, 'SUM':add, 'PLUS':add, 
             'SUBTRACT':sub, 'SUBTRACTION':sub, 'DIFFERENCE':sub, 'MINUS':sub, 
             'PRODUCT':mul, 'MULTIPLY':mul, 'MULTIPLICATION':mul,
             'DIVISION':div, 'DIVIDE':div,
             'LCM':lcm, 'HCF':hcf,
             'MOD':mod, 'REMAINDER':mod, 'MODULUS':mod}

def findNumbers(t):
    l = []
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play() 
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(m, duration=0.2)
            voice = sr.listen(m)
            text = sr.recognize_google(voice)
            
            mixer.music.load('music2.mp3')
            mixer.music.play() 
            text_list = text.split(' ')
            # print(text_list)
            
            for word in text_list:
                if(word.upper() in operations.keys()):
                    l = findNumbers(text_list)
                    res = operations[word.upper()](l[0], l[1])
                    print(l)
                    entryField.delete(0, END)
                    entryField.insert(END, res)

                else:
                    pass
                
        except:
            pass

#Helps to create GUI of the window
root = Tk()

# method of Tk class to give title to window
root.title("Smart Calculator") 

# sets background color of the window
root.config(bg='gray')

# defines height and width of the window
root.geometry('715x508+100+100')

#logo
logoImage = PhotoImage(file = 'logo.png')
logoLabel = Label(root, image=logoImage, bg='gray')
logoLabel.grid(row=0, column=0)

# designing the input field
entryField = Entry(root, font = ('arial', 20, 'bold'), bg = 'white', fg='black', bd=10, relief =SUNKEN, width=30)

entryField.grid(row=0, column=0, columnspan=8)

#Microphone
micImage = PhotoImage(file = 'microphone.png')
micButton = Button(root, image=micImage, bd=0, bg='gray', activebackground='gray', command=audio)
micButton.grid(row=0, column=7)

button_text_list = ["C", "CE","√","+","π","cos", "tan", "sin", "1", "2", "3", "-", "1/x", "cosh", "tanh", "sinh", "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00b3", "x\u00b2", "7", "8", "9", chr(247), "ln", "deg", "rad", "e", ".", "0", "%", "=", "log", "(", ")", "x!"]

rowValue = 1
colValue = 0

# loop to create buttons

for i in button_text_list:
    button = Button(root, width=5, height=2, bd=4, relief=SUNKEN, text= i, bg='gray', fg='white', font = ('arial', 18, 'bold'), activebackground='white', activeforeground='black', command=lambda button = i: click(button))
    button.grid(row= rowValue, column = colValue, pady=1)
    colValue += 1
    if(colValue > 7):
        rowValue+=1
        colValue = 0

# run window
root.mainloop()