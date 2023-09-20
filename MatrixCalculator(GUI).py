import tkinter as tk
from tkinter import messagebox

def add_matrices():
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(col)] for i in range(row)]
    display_result(result)

def subtract_matrices():
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(col)] for i in range(row)]
    display_result(result)

def multiply_matrices():
    result = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            for k in range(col):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    display_result(result)

def display_result(result):
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_label = tk.Label(result_window, text="Result:")
    result_label.grid(row=0, column=0)
    for i in range(row):
        for j in range(col):
            result_text = tk.Label(result_window, text=result[i][j])
            result_text.grid(row=i+1, column=j)

def get_matrix_size():
    global row, col, matrix1_entries, matrix2_entries
    try:
        row = int(rows_entry.get())
        col = int(cols_entry.get())
        matrix1_entries = create_matrix_input_frame(1)
        matrix2_entries = create_matrix_input_frame(2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values for rows and columns.")

def calculate_operation():
    global matrix1, matrix2, row, col
    matrix1 = [[int(entry.get()) for entry in matrix1_entries[i]] for i in range(row)]
    matrix2 = [[int(entry.get()) for entry in matrix2_entries[i]] for i in range(row)]
    
    operation = operation_var.get()
    
    if operation == "Addition":
        add_matrices()
    elif operation == "Subtraction":
        subtract_matrices()
    elif operation == "Multiplication":
        multiply_matrices()

def create_matrix_input_frame(matrix_number):
    frame = tk.Frame(root)
    frame.grid()
    tk.Label(frame, text=f"Matrix {matrix_number}:").grid(row=0, column=0, columnspan=col)
    entries = []
    for i in range(row):
        row_entries = []
        for j in range(col):
            entry = tk.Entry(frame)
            entry.grid(row=i+1, column=j)
            row_entries.append(entry)
        entries.append(row_entries)
    return entries

root = tk.Tk()
root.title("Matrix Calculator")

row, col = 0, 0
matrix1_entries = []
matrix2_entries = []

rows_label = tk.Label(root, text="Enter number of rows:")
rows_label.grid()
rows_entry = tk.Entry(root)
rows_entry.grid()

cols_label = tk.Label(root, text="Enter number of columns:")
cols_label.grid()
cols_entry = tk.Entry(root)
cols_entry.grid()

size_button = tk.Button(root, text="Set Matrix Size", command=get_matrix_size)
size_button.grid()

operation_var = tk.StringVar()
operation_var.set("Addition")

operation_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication")
operation_menu.grid()

calculate_button = tk.Button(root, text="Calculate", command=calculate_operation)
calculate_button.grid()

root.mainloop()
