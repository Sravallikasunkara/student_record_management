import tkinter as tk
from tkinter import ttk, messagebox

students = []

def add_student(roll_number, name, score):
    student = {
        "roll_number": roll_number,
        "name": name,
        "score": score
    }
    students.append(student)
    messagebox.showinfo("Success", f"Student {name} added successfully.")

def search_student(roll_number=None, name=None):
    for student in students:
        if roll_number and student["roll_number"] == roll_number:
            return student
        if name and student["name"].lower() == name.lower():
            return student
    return None


def sort_students(by="name", ascending=True):
    if by == "name":
        students.sort(key=lambda x: x["name"].lower(), reverse=not ascending)
    elif by == "score":
        students.sort(key=lambda x: x["score"], reverse=not ascending)


def display_students(tree):
    for item in tree.get_children():
        tree.delete(item)
    for student in students:
        tree.insert("", "end", values=(student["roll_number"], student["name"], student["score"]))

def handle_add_student(tree, roll_number_entry, name_entry, score_entry):
    try:
        roll_number = int(roll_number_entry.get())
        name = name_entry.get()
        score = int(score_entry.get())
        add_student(roll_number, name, score)
        display_students(tree)
        roll_number_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        score_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid roll number and score.")


def handle_search_student(tree, roll_number_entry, name_entry):
    roll_number = roll_number_entry.get()
    name = name_entry.get()
    if roll_number:
        student = search_student(roll_number=int(roll_number))
    elif name:
        student = search_student(name=name)
    else:
        messagebox.showerror("Error", "Please enter roll number or name to search.")
        return

    if student:
        messagebox.showinfo("Student Found", f"Roll Number: {student['roll_number']}\nName: {student['name']}\nScore: {student['score']}")
    else:
        messagebox.showinfo("Not Found", "Student not found.")


def handle_sort_students(tree, by, ascending):
    sort_students(by=by, ascending=ascending)
    display_students(tree)


def main():
    root = tk.Tk()
    root.title("Student Records Management System")

    
    top_frame = tk.Frame(root, padx=10, pady=10)
    top_frame.pack(fill=tk.X)

    mid_frame = tk.Frame(root, padx=10, pady=10)
    mid_frame.pack(fill=tk.X)

    bottom_frame = tk.Frame(root, padx=10, pady=10)
    bottom_frame.pack(fill=tk.BOTH, expand=True)

    
    tk.Label(top_frame, text="Roll Number").grid(row=0, column=0, padx=5, pady=5)
    roll_number_entry = tk.Entry(top_frame)
    roll_number_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(top_frame, text="Name").grid(row=0, column=2, padx=5, pady=5)
    name_entry = tk.Entry(top_frame)
    name_entry.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(top_frame, text="Score").grid(row=0, column=4, padx=5, pady=5)
    score_entry = tk.Entry(top_frame)
    score_entry.grid(row=0, column=5, padx=5, pady=5)

    tk.Button(top_frame, text="Add Student", command=lambda: handle_add_student(tree, roll_number_entry, name_entry, score_entry)).grid(row=0, column=6, padx=5, pady=5)
    tk.Button(top_frame, text="Search Student", command=lambda: handle_search_student(tree, roll_number_entry, name_entry)).grid(row=0, column=7, padx=5, pady=5)

    
    tk.Button(mid_frame, text="Sort by Name (Asc)", command=lambda: handle_sort_students(tree, by="name", ascending=True)).pack(side=tk.LEFT, padx=5)

    tk.Button(mid_frame, text="Sort by Score (Asc)", command=lambda: handle_sort_students(tree, by="score", ascending=True)).pack(side=tk.LEFT, padx=5)

    
    columns = ("Roll Number", "Name", "Score")
    tree = ttk.Treeview(bottom_frame, columns=columns, show="headings")
    tree.heading("Roll Number", text="Roll Number")
    tree.heading("Name", text="Name")
    tree.heading("Score", text="Score")
    tree.pack(fill=tk.BOTH, expand=True)

    
    root.mainloop()

if __name__ == "__main__":
    main()
