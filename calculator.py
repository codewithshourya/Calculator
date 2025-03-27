#Step 1: Import tkinter
from tkinter import *

#Step 2: Gui Interaction
window = Tk()
window.geometry("550x700")
window.title("Calculator")

# step 3: Adding inputs
def show(event):
    text = event.widget.cget("text")
    
    if text == "=":
        pass
    elif text=="AC":
        scval.set("")
        screen.update()
        
    elif text=="C":
        scval.set(scval.get()[:-1])
        screen.update()
        
    elif text=="ENTER":
        scval.set(eval(scval.get()))
        screen.update()
    
    else:
        scval.set(scval.get()+ text)

scval = StringVar()
screen= Entry(window,textvariable=scval, font=("lucida", 35, "bold"))
screen.pack(pady=10 )

buttons = [
    ["7","8","9","AC"],
    ["4","5","6","C"],
    ["1","2","3","ENTER"],
    ["0","*","/","="],
    ["+","-","%","."]
    
]
button_width = 4
button_height = 2

for row in buttons:
    f = Frame(window, bg="grey")
    f.pack(pady=5)
    for btn in row:
        b = Button(f, text=btn, font=("lucida", 20, "bold"), padx=15,pady=1,width=button_width, height=-button_height)
        b.pack(side="left",padx=10,pady=10)
        b.bind("<Button-1>", show)
        f.pack()
        

# Adjusting packing order and ensuring visibility

# step 4: mainloop

mainloop()