import tkinter as tk

def rent_calcu():
    try:
        rent = int(entry_rent.get())
        food = int(entry_food.get())
        electricity_spend = int(entry_electricity.get())
        charge_per_unit = int(entry_charge.get())
        persons = int(entry_persons.get())

        total_electricity = electricity_spend * charge_per_unit
        total_cost = rent + food + total_electricity
        per_person_cost = total_cost / persons

        label_result.config(text=f"Each person pays: TK {per_person_cost:.2f}")
    except ValueError:
        label_result.config(text="Please enter valid numbers.")


root = tk.Tk()
root.title("Rent Calculator")
root.geometry("600x800")
root.config(bg="#2d3436")

# Input fields
def create_labeled_entry(label_text):
    frame = tk.Frame(root, bg="#2d3436")
    frame.pack(pady=2)
    tk.Label(frame, text=label_text, fg="white", bg="#2d3436", font=("Calibri", 18)).pack(side="left")
    entry = tk.Entry(frame, font=("Calibri", 12))
    entry.pack(side="left")
    return entry

entry_rent = create_labeled_entry("Rent: ")
entry_food = create_labeled_entry("Food: ")
entry_electricity = create_labeled_entry("Electricity Units: ")
entry_charge = create_labeled_entry("Charge per Unit: ")
entry_persons = create_labeled_entry("Number of Persons: ")

# Create the button
btn = tk.Button(root, text="Calculate", command=rent_calcu, font=("Calibri", 12), bg="white", fg="black")
btn.pack(pady=20)

# Define hover functions
def on_enter(e):
    btn.config(bg="#2d3436", fg="#636e72" )

def on_leave(e):
    btn.config(bg="white", fg="black")

# Bind hover events
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# Result label
label_result = tk.Label(root, font=("Calibri", 16, "bold"), fg="white", bg="#2d3436")
label_result.pack()

root.mainloop()