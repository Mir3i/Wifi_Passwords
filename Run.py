import tkinter as tk
from tkinter import messagebox
import subprocess

def run_script():
    try:
        result = subprocess.run('Wifi_Password.py', capture_output=True, text=True, shell=True)
        output_text.delete(1.0, tk.END) 
        output_text.insert(tk.END, result.stdout)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


app = tk.Tk()
app.title("Show Wifi Password")

app.iconbitmap("Icon.ico") 

run_button = tk.Button(app, text="Run Script!", command=run_script)
run_button.pack(pady=10)

output_text = tk.Text(app, height=10, width=50)
output_text.pack()

app.mainloop()
