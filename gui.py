import tkinter as tk

def get_user():
    root = tk.Tk()
    root.title("Sélection utilisateur")
    
    name_label = tk.Label(root, text="Entrez votre nom :")
    name_entry = tk.Entry(root)
    submit_button = tk.Button(root, text="Soumettre", command=root.destroy)
    
    name_label.pack()
    name_entry.pack()
    submit_button.pack()
    
    root.mainloop()
    
    return name_entry.get()

def get_mode():
    root = tk.Tk()
    root.title("Sélection du mode")
    
    training_button = tk.Button(root, text="Entraînement", command=root.destroy)
    testing_button = tk.Button(root, text="Test", command=root.destroy)
    
    training_button.pack()
    testing_button.pack()
    
    root.mainloop()
    
    if training_button["state"] == "normal":
        return "training"
    else:
        return "testing"
