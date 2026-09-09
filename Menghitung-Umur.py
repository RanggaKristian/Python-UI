import tkinter as tk
from tkinter import messagebox
import datetime

def hitung():
    try:
        tahun_lahir = int(entry_tahun.get())
        tahun_sekarang = datetime.datetime.now().year
        
        # Process
        umur = tahun_sekarang - tahun_lahir
        
        # Output
        if umur < 0:
            messagebox.showerror("Error", "Tahun lahir tidak valid!")
        else:
            label_hasil.config(text=f"Umur Anda: {umur} Tahun")
    except ValueError:
        messagebox.showerror("Error", "Masukkan tahun lahir yang valid!")

def jalankan_testing():
    data_uji = [1998, 2005, 2012]
    tahun_sekarang = datetime.datetime.now().year
    hasil_text = "--- HASIL 3 DATA UJI ---\n"
    for i, thn in enumerate(data_uji, 1):
        u = tahun_sekarang - thn
        hasil_text += f"Uji {i} (Lahir {thn}): Umur {u} Tahun\n"
    messagebox.showinfo("Testing Data Uji", hasil_text)

# Window Setup
root = tk.Tk()
root.title("E. Menghitung Umur")
root.geometry("350x250")

# UI Components
tk.Label(root, text="Kalkulator Umur", font=("Arial", 14, "bold")).pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)
tk.Label(frame_input, text="Tahun Lahir:").pack(side=tk.LEFT, padx=5)
entry_tahun = tk.Entry(frame_input, width=10)
entry_tahun.pack(side=tk.LEFT)

tk.Button(root, text="Hitung Umur", command=hitung, bg="#4CAF50", fg="white").pack(pady=5)
label_hasil = tk.Label(root, text="Umur Anda: -", font=("Arial", 11, "bold"))
label_hasil.pack(pady=5)

tk.Button(root, text="Jalankan Testing (3 Data Uji)", command=jalankan_testing, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()