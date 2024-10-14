import tkinter as tk
from tkinter import StringVar
import re

# Function to check password strength using list comprehension
def check_password_strength(*args):
    password = password_var.get()
    
    # Criteria checks using list comprehension
    criteria_checks = [
        len(password) >= 8,  # Check length
        any(c.isupper() for c in password),  # Check uppercase
        any(c.islower() for c in password),  # Check lowercase
        any(c.isdigit() for c in password),  # Check numbers
        any(c in "!@#$%^&*(),.?\":{}|<>" for c in password)  # Check special characters
    ]
    
    # Calculate score based on how many criteria are met
    score = sum(criteria_checks)

    # Provide feedback based on the score
    feedback_text = ""
    if score == 5:
        feedback_text = "Password is Strong 💪"
        feedback_label.config(fg="green")
    elif score == 4:
        feedback_text = "Password is Good but could be stronger."
        feedback_label.config(fg="orange")
    elif score == 3:
        feedback_text = "Password is Medium. Add more variety."
        feedback_label.config(fg="orange")
    elif score == 2:
        feedback_text = "Password is Weak. Add uppercase, numbers, or special characters."
        feedback_label.config(fg="red")
    else:
        feedback_text = "Password is Very Weak. Consider making it longer with more diverse characters."
        feedback_label.config(fg="red")

    feedback.set(feedback_text)

# Function to toggle password visibility
def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Center window on screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Create the main application window
root = tk.Tk()
root.title("Password Complexity Checker")
center_window(root, 600, 400)

# Variables for password and feedback
password_var = StringVar()
feedback = StringVar()
show_password_var = tk.BooleanVar()

# Create a label and entry for password input
password_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
password_label.pack(pady=10)

password_entry = tk.Entry(root, textvariable=password_var, show="*", width=30, font=("Arial", 12))
password_entry.pack()

# Checkbox to show/hide password
show_password_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_checkbox.pack(pady=10)

# Create a label for feedback
feedback_label = tk.Label(root, textvariable=feedback, font=("Arial", 12))
feedback_label.pack(pady=20)

# Bind the function to update the password strength whenever the password changes
password_var.trace_add('write', check_password_strength)

# Run the application
root.mainloop()
