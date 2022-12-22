import subprocess
import tkinter as tk
from subprocess import CREATE_NEW_CONSOLE, Popen
import os
import signal




process = None


class ServerManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()
    process = None
    def initUI(self):
        global max_players_field
        global port_field
        # Create buttons to execute, stop, and restart the executable file
        execute_btn = tk.Button(self, text='Execute', command=self.execute)
        stop_btn = tk.Button(self, text='Stop', command=self.stop)
        restart_btn = tk.Button(self, text='Restart', command=self.restart)
        max_players_label = tk.Label(text="Max Players:")
        max_players_label.pack()
        max_players_field = tk.Entry()
        max_players_field.pack()

        port_label = tk.Label(text="Port:")
        port_label.pack()
        port_field = tk.Entry()
        port_field.pack()






        # Set up the layout
        execute_btn.pack(side='top', fill='x')
        stop_btn.pack(side='top', fill='x')
        restart_btn.pack(side='top', fill='x')
    process = None
    def execute(self):
        print("su2")
        max_players = max_players_field.get()
        port = port_field.get()
        global process
        global pid
    # Replace "path/to/executable" with the actual path to the executable file
        process = subprocess.Popen(f'AMP_Server.exe {max_players} {port} ',  creationflags=CREATE_NEW_CONSOLE)
        pid =Popen.pid()
        

    


    def stop(self):
        global process
        global pid
        print("su1")
        # Terminate the subprocess
        os.kill((process.pid), signal.SIGTERM)


    def restart(self):
        print("su3")
        # Restart the executable by stopping it and then starting it again
        self.stop()
        self.execute()


if __name__ == '__main__':
    server_manager = ServerManager()
    server_manager.mainloop()
