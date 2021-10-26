# A calculator application

import tkinter as tk
import tkinter.font

win = tk.Tk()
win.title('Simple Calculator')
win.resizable(0,0)

def insert():
    pass

entryFrame = tkinter.Frame(win,highlightthickness=1)
entryFrame.grid(column=0, row=0, padx=5, pady=5)

# entry number box
entry = tkinter.StringVar(entryFrame, value='0')
calculatorFont = tkinter.font.Font( family = "American Typewriter",
                                 size = 23,
                                 weight = "bold")
entry_txt = tkinter.Entry(entryFrame, textvariable=entry, font=calculatorFont, justify=tkinter.RIGHT)
entry_txt.grid(column=0, row=0)
entry_txt.focus()

frame0 = tkinter.Frame(win)
frame0.grid(column=0, row=1, padx=3,pady=5)

frame1 = tkinter.Frame(win)
frame1.grid(column=0, row=2, padx=3,pady=5)

mcButton = tkinter.Button(frame0, text="MC", width=6, height=1,command=insert)
mcButton.grid(column=0, row=0, pady=1, padx=1)

mrButton = tkinter.Button(frame0, text="MR",width=6, height=1, command=insert)
mrButton.grid(column=1, row=0, pady=1, padx=1)

mplusButton = tkinter.Button(frame0, text="M+",width=6, height=1,command=insert)
mplusButton.grid(column=2, row=0, pady=1, padx=1)

mminusButton = tkinter.Button(frame0, text="M-",width=6, height=1,command=insert)
mminusButton.grid(column=3, row=0, pady=1, padx=1)

msButton = tkinter.Button(frame0, text="MS", width=6, height=1,command=insert)
msButton.grid(column=4, row=0, pady=1, padx=1)

mxButton = tkinter.Button(frame0, text="M*",width=6, height=1,command=insert)
mxButton.grid(column=5, row=0, pady=1, padx=1)

percentageButton = tkinter.Button(frame1, text="%", width=10, height=3, command=insert)
percentageButton.grid(column=0, row=1, padx=3,pady=3)

ceButton = tkinter.Button(frame1, text="CE",width=10, height=3, command=insert)
ceButton.grid(column=1, row=1, padx=3,pady=3)

cButton = tkinter.Button(frame1, text="C",width=10, height=3,command=insert)
cButton.grid(column=2, row=1, padx=3,pady=3)

dButton = tkinter.Button(frame1, text="<-",width=10, height=3,command=insert)
dButton.grid(column=3, row=1, padx=3,pady=3)

deButton = tkinter.Button(frame1, text="1/x", width=10, height=3, command=insert)
deButton.grid(column=0, row=2, padx=3,pady=3)

powButton = tkinter.Button(frame1, text="x\u00b2", width=10, height=3, command=insert)
powButton.grid(column=1, row=2, padx=3,pady=3)

squareRootButton = tkinter.Button(frame1, text="\u221Ax\u0305\u0305",width=10, height=3,command=insert)
squareRootButton.grid(column=2, row=2, padx=3,pady=3)

divideButton = tkinter.Button(frame1, text="\u00F7",width=10, height=3,command=insert)
divideButton.grid(column=3, row=2, padx=3,pady=3)

sevenButton = tkinter.Button(frame1, text="7", width=10, height=3, command=insert)
sevenButton.grid(column=0, row=3, padx=3,pady=3)

eightButton = tkinter.Button(frame1, text="8", width=10, height=3, command=insert)
eightButton.grid(column=1, row=3, padx=3,pady=3)

nineButton = tkinter.Button(frame1, text="9",width=10, height=3,command=insert)
nineButton.grid(column=2, row=3, padx=3,pady=3)

timesButton = tkinter.Button(frame1, text="x",width=10, height=3,command=insert)
timesButton.grid(column=3, row=3, padx=3,pady=3)

fourButton = tkinter.Button(frame1, text="4", width=10, height=3, command=insert)
fourButton.grid(column=0, row=4, padx=3,pady=3)

fiveButton = tkinter.Button(frame1, text="5", width=10, height=3, command=insert)
fiveButton.grid(column=1, row=4, padx=3,pady=3)

sixButton = tkinter.Button(frame1, text="6",width=10, height=3,command=insert)
sixButton.grid(column=2, row=4, padx=3,pady=3)

minusButton = tkinter.Button(frame1, text="-" ,width=10, height=3,command=insert)
minusButton.grid(column=3, row=4, padx=3,pady=3)

oneButton = tkinter.Button(frame1, text="1", width=10, height=3, command=insert)
oneButton.grid(column=0, row=5, padx=3,pady=3)

twoButton = tkinter.Button(frame1, text="2", width=10, height=3, command=insert)
twoButton.grid(column=1, row=5, padx=3,pady=3)

threeButton = tkinter.Button(frame1, text="3",width=10, height=3,command=insert)
threeButton.grid(column=2, row=5, padx=3,pady=3)

plusButton = tkinter.Button(frame1, text="+",width=10, height=3,command=insert)
plusButton.grid(column=3, row=5, padx=3,pady=3)

plusminusButton = tkinter.Button(frame1, text="+/-", width=10, height=3, command=insert)
plusminusButton.grid(column=0, row=6, padx=3,pady=3)

zeroButton = tkinter.Button(frame1, text="0", width=10, height=3, command=insert)
zeroButton.grid(column=1, row=6, padx=3,pady=3)

dotButton = tkinter.Button(frame1, text=".",width=10, height=3,command=insert)
dotButton.grid(column=2, row=6, padx=3,pady=3)

equalButton = tkinter.Button(frame1, text="=",width=10, height=3,command=insert)
equalButton.grid(column=3, row=6, padx=3,pady=3)

win.mainloop()