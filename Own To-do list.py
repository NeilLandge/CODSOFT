# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 10:23:44 2023

@author: neill
"""

import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Own To-Do List")

        self.tasks = []

        # Entry for new task
        self.new_task_entry = tk.Entry(root, width=40)
        self.new_task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Buttons for adding and deleting tasks
        add_button = tk.Button(root, text="Add Task", command=self.add_task, background="yellow")
        add_button.grid(row=0, column=1, padx=10, pady=10)

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, background="blue")
        delete_button.grid(row=0, column=2, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Save tasks button
        save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks, background="green")
        save_button.grid(row=2, column=0, padx=10, pady=10)

        # Load tasks button
        load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks, background="pink")
        load_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        new_task = self.new_task_entry.get()
        if new_task:
            self.tasks.append(new_task)
            self.update_task_listbox()
            self.new_task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
        messagebox.showinfo("Save", "Tasks saved successfully!")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
            self.update_task_listbox()
            messagebox.showinfo("Load", "Tasks loaded successfully!")
        except FileNotFoundError:
            messagebox.showwarning("Load", "No saved tasks found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()