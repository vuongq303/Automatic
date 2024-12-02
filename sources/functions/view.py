from tkinter import simpledialog


def show_frame(frame):
    frame.tkraise()


def ask_for_input():
    user_input = simpledialog.askstring("Input", "Enter url group:")
    print(f"User Input: {user_input}")
