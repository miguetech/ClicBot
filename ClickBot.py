from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import KeyCode, Controller, Key
from pynput import keyboard
from tkinter import *
from tkinter import *
import time

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()



# Keyboard = Controller()

# COMBINATIONS = [
#     {keyboard.Key.ctrl_l, keyboard.KeyCode(char = 'x')},
#     {keyboard.Key.shift, keyboard.KeyCode(char = 'X')},
#     {keyboard.Key.ctrl, keyboard.KeyCode(char = 'z')},
#     {keyboard.Key.ctrl, keyboard.KeyCode(char = 'Z')},
#     {keyboard.Key.ctrl, keyboard.KeyCode(char = 'j')},
#     {keyboard.Key.ctrl, keyboard.KeyCode(char = 'J')}
#     ]

# with Keyboard.pressed(Key.ctrl):
#     with Keyboard.pressed(Key.alt):
#         Keyboard.press('v')

# current = set()

# def execute(current):
#     print("hola")

# def on_press(key):
#     if any([key in COMBO for COMBO in COMBINATIONS]):
#         current.add(key)
#         print(current)
#         if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
#             execute(current)
#     if key == keyboard.Key.esc:
#         listener.stop()

# def on_release(key):
#     if any([key in COMBO for COMBO in COMBINATIONS]):
#         current.remove(key)


# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
        
signos = StringVar()

pantallaResp = Entry(miFrame,state = 'disabled', textvariable = signos)
pantallaResp.grid(row = 0, column = 1, padx = 10, columnspan = 4, ipady = 5)
pantallaResp.config(background = "blue", fg = "black", justify = "right")




class clickBot():
    
    def __init__(self):
        super().__init__()
        self.on_click_letf_pressed = False
        self.on_click_right_pressed = False 
        self.program_running = True
        self.running = False
    
    
    def save_click(self, saveClick = [], saveTime = []):
        self.saveClick
        self.saveTime
    
    def star_clicking(self):
        self.running = True
    
    def stop_clicking(self):
        self.program_running = False
    
    def exit_clicking(self):#stop all program 
        self.stop_clicking()
        self.program_running = False
        
    def run(self, Delay):
        while(self.program_running):
            if(running):
                
                time.sleep(Delay)
                
def hola(event):
    signos.set("(%s %s)" % (event.x, event.y))

botonStart= Button(miFrame, text = "Start ctrl+c", width = 10,command =lambda:numeroPulsado("1"))
botonStart.grid(row = 1, column = 1)

raiz.bind("<Control-Key-c>",hola)

botonStop= Button(miFrame, text = "Stop ctrl+d", width = 10,command =lambda:numeroPulsado("1"))
botonStop.grid(row = 1, column = 2)


raiz.mainloop()