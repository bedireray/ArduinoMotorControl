import serial
from tkinter import *
from tkinter import ttk
import time

pos = 0
def send(*args):
    try:
        data = rpm.get() + direc.get() + degree.get()
        #data = degree.get()
        global pos
        pos.set( pos.get() + int(degree.get()))
        print (data)
        ser = serial.Serial('COM4', 115200)
        time.sleep(2)
        ser.write(data.encode())
        time.sleep(5)
        


        #btn.config(state=DISABLED)
        while True:
            myData = ''
            if (ser.inWaiting()>0):
                myData = ser.readline()
                print (myData.decode())
            if (myData == ""):
                break
            
        #     msg = ser.readline()
        #     if msg == "Done!":
        #         #btn.config(state=NORMAL)
        #         break
        #     pass
        ser.close()
    except ValueError:
        pass
    
root = Tk()
root.title("Arduino Serial")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

rpm = StringVar()
degree = StringVar()
direc = StringVar()
pos = IntVar()



feet_entry = ttk.Entry(mainframe, width=7, textvariable=rpm)
feet_entry.grid(column=2, row=1, sticky=(W, E))
degree_entry = ttk.Entry(mainframe, width=7, textvariable=degree)
degree_entry.grid(column=7, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=pos).grid(column=2, row=3, sticky=(W, E))
box = ttk.Combobox(mainframe, textvariable=direc, state='readonly')
box['values'] = ('CW', 'CCW')
box.current(0)
box.grid(column=5, row=1, sticky=(E))

ttk.Label(mainframe, textvariable=rpm).grid(column=2, row=2, sticky=(W, E))
btn = ttk.Button(mainframe, text="Send", command=send).grid(column=8, row=4, sticky=W)
ttk.Label(mainframe, text="Speed").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="rpm").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Direction").grid(column=4, row=1, sticky=W)
ttk.Label(mainframe, text="Position").grid(column=6, row=1, sticky=E)
ttk.Label(mainframe, text="degree").grid(column=8, row=1, sticky=E)
ttk.Label(mainframe, text="CV").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="rpm").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="CV").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Degree").grid(column=3, row=3, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind('<Return>', send)

root.mainloop()