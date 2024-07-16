import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        return f"{status} {self.title}: {self.description}"

class ToDo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.configure(bg="white")
        
        self.tasks = []
        
        fontSettings = ("Arial", 14)
        
        self.frame = tk.Frame(root, bg="white")
        self.frame.pack(pady=20)
        
        self.titleLabel = tk.Label(self.frame, text="Title", bg="white", font=fontSettings)
        self.titleLabel.grid(row=0, column=0, pady=5)
        self.titleEntry = tk.Entry(self.frame, font=fontSettings)
        self.titleEntry.grid(row=0, column=1, pady=5)
        
        self.descLabel = tk.Label(self.frame, text="Description", bg="white", font=fontSettings)
        self.descLabel.grid(row=1, column=0, pady=5)
        self.descEntry = tk.Entry(self.frame, font=fontSettings)
        self.descEntry.grid(row=1, column=1, pady=5)
        
        self.addButton = tk.Button(self.frame, text="Add Task", command=self.addTask, bg="pink", font=fontSettings)
        self.addButton.grid(row=2, columnspan=2, pady=10)
        
        self.tasksListbox = tk.Listbox(root, width=50, font=fontSettings)
        self.tasksListbox.pack(pady=20)
        
        self.buttonFrame = tk.Frame(root, bg="white")
        self.buttonFrame.pack()
        
        self.updateButton = tk.Button(self.buttonFrame, text="Update Task", command=self.updateTask, bg="pink", font=fontSettings)
        self.updateButton.grid(row=0, column=0, padx=5, pady=5)
        
        self.deleteButton = tk.Button(self.buttonFrame, text="Delete Task", command=self.deleteTask, bg="pink", font=fontSettings)
        self.deleteButton.grid(row=0, column=1, padx=5, pady=5)
        
        self.completeButton = tk.Button(self.buttonFrame, text="Complete Task", command=self.completeTask, bg="pink", font=fontSettings)
        self.completeButton.grid(row=0, column=2, padx=5, pady=5)
        
    def addTask(self):
        title = self.titleEntry.get()
        description = self.descEntry.get()
        if title and description:
            self.tasks.append(Task(title, description))
            self.updateTasksListbox()
            self.titleEntry.delete(0, tk.END)
            self.descEntry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both title and description.")
        
    def updateTask(self):
        selectedTaskIndex = self.tasksListbox.curselection()
        if selectedTaskIndex:
            selected_task = self.tasks[selectedTaskIndex[0]]
            newTitle = self.titleEntry.get()
            newDescription = self.descEntry.get()
            if newTitle:
                selected_task.title = newTitle
            if newDescription:
                selected_task.description = newDescription
            self.updateTasksListbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
        
    def deleteTask(self):
        selectedTaskIndex = self.tasksListbox.curselection()
        if selectedTaskIndex:
            del self.tasks[selectedTaskIndex[0]]
            self.updateTasksListbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
        
    def completeTask(self):
        selectedTaskIndex = self.tasksListbox.curselection()
        if selectedTaskIndex:
            self.tasks[selectedTaskIndex[0]].completed = True
            self.updateTasksListbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete.")
        
    def updateTasksListbox(self):
        self.tasksListbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasksListbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDo(root)
    root.mainloop()
