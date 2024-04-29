import tkinter as tk
from tkinter import messagebox
from PIL import ImageGrab

# Read the Operations.txt file
with open('Operations.txt', 'r') as file:
    lines = file.readlines()

# Read the OpitzCodes.txt file
with open('OpitzCodes.txt', 'r') as file:
    codes = file.readlines()

# Read the Tools.txt file
with open('Tools.txt', 'r') as file:
    tools = file.readlines()

# Function to create a process sheet for each part
def create_process_sheet(part_name, size, material, code, operations):
    def save_screenshot(widget):
        bbox=(widget.winfo_rootx(), widget.winfo_rooty(),
                                          widget.winfo_rootx() + 950,
                                          widget.winfo_rooty() + 600)
        screenshot = ImageGrab.grab(bbox)
        screenshot.save(f"ProcessSheets/{part_name.get()}_Process_Sheet.png")
        messagebox.showinfo("Success", "Process Sheet saved successfully.")
        widget.destroy()

    def update_material(material_var):
        material_label.config(text=material_var.get())

    process_sheet = tk.Toplevel(root)
    process_sheet.title(f"Process Sheet for {part_name.get()}")
    process_sheet.attributes('-fullscreen', True)  # Set the window to fullscreen

    # Create header labels
    tk.Label(process_sheet, text="Part Name:").grid(row=0, column=0, sticky='e')
    part_name_entry = tk.Entry(process_sheet, textvariable=part_name, justify='center')
    part_name_entry.grid(row=0, column=1, sticky='ew')

    tk.Label(process_sheet, text="Size:").grid(row=1, column=0, sticky='e')
    tk.Label(process_sheet, text=size).grid(row=1, column=1, sticky='w')

    tk.Label(process_sheet, text="Material:").grid(row=2, column=0, sticky='e')
    material_var = tk.StringVar(process_sheet)
    material_var.set(material)
    material_label = tk.Label(process_sheet, text=material_var.get())
    material_label.grid(row=2, column=1, sticky='w')
    tk.OptionMenu(process_sheet, material_var, "Aluminum", "Steel", command=lambda x: update_material(material_var)).grid(row=2, column=2, sticky='w')

    tk.Label(process_sheet, text="Code:").grid(row=3, column=0, sticky='e')
    tk.Label(process_sheet, text=code).grid(row=3, column=1, sticky='w')

    # Create labels for each column
    tk.Label(process_sheet, text="Operation #").grid(row=5, column=0)
    tk.Label(process_sheet, text="Operation Name").grid(row=5, column=1)
    tk.Label(process_sheet, text="Tool").grid(row=5, column=2)
    tk.Label(process_sheet, text="Spindle Speed (v)").grid(row=5, column=3)
    tk.Label(process_sheet, text="Feedrate (N)").grid(row=5, column=4)
    tk.Label(process_sheet, text="Depth of Cut (d)").grid(row=5, column=5)

    # Iterate over operations and display them in the process sheet
    for i, operation in enumerate(operations, start=1):
        tk.Label(process_sheet, text=str(10*i)).grid(row=i+5, column=0)
        tk.Label(process_sheet, text=operation).grid(row=i+5, column=1)
        tool_var = tk.StringVar(process_sheet)
        tool_var.set(tools[0].strip())  # Default tool
        tk.OptionMenu(process_sheet, tool_var, *map(lambda x: x.strip(), tools)).grid(row=i+5, column=2, sticky='ew')
        tk.Entry(process_sheet).grid(row=i+5, column=3, sticky='ew')  # Spindle Speed (v)
        tk.Entry(process_sheet).grid(row=i+5, column=4, sticky='ew')  # Feedrate (N)
        tk.Entry(process_sheet).grid(row=i+5, column=5, sticky='ew')  # Depth of Cut (d)

    # Save screenshot button
    tk.Button(process_sheet, text="Save Screenshot", command=lambda: save_screenshot(process_sheet), bg="green").grid(row=i+6, column=0, columnspan=6, sticky='ew')

# Create the main Tkinter window
root = tk.Tk()
root.title("CNC Parts Process Sheets")
root.iconbitmap("CAPP.ico")

# Set the window size and position
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 5
window_height = 5
x_position = screen_width - window_width
y_position = screen_height - window_height
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Automatically create process sheets
for idx, line in enumerate(lines, start=1):
    # Split the line into parts
    parts = line.split()
    if len(parts) < 3:
        messagebox.showerror("Error", f"Incomplete data in line {idx}")
        continue

    # Extract the size, material, and operations
    size = f"Length: {parts[0]}, Diameter: {parts[1]}"
    material = "Aluminum"  # Default material
    code = codes[idx - 1].strip()
    operations = parts[2:]
    part_name = tk.StringVar()
    part_name.set(f"Part {idx}")
    
    create_process_sheet(part_name, size, material, code, operations)

root.mainloop()
