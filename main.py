# A calculator application

import tkinter as tk
import tkinter.font
from math import sqrt

from calculate import Calculate

win = tk.Tk()
win.title('Simple Calculator')
win.resizable(0,0)

data = Calculate()
operatorFlag = False #this flag control the operator operation
dataSet = []

memory = 0

total = []
total.append(0)
grandTotalFlag = False

def plusminus():
    if (entry.get() == "0"):
        pass
    else:
        dataSet.clear()
        dataSet.append(-float(entry.get()))
        entry.set(-float(entry.get()))

def clear(elem):
    if elem == "All":
        dataSet.clear()
    else:
        dataSet.pop(len(dataSet) - 1)
    entry.set("0")
    #total[0] = 0

def insert(elem):
    global operatorFlag,total
    if operatorFlag == False and (len(dataSet)==0):
        dataSet.append(entry.get())
        dataSet.append(elem)
        operatorFlag = True
    elif operatorFlag == False and (len(dataSet)==1):
        dataSet.append(elem)
        operatorFlag = True
    elif operatorFlag == True and (len(dataSet)==0):
        dataSet.append(entry.get())
        dataSet.append(elem)
    elif len(dataSet) == 2:
        dataSet.append(entry.get())
        data.cal(dataSet,entry, total)

def insertNumber(elem):
    global operatorFlag
    if operatorFlag == False:
        if entry.get() == "0":
            entry.set(elem)
        elif len(dataSet) == 1:
            pass
        else:
            entry.set(entry.get()+elem)
    else:
        entry.set(elem)
        operatorFlag = False

def insertDot():
    if len(entry.get()) > 0 and "." not in entry.get():
        entry.set(entry.get() + ".")

def delete():
    if entry.get() == "0" or len(entry.get()) == 1:
        entry.set("0")
    else:
        entry.set(entry.get()[:len(entry.get()) - 1])

def percent():
    global operatorFlag
    pct = float(entry.get())/100
    entry.set(pct)
    dataSet.clear()
    dataSet.append(pct)

def otherOp(elem):

    global operatorFlag

    if operatorFlag == False:

        if elem == "1/x":
            if entry.get() == "0":
                entry.set(elem)
            else:
                entry.set(1/float(entry.get()))
        elif elem == "x\u00b2":
            if entry.get() == "0":
                entry.set(elem)
            else:
                entry.set((float(entry.get())**2))
        elif elem == "\u221Ax\u0305\u0305":
            if entry.get() == "0":
                entry.set(elem)
            else:
                entry.set((sqrt(float(entry.get()))))
        operatorFlag = True

    else:
        if elem == "1/x":
            entry.set(1/float(entry.get()))
        elif elem == "x\u00b2":
            entry.set((float(entry.get())**2))
        elif elem == "\u221Ax\u0305\u0305":
            entry.set((sqrt(float(entry.get()))))


def memClear():
    global memory
    memory = 0

def memRecall():
    global memory, operatorFlag
    entry.set(memory)
    operatorFlag = True

def memAdd():
    global memory
    memory += float(entry.get())

def memMinus():
    global memory
    memory -= float(entry.get())

def memStore():
    global memory
    memory = float(entry.get())

def grandTotal():
    global total,grandTotalFlag
    dataSet.clear()
    entry.set(total[0])

    if grandTotalFlag == False:
        total[0] = 0
        grandTotalFlag = True
    else:
        grandTotalFlag = False

entryFrame = tkinter.Frame(win,highlightthickness=1)
entryFrame.grid(column=0, row=0, padx=5, pady=5)

# entry number box
entry = tkinter.StringVar(entryFrame, value="0")
calculatorFont = tkinter.font.Font( family = "American Typewriter",
                                 size = 23,
                                 weight = "bold")
entry_txt = tkinter.Entry(entryFrame, textvariable=entry, font=calculatorFont, justify=tkinter.RIGHT)
entry_txt.grid(column=0, row=0)

frame0 = tkinter.Frame(win)
frame0.grid(column=0, row=1, padx=3,pady=5)

frame1 = tkinter.Frame(win)
frame1.grid(column=0, row=2, padx=3,pady=5)

mcButton = tkinter.Button(frame0, text="MC", width=6, height=1,command=lambda : memClear())
mcButton.grid(column=0, row=0, pady=1, padx=1)

mrButton = tkinter.Button(frame0, text="MR",width=6, height=1, command=lambda : memRecall())
mrButton.grid(column=1, row=0, pady=1, padx=1)

mplusButton = tkinter.Button(frame0, text="M+",width=6, height=1,command=lambda : memAdd())
mplusButton.grid(column=2, row=0, pady=1, padx=1)

mminusButton = tkinter.Button(frame0, text="M-",width=6, height=1,command=lambda : memMinus())
mminusButton.grid(column=3, row=0, pady=1, padx=1)

msButton = tkinter.Button(frame0, text="MS", width=6, height=1,command=lambda : memStore())
msButton.grid(column=4, row=0, pady=1, padx=1)

mxButton = tkinter.Button(frame0, text="GT",width=6, height=1,command=lambda : grandTotal())
mxButton.grid(column=5, row=0, pady=1, padx=1)

percentageButton = tkinter.Button(frame1, text="%", width=10, height=3, command=lambda : percent())
percentageButton.grid(column=0, row=1, padx=3,pady=3)

ceButton = tkinter.Button(frame1, text="CE",width=10, height=3, command=lambda : clear("Partial"))
ceButton.grid(column=1, row=1, padx=3,pady=3)

cButton = tkinter.Button(frame1, text="C",width=10, height=3,command=lambda : clear("All"))
cButton.grid(column=2, row=1, padx=3,pady=3)

dButton = tkinter.Button(frame1, text="<-",width=10, height=3,command=lambda : delete())
dButton.grid(column=3, row=1, padx=3,pady=3)

deButton = tkinter.Button(frame1, text="1/x", width=10, height=3, command=lambda : otherOp("1/x"))
deButton.grid(column=0, row=2, padx=3,pady=3)

powButton = tkinter.Button(frame1, text="x\u00b2", width=10, height=3, command=lambda : otherOp("x\u00b2"))
powButton.grid(column=1, row=2, padx=3,pady=3)

squareRootButton = tkinter.Button(frame1, text="\u221Ax\u0305\u0305",width=10, height=3,command=lambda : otherOp("\u221Ax\u0305\u0305"))
squareRootButton.grid(column=2, row=2, padx=3,pady=3)

divideButton = tkinter.Button(frame1, text="\u00F7",width=10, height=3,command=lambda:insert("\u00F7"))
divideButton.grid(column=3, row=2, padx=3,pady=3)

sevenButton = tkinter.Button(frame1, text="7", width=10, height=3, command=lambda:insertNumber("7"))
sevenButton.grid(column=0, row=3, padx=3,pady=3)

eightButton = tkinter.Button(frame1, text="8", width=10, height=3, command=lambda:insertNumber("8"))
eightButton.grid(column=1, row=3, padx=3,pady=3)

nineButton = tkinter.Button(frame1, text="9",width=10, height=3,command=lambda:insertNumber("9"))
nineButton.grid(column=2, row=3, padx=3,pady=3)

timesButton = tkinter.Button(frame1, text="x",width=10, height=3,command=lambda:insert("x"))
timesButton.grid(column=3, row=3, padx=3,pady=3)

fourButton = tkinter.Button(frame1, text="4", width=10, height=3, command=lambda:insertNumber("4"))
fourButton.grid(column=0, row=4, padx=3,pady=3)

fiveButton = tkinter.Button(frame1, text="5", width=10, height=3, command=lambda:insertNumber("5"))
fiveButton.grid(column=1, row=4, padx=3,pady=3)

sixButton = tkinter.Button(frame1, text="6",width=10, height=3,command=lambda:insertNumber("6"))
sixButton.grid(column=2, row=4, padx=3,pady=3)

minusButton = tkinter.Button(frame1, text="-" ,width=10, height=3,command=lambda:insert("-"))
minusButton.grid(column=3, row=4, padx=3,pady=3)

oneButton = tkinter.Button(frame1, text="1", width=10, height=3, command=lambda:insertNumber("1"))
oneButton.grid(column=0, row=5, padx=3,pady=3)

twoButton = tkinter.Button(frame1, text="2", width=10, height=3, command=lambda:insertNumber("2"))
twoButton.grid(column=1, row=5, padx=3,pady=3)

threeButton = tkinter.Button(frame1, text="3",width=10, height=3,command=lambda:insertNumber("3"))
threeButton.grid(column=2, row=5, padx=3,pady=3)

plusButton = tkinter.Button(frame1, text="+",width=10, height=3,command=lambda:insert("+"))
plusButton.grid(column=3, row=5, padx=3,pady=3)

plusminusButton = tkinter.Button(frame1, text="+/-", width=10, height=3, command=lambda:plusminus())
plusminusButton.grid(column=0, row=6, padx=3,pady=3)

zeroButton = tkinter.Button(frame1, text="0", width=10, height=3, command=lambda:insertNumber("0"))
zeroButton.grid(column=1, row=6, padx=3,pady=3)

dotButton = tkinter.Button(frame1, text=".",width=10, height=3,command=lambda:insertDot())
dotButton.grid(column=2, row=6, padx=3,pady=3)

equalButton = tkinter.Button(frame1, text="=",width=10, height=3,command=lambda:insert("="))
equalButton.grid(column=3, row=6, padx=3,pady=3)

win.mainloop()