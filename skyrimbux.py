"""
Copyright Jacob Rice 2020
skyrimbux
contact me @ jwr5ky@virginia.edu to hire me or to shame me or to shar memes, your choice, really
"""
import tkinter as tk
from playsound import playsound
import os
import sys
window = tk.Tk()
window.title("skyrimbux")
#initializing all labels
nwLabel = tk.Label(window,text="Enter your person's net worth")
outLabel = tk.Label(window)
itemLabel = tk.Label(window,text="What item is your person buying?")
#initializing entry fields
itemEntry = tk.Entry(window)
nwEntry = tk.Entry(window)
#initializing calc button
calcButton = tk.Button(window,text="Calculate")
mercyMeter = 0
#defining event methods
def getValue(item):
    itemFile = open('finalItems.txt','r')
    for line in itemFile:
        splitline = line.split('\t')
        if splitline[1].lower() == item.lower() and splitline[1] != 'Name':
            return int(splitline[3])
    return 0
        
def calc():
    
    item = itemEntry.get()
    nw = nwEntry.get()
    if item != '' and nw != '':
        try:
            inSeptums = int(nw)/2.4
            itemVal = getValue(item)
            numItems = inSeptums / itemVal
            outLabel.configure(text="Your person can purchase "+str(round(numItems))+" "+str(item)+"(s)")
        except:
            global mercyMeter
            if mercyMeter == 0:
                mercyMeter += 1
                errorWindow = tk.Tk()
                errorWindow.title("Fuck you")
                errorLabel = tk.Message(errorWindow,text="Don't break my program. Final warning. -Jacob",font=("Arial",70))
                errorLabel.grid(row=0,column=0)
                playsound('doBetter.mp3',block=False)
                errorWindow.mainloop()
            else:
                errorWindow = tk.Tk()
                errorWindow.title("Talos is angry")
                errorLabel = tk.Message(errorWindow,text="Talos demands blood for your sins. And thus, this program has died, and you have killed it.",font=("Arial",70))
                errorLabel.grid(row=0,column=0)
                window.destroy()
                errorWindow.mainloop()
calcButton.configure(command=calc)
nwLabel.grid(row=0,column=0)
outLabel.grid(row=3,column=1)
itemLabel.grid(row=0,column=2)
itemEntry.grid(row=1,column=2)
nwEntry.grid(row=1,column=0)
calcButton.grid(row=2,column=1)
window.mainloop()
