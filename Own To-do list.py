# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:11:05 2023

@author: neill
"""

import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("Own To-Do List")

# Entry for adding tasks
entry = tk.Entry(root, width=50)
entry.pack(pady=20)

# Button to add tasks
add_button = tk.Button(root, text="CLICK TO ADD TASK", command=add_task, background="yellow")
add_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=20)
listbox.pack(pady=20)

# Button to delete selected task
delete_button = tk.Button(root, text="CLICK TO DELETE TASK", command=delete_task, background="blue")
delete_button.pack()

# Run the Tkinter event loop
root.mainloop()