#list for jedi matstesr then removes anakin form jedi 
#anakin wants to be jedi masters - on the list but not the rank of master 
#return all jedis
#return all jedis that are jedi masters 
#list of masters 
#list of jedi


import tkinter as tk

list_of_jedi_masters = [
    "Yoda", "Mace Windu", "Obi-Wan Kenobi",
    "Plo Koon", "Kit Fisto", "Ki-Adi-Mundi", "Shaak Ti",
    "Luminara Unduli", "Depa Billaba", "Quinlan Vos", "Jocasta Nu",
    "Qui-Gon Jinn", "Aayla Secura", "Luke Skywalker"
]

def check_jedi():
    jedi_input = entry.get().strip()
    if not jedi_input:
        result_label.config(text="Please enter a name.", fg="orange")
        return

    if "anakin" in jedi_input.lower():
        result_label.config(text="He is NOT a Jedi Master!", fg="red")
    else:
        match = next((j for j in list_of_jedi_masters if j.lower() == jedi_input.lower()), None)
        if match:
            result_label.config(text=f"{match} is a Jedi Master!", fg="lightgreen")
        else:
            result_label.config(text=f"{jedi_input} is not in the Jedi Council records.", fg="gray")

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="", fg="white")
    entry.focus()

# Window setup
window = tk.Tk()
window.title("Jedi Status Checker")
window.geometry("380x220")
window.configure(bg="#1a1a2e")
window.resizable(False, False)

# Title
tk.Label(window, text="⚔️ Jedi Status Checker ⚔️", font=("Arial", 14, "bold"),
         bg="#1a1a2e", fg="#f0e68c").pack(pady=15)

# Entry field
entry = tk.Entry(window, font=("Arial", 12), width=28, justify="center")
entry.pack(pady=5)
entry.focus()

# Bind Enter key to check
window.bind("<Return>", lambda event: check_jedi())

# Buttons
button_frame = tk.Frame(window, bg="#1a1a2e")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Check Status", command=check_jedi,
          bg="#4a4a8a", fg="white", font=("Arial", 10, "bold"),
          padx=10).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="Reset", command=reset,
          bg="#5a2a2a", fg="white", font=("Arial", 10, "bold"),
          padx=10).grid(row=0, column=1, padx=5)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 11), bg="#1a1a2e",
                         fg="white", wraplength=340, justify="center")
result_label.pack(pady=10)

window.mainloop()
