from time import sleep
import tkinter as tk
from tkinter import ttk
from sources.functions.view import show_frame, ask_for_input
from sources.run import submit_form, chooseFile

root = tk.Tk()
root.title("Automatic Facebook")
root.geometry("1280x720")
root.resizable(False, False)

frameLogin = tk.Frame(root)
frameMain = tk.Frame(root)

for frame in (frameLogin, frameMain):
    frame.grid(row=0, column=0, sticky="news")

frameUsername = tk.Frame(frameLogin, height=10)
frameUsername.grid(row=0, column=0, padx=10, pady=10, sticky="w")
lbl_username = tk.Label(frameUsername, text="Username:", font=("Arial", 10))
lbl_username.grid(row=0, column=0, padx=5)
input_username = tk.Entry(frameUsername, font=("Arial", 10))
input_username.grid(row=0, column=1, padx=13)

framePassword = tk.Frame(frameLogin, height=10)
framePassword.grid(row=1, column=0, padx=10, pady=10, sticky="w")
lbl_password = tk.Label(framePassword, text="Password:", font=("Arial", 10))
lbl_password.grid(row=0, column=0, padx=5)
input_password = tk.Entry(framePassword, font=("Arial", 10))
input_password.grid(row=0, column=1, padx=15)

submit_button = tk.Button(
    frameLogin, text="Login", font=("Arial", 10), command=lambda: show_frame(frameMain)
)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

show_frame(frameLogin)


frameUsername = tk.Frame(frameMain, height=10)
frameUsername.grid(row=0, column=0, padx=10, pady=10, sticky="w")
lbl_username = tk.Label(frameUsername, text="Username:", font=("Arial", 10))
lbl_username.grid(row=0, column=0, padx=5)
input_username = tk.Entry(frameUsername, font=("Arial", 10))
input_username.grid(row=0, column=1, padx=13)

framePassword = tk.Frame(frameMain, height=10)
framePassword.grid(row=1, column=0, padx=10, pady=10, sticky="w")
lbl_password = tk.Label(framePassword, text="Password:", font=("Arial", 10))
lbl_password.grid(row=0, column=0, padx=5)
input_password = tk.Entry(framePassword, font=("Arial", 10))
input_password.grid(row=0, column=1, padx=15)

frameImage = tk.Frame(frameMain, height=10)
frameImage.grid(row=2, column=0, padx=10, pady=10, sticky="w")
btnOpenFile = tk.Button(
    frameImage,
    text="Choose file",
    font=("Arial", 10),
    command=lambda: chooseFile(label_text=lbl_image),
)
btnOpenFile.grid(row=0, column=0, pady=10, sticky="w", padx=10)
lbl_image = tk.Label(frameImage, text="No file choose", font=("Arial", 10))
lbl_image.grid(row=0, column=1, padx=5)

frameContent = tk.Frame(frameMain, height=10)
frameContent.grid(row=3, column=0, padx=10, pady=10, sticky="w")
lbl_content = tk.Label(frameContent, text="Content:", font=("Arial", 10))
lbl_content.grid(row=0, column=0, padx=5, sticky="nw")
text_box = tk.Text(frameContent, font=("Arial", 12), height=10, width=50, wrap="word")
text_box.grid(row=0, column=1, padx=25, pady=5)


newGroup = tk.Button(
    frameMain, text="New Group", font=("Arial", 10), command=ask_for_input
)
newGroup.grid(row=2, column=1, columnspan=2, pady=10, sticky="w", padx=10)


def get_selected_items():
    selected_items = tree.selection()
    if selected_items:
        for item in selected_items:
            item_data = tree.item(item)
            print(f"Item Data: {item_data}")


columns = ("ID", "Tên", "Tuổi")
tree = ttk.Treeview(
    frameMain, columns=columns, show="headings", selectmode="extended", height=10
)
tree.heading("ID", text="ID")
tree.heading("Tên", text="Tên")
tree.heading("Tuổi", text="Tuổi")

data = [
    (1, "Nguyễn Văn A", 25),
    (2, "Trần Thị B", 30),
    (3, "Lê Văn C", 22),
    (4, "Phạm Văn D", 28),
]

for item in data:
    tree.insert("", "end", values=item)

tree.grid(row=3, column=1, padx=10, pady=10, sticky="ew")


def adjust_tree_columns(event):
    total_width = event.width
    num_columns = len(columns)
    column_width = total_width // num_columns
    for col in columns:
        tree.column(col, width=column_width)


submit_button = tk.Button(
    frameMain,
    text="Gửi",
    font=("Arial", 12),
    command=lambda: submit_form(text_box, lbl_image),
)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
