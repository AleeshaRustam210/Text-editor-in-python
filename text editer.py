import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    text.delete("1.0", tk.END)


def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            text.delete("1.0", tk.END)
            text.insert(tk.END, content)

        except Exception as e:
            messagebox.showerror("Error", f"File open nahi hui:\n{e}")


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text.get("1.0", "end-1c"))

            messagebox.showinfo(
                "Success",
                "File successfully save ho gayi!"
            )

        except Exception as e:
            messagebox.showerror("Error", f"File save nahi hui:\n{e}")


# Main window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 12),
    fg="blue"
)
text.pack(expand=True, fill=tk.BOTH)

# Run application
root.mainloop()