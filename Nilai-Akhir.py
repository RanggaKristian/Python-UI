import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        tugas = float(entry_tugas.get())
        uts = float(entry_uts.get())
        uas = float(entry_uas.get())
        
        # Process (Tugas 20%, UTS 30%, UAS 50%)
        nilai = (tugas * 0.20) + (uts * 0.30) + (uas * 0.50)
        status = "LULUS" if nilai >= 60 else "TIDAK LULUS"
        
        # Output
        label_hasil.config(text=f"Nilai Akhir: {nilai:.1f} | Status: {status}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan semua nilai dengan benar!")

def jalankan_testing():
    data_uji = [(80, 75, 85), (50, 40, 50), (90, 95, 100)]
    hasil_text = "--- HASIL 3 DATA UJI ---\n"
    for i, (t, u, ua) in enumerate(data_uji, 1):
        n = (t * 0.20) + (u * 0.30) + (ua * 0.50)
        st = "LULUS" if n >= 60 else "TIDAK LULUS"
        hasil_text += f"Uji {i} ({t}, {u}, {ua}): Nilai {n:.1f} ({st})\n"
    messagebox.showinfo("Testing Data Uji", hasil_text)

# Window Setup
root = tk.Tk()
root.title("D. Hitung Nilai Akhir")
root.geometry("380x320")

# UI Components
tk.Label(root, text="Kalkulator Nilai Akhir", font=("Arial", 14, "bold")).pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

tk.Label(frame_input, text="Nilai Tugas (20%):").grid(row=0, column=0, sticky="w", pady=2)
entry_tugas = tk.Entry(frame_input)
entry_tugas.grid(row=0, column=1, pady=2)

tk.Label(frame_input, text="Nilai UTS (30%):").grid(row=1, column=0, sticky="w", pady=2)
entry_uts = tk.Entry(frame_input)
entry_uts.grid(row=1, column=1, pady=2)

tk.Label(frame_input, text="Nilai UAS (50%):").grid(row=2, column=0, sticky="w", pady=2)
entry_uas = tk.Entry(frame_input)
entry_uas.grid(row=2, column=1, pady=2)

tk.Button(root, text="Hitung Nilai", command=hitung, bg="#4CAF50", fg="white").pack(pady=10)
label_hasil = tk.Label(root, text="Nilai Akhir: -", font=("Arial", 11, "bold"))
label_hasil.pack(pady=5)

tk.Button(root, text="Jalankan Testing (3 Data Uji)", command=jalankan_testing, bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()