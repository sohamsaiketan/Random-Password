import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # Install with: pip install pyperclip

# Password Generator Logic
def generate_password():
    length = int(length_var.get())

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    if not (use_upper or use_lower or use_digits or use_symbols):
        messagebox.showwarning("Selection Error", "Please select at least one character type.")
        return

    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # Ensure at least one character of each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)
    final_password = ''.join(password[:length])
    password_entry.delete(0, tk.END)
    password_entry.insert(0, final_password)

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Variables
length_var = tk.StringVar(value="12")
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=False)

# Title
tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold")).pack(pady=10)

# Length
tk.Label(root, text="Password Length:").pack()
tk.Entry(root, textvariable=length_var, width=10, justify='center').pack(pady=5)

# Checkboxes
tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=upper_var).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lower_var).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=digit_var).pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Symbols (!@#...)", variable=symbol_var).pack(anchor='w', padx=40)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", padx=10, pady=5).pack(pady=15)

# Password Entry
password_entry = tk.Entry(root, font=("Consolas", 14), width=28, justify='center')
password_entry.pack(pady=10)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white", padx=10, pady=5).pack()

# Run
root.mainloop()
