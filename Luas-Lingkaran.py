import tkinter as tk
from tkinter import messagebox
import math

def hitung():
    try:
        r = float(entry_r.get())
        luas = math.pi * (r ** 2)  # Process
        label_hasil.config(text=f"Luas: {luas:.2f} cm²")  # Output
    except ValueError:
        messagebox.showerror("Error", "Masukkan jari-jari yang valid!")

def jalankan_testing():
    data_uji = [7, 10, 14.5]
    hasil_text = "--- HASIL 3 DATA UJI ---\n"
    for i, r in enumerate(data_uji, 1):
        luas = math.pi * (r ** 2)
        hasil_text += f"Uji {i} (r={r}): {luas:.2f} cm²\n"
    messagebox.showinfo("Testing Data Uji", hasil_text)

# Window Setup
root = tk.Tk()
root.title("B. Hitung Luas Lingkaran")
root.geometry("350x250")

# UI Components
tk.Label(root, text="Hitung Luas Lingkaran", font=("Arial", 14, "bold")).pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)
tk.Label(frame_input, text="Jari-jari (r):").pack(side=tk.LEFT, padx=5)
entry_r = tk.Entry(frame_input, width=10)
entry_r.pack(side=tk.LEFT)

tk.Button(root, text="Hitung Luas", command=hitung, bg="#4CAF50", fg="white").pack(pady=5)
label_hasil = tk.Label(root, text="Luas: -", font=("Arial", 11, "bold"))
label_hasil.pack(pady=5)

tk.Button(root, text="Jalankan Testing (3 Data Uji)", command=jalankan_testing, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()