import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.pack(pady=10)

        self.mark_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.mark_button.pack()

        self.show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks)
        self.show_button.pack()

    def add_task(self):
        task_name = self.task_entry.get()
        if task_name:
            self.tasks.append(task_name)
            self.task_listbox.insert(tk.END, task_name)
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Task Added", "Task added successfully!")

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            completed_task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.tasks.remove(completed_task)
            messagebox.showinfo("Task Completed", f"Task '{completed_task}' marked as completed.")

    def show_tasks(self):
        task_text = "\n".join(self.tasks)
        if not task_text:
            task_text = "No tasks yet."
        messagebox.showinfo("Tasks", task_text)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
