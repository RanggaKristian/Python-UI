import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32  # Process
        label_hasil.config(text=f"Hasil: {fahrenheit:.2f} °F")  # Output
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka suhu yang valid!")

def jalankan_testing():
    data_uji = [0, 37.5, 100]
    hasil_text = "--- HASIL 3 DATA UJI ---\n"
    for i, val in enumerate(data_uji, 1):
        res = (val * 9/5) + 32
        hasil_text += f"Uji {i}: {val}°C = {res:.2f}°F\n"
    messagebox.showinfo("Testing Data Uji", hasil_text)

# Window Setup
root = tk.Tk()
root.title("A. Konversi Celsius ke Fahrenheit")
root.geometry("350x250")

# UI Components
tk.Label(root, text="Konversi Suhu", font=("Arial", 14, "bold")).pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)
tk.Label(frame_input, text="Suhu (°C):").pack(side=tk.LEFT, padx=5)
entry_celsius = tk.Entry(frame_input, width=10)
entry_celsius.pack(side=tk.LEFT)

tk.Button(root, text="Hitung", command=hitung, bg="#4CAF50", fg="white").pack(pady=5)
label_hasil = tk.Label(root, text="Hasil: -", font=("Arial", 11, "bold"))
label_hasil.pack(pady=5)

tk.Button(root, text="Jalankan Testing (3 Data Uji)", command=jalankan_testing, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()