import subprocess
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Server Manager")

# Create a function to start the server process
def start_server():
    global server_process
    # Get the maximum number of players and port number from the input fields
    max_players = max_players_field.get()
    port = port_field.get()
    # Start the server with the specified maximum number of players and port number
    server_process = subprocess.Popen(f"cmd.exe {max_players} {port}", stdout=subprocess.PIPE)
    while True:
        output = server_process.stdout.readline()
        output_text.insert('end', output)
        output_text.see('end')
        if not output:
            break

# Create a button to start the server process
start_button = tk.Button(text="Start Server", command=start_server)
start_button.pack()

# Create a function to stop the server process
def stop_server():
    server_process.kill()

# Create a button to stop the server process
stop_button = tk.Button(text="Stop Server", command=stop_server)
stop_button.pack()

# Create a function to restart the server process
def restart_server():
    stop_server()
    start_server()

# Create a button to restart the server process
restart_button = tk.Button(text="Restart Server", command=restart_server)
restart_button.pack()

# Create a function to send a custom input to the server process
def send_input():
    input_text = input_field.get()
    server_process.stdin.write(input_text + '\n')

# Create a custom input field
input_field = tk.Entry()
input_field.pack()

# Create a button to send the custom input
input_button = tk.Button(text="Send Input", command=send_input)
input_button.pack()

# Create input fields for the maximum number of players and port number
max_players_label = tk.Label(text="Max Players:")
max_players_label.pack()
max_players_field = tk.Entry()
max_players_field.pack()

port_label = tk.Label(text="Port:")
port_label.pack()
port_field = tk.Entry()
port_field.pack()

# Create a text widget to display the output of the cmd process
output_text = tk.Text(window)
output_text.pack()

# Create a scroll bar for the text widget
scrollbar = tk.Scrollbar(output_text)
scrollbar.pack(side='right', fill='y')
scrollbar.config(command=output_text.yview)
output_text.config(yscrollcommand=scrollbar.set)

# Run the main loop
window.mainloop()
