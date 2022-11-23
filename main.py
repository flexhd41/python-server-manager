import tkinter as tk					
from tkinter import *
from tkinter import ttk
import os
import subprocess
import threading
import sys
def handleTabChange(event):
    if notebook.select() == notebook.tabs()[-1]:
        index = len(notebook.tabs())-1
        frame = tk.Frame(notebook)
        notebook.insert(index, frame, text="<untitled>")
        notebook.select(index)



root = tk.Tk()
root.title("Server Manager")
root.geometry('1000x400')
#tabControl = ttk.Notebook(root)
frame = tk.Frame(root)
frame.pack()
#notebook = ttk.Notebook(root)
#notebook.bind("<<NotebookTabChanged>>", handleTabChange)

#notebook.pack(fill="both", expand=True)


#add a tab that creates new tabs when selected
#frame = tk.Frame()
#notebook.add(frame, text="+")




# --- classes ---

class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll
        
    #def flush(self):
    #    pass

# --- functions ---

def run():
    threading.Thread(target=test).start()

def test():
    print("Thread: start")

    p = subprocess.Popen("ping -c 4 stackoverflow.com".split(), stdout=subprocess.PIPE, bufsize=1, text=True)
    while p.poll() is None:
        msg = p.stdout.readline().strip() # read a line from the process output
        if msg:
            print(msg)

    print("Thread: end")

def start():
    print("Starting server")
    p = subprocess.Popen("AMP_Server.exe {} {}".split(), stdout=subprocess.PIPE, bufsize=1, text=True .format(Port, Max-players))
    while p.poll() is None:
        msg = p.stdout.readline().strip() # read a line from the process output
        if msg:
            print(msg)


# --- main ---    



# - Frame with Text and Scrollbar -

frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

text = tk.Text(frame)
text.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

text['yscrollcommand'] = scrollbar.set
scrollbar['command'] = text.yview

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

# - rest -

button = tk.Button(root, text='Start', command=start)
button.pack(side=LEFT)
button = tk.Button(root, text='Stop', command=run)
button.pack(side=LEFT)
button = tk.Button(root, text='Restart', command=run)
button.pack(side=LEFT)
button= ttk.Button(root, text="Enter",)
button.pack(side=RIGHT)
E1 = Entry(root, textvariable=Port, bd =4)
E1.pack(side = RIGHT)
E1 = Entry(root, textvariable=Max-players,  bd =4)
E1.pack(side = RIGHT)



root.mainloop()

# - after close window -

sys.stdout = old_stdout
