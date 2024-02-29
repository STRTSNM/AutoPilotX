import eel, time
import json
l=[]

eel.init('src')
@eel.expose
def appendlist(bt,bv):
    l.append((bt,bv))
    print(l)

@eel.expose
def execution():
    global l
    for i in l:
        if i[0]=='commandButton':
            print("Running command", i[1])
        if i[0]=='keyboardButton':
            print("Typing in keyboard: ", i[1])
        if i[0]=='mouseButton':
            print("Moving mouse to :", i[1])
eel.start('index.html')

