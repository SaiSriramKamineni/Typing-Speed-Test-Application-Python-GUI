import tkinter as tk
from tkinter import messagebox
from time import time
import random

# List of technical language-related prompts
prompts = [
    "Python is a versatile language used for web development, data analysis, and automation.",
    "JavaScript is essential for creating interactive websites and is widely used in frontend development.",
    "Java is a popular programming language known for its portability across platforms.",
    "C++ is often used in systems programming and game development due to its performance capabilities.",
    "HTML is the standard markup language used to create web pages.",
    "CSS is used to control the layout and style of web pages, working alongside HTML.",
    "SQL is a language used to manage and manipulate databases.",
    "Ruby is a dynamic, open-source programming language with a focus on simplicity and productivity.",
    "Swift is a powerful programming language created by Apple for iOS and macOS app development.",
    "Go, also known as Golang, is a statically typed programming language designed for scalability and reliability."
]

# Function to calculate the accuracy of the typed input compared to the prompt
def calculate_accuracy(prompt, input_text):
    prompt_words = prompt.split()
    input_words = input_text.split()

    correct_words = 0
    for i in range(min(len(prompt_words), len(input_words))):
        if prompt_words[i] == input_words[i]:
            correct_words += 1

    # Accuracy is calculated as the percentage of correct words
    accuracy = (correct_words / len(prompt_words)) * 100
    return round(accuracy, 2)

# Function to calculate the number of typing errors
def typing_errors(prompt, input_text):
    prompt_words = prompt.split()
    input_words = input_text.split()
    errors = 0

    for i in range(len(input_words)):
        if i < len(prompt_words):
            if input_words[i] != prompt_words[i]:
                errors += 1
        else:
            errors += 1

    # Adding the words from the prompt that were not typed
    errors += len(prompt_words) - len(input_words)
    
    return errors

# Function to calculate the typing speed in words per minute (WPM)
def typing_speed(input_text, elapsed_time):
    words = input_text.split()
    num_words = len(words)

    # Speed is calculated in words per minute
    speed = (num_words / elapsed_time) * 60
    return round(speed, 2)

# Function to calculate the total time elapsed during typing
def time_elapsed(start_time, end_time):
    return round(end_time - start_time, 2)

# Start the typing test
def start_typing_test():
    global start_time, prompt
    prompt = random.choice(prompts)  # Select a random prompt
    prompt_label.config(text=prompt)
    
    start_time = time()
    typing_entry.config(state=tk.NORMAL)
    typing_entry.delete(1.0, tk.END)
    result_label.config(text="Start typing the prompt above and press 'Submit' when done.")

# Submit the typed text and calculate results
def submit_text():
    end_time = time()
    input_text = typing_entry.get("1.0", tk.END).strip()

    elapsed_time = time_elapsed(start_time, end_time)
    speed = typing_speed(input_text, elapsed_time)
    errors = typing_errors(prompt, input_text)
    accuracy = calculate_accuracy(prompt, input_text)

    result_text = (
        f"Time Elapsed: {elapsed_time} seconds\n"
        f"Typing Speed: {speed} words per minute\n"
        f"Errors: {errors}\n"
        f"Accuracy: {accuracy}%"
    )
    
    result_label.config(text=result_text)
    typing_entry.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("700x450")
root.config(bg="#1F1F1F")

# Style configurations
title_font = ("Arial", 18, "bold")
label_font = ("Arial", 14)
button_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)

# Colors
bg_color = "#1F1F1F"  # Background color
text_color = "#FFFFFF"  # Text color
button_color = "#4CAF50"  # Button color
button_hover_color = "#45A049"
entry_bg_color = "#333333"  # Entry box background
entry_fg_color = "#F0F0F0"  # Entry box text

# Prompt label
prompt_label = tk.Label(root, text="", wraplength=600, font=title_font, bg=bg_color, fg=text_color)
prompt_label.pack(pady=20)

# Typing entry box
typing_entry = tk.Text(root, height=5, width=60, font=entry_font, bg=entry_bg_color, fg=entry_fg_color, insertbackground=text_color, relief=tk.FLAT, wrap=tk.WORD)
typing_entry.pack(pady=10)
typing_entry.config(state=tk.DISABLED)

# Button styles
def on_enter(e, button):
    button['background'] = button_hover_color

def on_leave(e, button):
    button['background'] = button_color

# Start button
start_button = tk.Button(root, text="Start", command=start_typing_test, font=button_font, bg=button_color, fg=text_color, relief=tk.FLAT, activebackground=button_hover_color)
start_button.pack(pady=10)
start_button.bind("<Enter>", lambda e: on_enter(e, start_button))
start_button.bind("<Leave>", lambda e: on_leave(e, start_button))

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_text, font=button_font, bg=button_color, fg=text_color, relief=tk.FLAT, activebackground=button_hover_color)
submit_button.pack(pady=10)
submit_button.bind("<Enter>", lambda e: on_enter(e, submit_button))
submit_button.bind("<Leave>", lambda e: on_leave(e, submit_button))

# Result label
result_label = tk.Label(root, text="", font=label_font, bg=bg_color, fg=text_color)
result_label.pack(pady=20)

root.mainloop()
