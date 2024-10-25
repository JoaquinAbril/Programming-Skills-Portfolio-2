# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 06:59:38 2024

@author: joaqu
"""

import tkinter as tk  # Import tkinter for the window
from tkinter import ttk  # Import ttk for themed widgets
import random  # Import random for selecting jokes
import os  # Import os for file handling

# Set up the main window
root = tk.Tk()
root.title("Alexa Tell Me A Joke")
root.geometry("500x550")
root.configure(bg="#e0f7fa")
root.iconbitmap('C:/Users/joaqu/Downloads/images.ico')  # Set window icon

# Load jokes from a text file
def load_jokes(file_path):
    if not os.path.isfile(file_path):  # Check if file exists
        return []  # Return empty list if file is not found
    with open(file_path, 'r') as file:  # Open file in read mode
        return [joke.strip() for joke in file.readlines()]  # Read and clean up each line

# Display a random joke setup
def tell_joke():
    joke = random.choice(jokes)  # Choose a random joke
    setup, tell_joke.punchline = joke.split("?", 1)  # Split into setup and punchline
    joke_text.delete(1.0, tk.END)  # Clear text area
    joke_text.insert(tk.END, setup + "?")  # Show setup part
    punchline_button.config(state="normal")  # Enable punchline button

# Show the punchline of the joke
def show_punchline():
    joke_text.insert(tk.END, "\n\n" + tell_joke.punchline.strip())  # Add punchline to text area
    punchline_button.config(state="disabled")  # Disable punchline button

# Set up the user interface
def setup_ui():
    # Main frame for the content
    frame = tk.Frame(root, bg="#e0f7fa")
    frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    # Title label
    title_label = tk.Label(frame, text="Joaquin's Joke Teller", bg="#e0f7fa", fg="#00695c", font=("Comic Sans MS", 30, "bold"))
    title_label.pack(pady=(10, 20))

    # Text area for displaying joke setup and punchline
    global joke_text
    joke_text = tk.Text(frame, height=8, width=50, wrap=tk.WORD, bg="#ffffff", fg="#333333", font=("Arial", 14), bd=0, relief=tk.FLAT)
    joke_text.pack(pady=10)
    joke_text.config(highlightthickness=2, highlightbackground="#00796b", highlightcolor="#00796b")

    # Button to display a new joke
    tell_joke_button = ttk.Button(frame, text="Tell me a Joke", command=tell_joke)
    tell_joke_button.pack(pady=5, fill=tk.X)
    style_button(tell_joke_button)

    # Button to show the punchline (starts as disabled)
    global punchline_button
    punchline_button = ttk.Button(frame, text="Show Punchline", state="disabled", command=show_punchline)
    punchline_button.pack(pady=5, fill=tk.X)
    style_button(punchline_button)

    # Quit button to close the app
    quit_button = ttk.Button(frame, text="Quit", command=root.quit)
    quit_button.pack(pady=(10, 20), fill=tk.X)
    style_button(quit_button)

# Style for buttons
def style_button(button):
    button.config(style="TButton")  # Apply custom style
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 16, "bold"), padding=10, borderwidth=0)  # Style details
    style.map("TButton", foreground=[("active", "white")], background=[("active", "#4CAF50")])

# Load jokes from the specified file path
jokes_file = 'C:/Users/joaqu/Desktop/joke.txt'
jokes = load_jokes(jokes_file)

setup_ui() # Call setup to initialize the UI

root.mainloop()  # Run the main event loop