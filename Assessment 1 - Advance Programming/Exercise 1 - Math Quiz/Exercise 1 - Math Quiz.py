# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk  # Import tkinter for the window
from tkinter import messagebox  # Import messagebox for popup messages
import random  # Import random for generating random numbers

# Create the main window
root = tk.Tk()
root.title("Math Quiz Game")  # Set the window title
root.geometry("400x300")  # Set window size
root.configure(bg="#f0f0f0")  # Set background color

# Game variables
score = 0  # To keep track of the score
current_question = 1  # Current question number
total_questions = 10  # Total number of questions
level = 1  # Difficulty level
num1 = 0  # First number for the math problem
num2 = 0  # Second number for the math problem
operation = ""  # Math operation (e.g., +, -, *, /)
correct_answer = 0  # Correct answer for the problem

# Function to reset the game
def reset_game():
    global score, current_question
    score = 0  # Reset score to 0
    current_question = 1  # Reset question number to 1
    update_score()  # Update the score on the screen
    display_menu()  # Go back to the main menu

# Function to get a random number based on difficulty level
def random_number(level):
    if level == 1 or level == 2:  # For easy or moderate
        return random.randint(1, 99)  # Random integer between 1 and 99
    elif level == 3:  # For advanced
        return round(random.uniform(1, 99), 2)  # Random float (e.g., 45.67)

# Function to choose a math operation based on difficulty level
def decide_operation(level):
    if level == 1:  # Easy level
        return random.choice(['+', '-'])  # Use + or -
    else:  # Moderate or advanced level
        return random.choice(['+', '-', '*', '/'])  # Use +, -, *, /

# Function to update the score display
def update_score():
    score_label.config(text=f"Score: {score}")  # Update the score label

# Function to display a math problem
def display_problem():
    global num1, num2, operation, correct_answer, current_question, total_questions
    num1 = random_number(level)  # Get the first random number
    num2 = random_number(level)  # Get the second random number
    operation = decide_operation(level)  # Decide the math operation

    # Calculate the correct answer based on the operation
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2
    elif operation == '/':
        while num2 == 0:  # Avoid division by zero
            num2 = random_number(level)
        correct_answer = num1 / num2

    # Show the question
    question_label.config(text=f"Question {current_question}/{total_questions}: {num1} {operation} {num2} =")
    entry_answer.delete(0, tk.END)  # Clear the answer input box

# Function to check if the user's answer is correct
def check_answer():
    global score, current_question, correct_answer
    try:
        user_answer = float(entry_answer.get())  # Get the user's answer
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number.")  # Show error if input is not a number
        return

    # Check if the answer is correct
    if abs(user_answer - correct_answer) < 0.01:  # Small tolerance for floating points
        score += 1  # Increase score
        messagebox.showinfo("Correct!", "Good job!")  # Show success message
    else:
        messagebox.showinfo("Incorrect", f"The correct answer was {correct_answer:.2f}")  # Show correct answer

    update_score()  # Update the score display
    current_question += 1  # Go to the next question
    if current_question > total_questions:  # If all questions are done
        show_results()  # Show the results
    else:
        display_problem()  # Show the next problem

# Function to show results at the end of the quiz
def show_results():
    global score
    if score == 10:
        rank = "A+ (Perfect!) 🌟"
    elif score >= 8:
        rank = "A (Great Job!)"
    elif score >= 6:
        rank = "B (Good Effort!)"
    elif score >= 4:
        rank = "C (You can do better!)"
    else:
        rank = "F (Try again!) 😢"

    messagebox.showinfo("Quiz Complete", f"Your score is: {score} out of 10\nRank: {rank}")
    reset_game()  # Reset the game for replay

# Function to start the quiz based on the selected difficulty level
def start_quiz(selected_level):
    global level
    level = selected_level  # Set the selected level
    menu_frame.pack_forget()  # Hide the menu
    quiz_frame.pack(pady=20)  # Show the quiz
    display_problem()  # Display the first problem

# Function to display the main menu
def display_menu():
    quiz_frame.pack_forget()  # Hide the quiz
    menu_frame.pack(pady=20)  # Show the menu

# Create the main menu frame
menu_frame = tk.Frame(root, bg="#f0f0f0")
menu_label = tk.Label(menu_frame, text="Choose Difficulty Level", font=("Arial", 18, "bold"), bg="#f0f0f0")
menu_label.pack(pady=10)

# Difficulty level buttons
easy_button = tk.Button(menu_frame, text="Easy", font=("Arial", 14), command=lambda: start_quiz(1), width=10, bg="#add8e6")
moderate_button = tk.Button(menu_frame, text="Moderate", font=("Arial", 14), command=lambda: start_quiz(2), width=10, bg="#add8e6")
advanced_button = tk.Button(menu_frame, text="Advanced", font=("Arial", 14), command=lambda: start_quiz(3), width=10, bg="#add8e6")

# Place the buttons on the menu
easy_button.pack(pady=5)
moderate_button.pack(pady=5)
advanced_button.pack(pady=5)

# Create the quiz frame (hidden at the start)
quiz_frame = tk.Frame(root, bg="#f0f0f0")
question_label = tk.Label(quiz_frame, text="", font=("Arial", 16), bg="#f0f0f0")
question_label.pack(pady=10)

# Input box for the answer
entry_answer = tk.Entry(quiz_frame, font=("Arial", 14))
entry_answer.pack(pady=10)

# Submit button
submit_button = tk.Button(quiz_frame, text="Submit Answer", font=("Arial", 14), command=check_answer, bg="#add8e6")
submit_button.pack(pady=10)

# Score display
score_label = tk.Label(quiz_frame, text="Score: 0", font=("Arial", 14), bg="#f0f0f0")
score_label.pack(pady=10)

display_menu()  # Show the menu when the game starts

root.mainloop()  # Run the main event loop



