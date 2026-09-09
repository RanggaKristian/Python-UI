import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        harga = float(entry_harga.get())
        qty = int(entry_qty.get())
        
        # Process
        subtotal = harga * qty
        diskon = subtotal * 0.10 if subtotal > 100000 else 0
        total = subtotal - diskon
        
        # Output
        label_hasil.config(text=f"Total Bayar: Rp{total:,.0f}\n(Diskon: Rp{diskon:,.0f})")
    except ValueError:
        messagebox.showerror("Error", "Masukkan harga dan jumlah yang valid!")

def jalankan_testing():
    data_uji = [(15000, 3), (50000, 3), (120000, 1)]
    hasil_text = "--- HASIL 3 DATA UJI ---\n"
    for i, (h, q) in enumerate(data_uji, 1):
        sub = h * q
        disc = sub * 0.10 if sub > 100000 else 0
        tot = sub - disc
        hasil_text += f"Uji {i} (Rp{h} x {q}): Rp{tot:,.0f}\n"
    messagebox.showinfo("Testing Data Uji", hasil_text)

# Window Setup
root = tk.Tk()
root.title("C. Program Total Belanja")
root.geometry("380x300")

# UI Components
tk.Label(root, text="Kalkulator Total Belanja", font=("Arial", 14, "bold")).pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

tk.Label(frame_input, text="Harga Barang (Rp):").grid(row=0, column=0, sticky="w", pady=2)
entry_harga = tk.Entry(frame_input)
entry_harga.grid(row=0, column=1, pady=2)

tk.Label(frame_input, text="Jumlah Beli:").grid(row=1, column=0, sticky="w", pady=2)
entry_qty = tk.Entry(frame_input)
entry_qty.grid(row=1, column=1, pady=2)

tk.Button(root, text="Hitung Total", command=hitung, bg="#4CAF50", fg="white").pack(pady=10)
label_hasil = tk.Label(root, text="Total Bayar: -", font=("Arial", 11, "bold"))
label_hasil.pack(pady=5)

tk.Button(root, text="Jalankan Testing (3 Data Uji)", command=jalankan_testing, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()