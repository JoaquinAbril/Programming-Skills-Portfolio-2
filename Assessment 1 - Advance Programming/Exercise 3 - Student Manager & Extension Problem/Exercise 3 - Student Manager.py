# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:48:27 2024

@author: joaqu
"""

import tkinter as tk  # For creating the GUI
import os  # Import os for file handling

# Initialize the main window
root = tk.Tk()
root.title("Student Record's Manager")  # Set title of the window
root.geometry("500x600")  # Set size of the window
root.iconbitmap('')  # You can add an icon file path here

# Function to load jokes from a file (for future use if needed)
def load_jokes(file_path):
    if not os.path.isfile(file_path):  # Check if file exists
        return []
    with open(file_path, 'r') as file:
        return [joke.strip() for joke in file.readlines()]

# Load student data from a file and calculate necessary information
def load_student_data(file_path):
    if not os.path.isfile(file_path):  # Check if file exists
        return []
    with open(file_path, 'r') as file:
        data = file.readlines()  # Read all lines
    students = []
    for line in data[1:]:  # Skip header line
        parts = line.strip().split(',')  # Split each line by commas
        student_number = parts[0]
        name = parts[1]
        coursework_marks = list(map(int, parts[2:5]))  # Convert coursework marks to integers
        exam_mark = int(parts[5])  # Convert exam mark to integer
        total_coursework = sum(coursework_marks)  # Sum coursework marks
        total_marks = total_coursework + exam_mark  # Calculate total marks
        percentage = (total_marks / 160) * 100  # Calculate percentage
        grade = calculate_grade(percentage)  # Calculate grade based on percentage
        students.append((student_number, name, total_coursework, exam_mark, percentage, grade))
    return students  # Return list of students with calculated data

# Determine grade based on percentage
def calculate_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

# Display all student records in the text box
def display_student_records():
    output_text.delete(1.0, tk.END)  # Clear text box
    for student in students:
        output_text.insert(tk.END, f"Name: {student[1]}\n")
        output_text.insert(tk.END, f"Student Number: {student[0]}\n")
        output_text.insert(tk.END, f"Total Coursework Mark: {student[2]}\n")
        output_text.insert(tk.END, f"Exam Mark: {student[3]}\n")
        output_text.insert(tk.END, f"Overall Percentage: {student[4]:.2f}%\n")
        output_text.insert(tk.END, f"Grade: {student[5]}\n\n")
    avg_percentage = sum(student[4] for student in students) / len(students) if students else 0
    output_text.insert(tk.END, f"Number of Students: {len(students)}\n")
    output_text.insert(tk.END, f"Average Percentage: {avg_percentage:.2f}%\n")

# Display the student with the highest score
def show_highest_score():
    highest_student = max(students, key=lambda s: s[4])  # Find student with highest percentage
    display_student(highest_student)  # Display that student's data

# Display the student with the lowest score
def show_lowest_score():
    lowest_student = min(students, key=lambda s: s[4])  # Find student with lowest percentage
    display_student(lowest_student)  # Display that student's data

# Display a single student's record
def display_student(student):
    output_text.delete(1.0, tk.END)  # Clear text box
    output_text.insert(tk.END, f"Name: {student[1]}\n")
    output_text.insert(tk.END, f"Student Number: {student[0]}\n")
    output_text.insert(tk.END, f"Total Coursework Mark: {student[2]}\n")
    output_text.insert(tk.END, f"Exam Mark: {student[3]}\n")
    output_text.insert(tk.END, f"Overall Percentage: {student[4]:.2f}%\n")
    output_text.insert(tk.END, f"Grade: {student[5]}\n")

# Display the selected student's record from the dropdown
def view_selected_student():
    selected_index = student_dropdown.current()
    if selected_index != -1:
        display_student(students[selected_index])

# Main header
header_label = tk.Label(root, text="Student Record's Manager", font=("Arial", 18, "bold"))
header_label.pack(pady=10)

# Load student data from file
students = load_student_data('C:/Users/joaqu/Desktop/studentmarks.txt')

# Frame for action buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Button to view all student records
view_records_button = tk.Button(button_frame, text="View All Records", command=display_student_records)
view_records_button.grid(row=0, column=0, padx=5)

# Button to view the student with the highest score
highest_score_button = tk.Button(button_frame, text="Highest Score", command=show_highest_score)
highest_score_button.grid(row=0, column=1, padx=5)

# Button to view the student with the lowest score
lowest_score_button = tk.Button(button_frame, text="Lowest Score", command=show_lowest_score)
lowest_score_button.grid(row=0, column=2, padx=5)

# Dropdown menu to select a student by name
student_dropdown = tk.ttk.Combobox(root, values=[student[1] for student in students], state="readonly")
student_dropdown.pack(pady=10)

# Button to view the selected student's record from the dropdown
view_selected_button = tk.Button(root, text="View Selected Student Record", command=view_selected_student)
view_selected_button.pack(pady=5)

# Text box to display student records
output_text = tk.Text(root, height=20, width=60)
output_text.pack(pady=10)

# Start the application
root.mainloop()
