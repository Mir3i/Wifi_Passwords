import tkinter as tk
from tkinter import messagebox
import subprocess

def run_script():
    try:
        result = subprocess.run('Wifi_Password.py', capture_output=True, text=True, shell=True)
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, result.stdout)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
app = tk.Tk()
app.title("Show Wifi Password")

# Set the window icon
app.iconbitmap("Icon.ico")  # Replace "your_icon.ico" with the path to your icon file

# Create a button to run the script
run_button = tk.Button(app, text="Run Script!", command=run_script)
run_button.pack(pady=10)

# Create a text widget to display the script output
output_text = tk.Text(app, height=10, width=50)
output_text.pack()

# Run the Tkinter event loop
app.mainloop()
