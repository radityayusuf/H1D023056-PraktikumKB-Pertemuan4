import tkinter as tk
from tkinter import ttk, messagebox
from pyswip import Prolog

prolog = Prolog()
prolog.consult("pakar_tidur_gui.pl")

penyakit = []
gejala = {}
index_penyakit = 0
index_gejala = 0
current_penyakit = ""
current_gejala = ""

def mulai_diagnosa():
    global penyakit, gejala, index_penyakit, index_gejala
    prolog.retractall("gejala_pos(_)") 
    prolog.retractall("gejala_neg(_)") 

    start_btn.config(state=tk.DISABLED)
    yes_btn.config(state=tk.NORMAL)
    no_btn.config(state=tk.NORMAL)

    penyakit.clear()
    gejala.clear()
    penyakit.extend([p["X"].decode() for p in prolog.query("penyakit(X)")])
    for p in penyakit:
        gejala[p] = [g["X"] for g in prolog.query(f'gejala(X, "{p}")')]

    index_penyakit = 0
    index_gejala = -1
    pertanyaan_selanjutnya()

def pertanyaan_selanjutnya(ganti_penyakit=False):
    global current_penyakit, current_gejala, index_penyakit, index_gejala

    if ganti_penyakit:
        index_penyakit += 1
        index_gejala = -1

    if index_penyakit >= len(penyakit):
        hasil_diagnosa()
        return

    current_penyakit = penyakit[index_penyakit]
    index_gejala += 1

    if index_gejala >= len(gejala[current_penyakit]):
        hasil_diagnosa(current_penyakit)
        return

    current_gejala = gejala[current_penyakit][index_gejala]

    if list(prolog.query(f"gejala_pos({current_gejala})")):
        pertanyaan_selanjutnya()
        return
    elif list(prolog.query(f"gejala_neg({current_gejala})")):
        pertanyaan_selanjutnya(ganti_penyakit=True)
        return

    pertanyaan = prolog.query(f"pertanyaan({current_gejala}, Y)").__next__()["Y"].decode()
    tampilkan_pertanyaan(pertanyaan)

def tampilkan_pertanyaan(pertanyaan):
    kotak_pertanyaan.config(state=tk.NORMAL)
    kotak_pertanyaan.delete(1.0, tk.END)
    kotak_pertanyaan.insert(tk.END, pertanyaan)
    kotak_pertanyaan.config(state=tk.DISABLED)

def jawaban(jwb):
    if jwb:
        prolog.assertz(f"gejala_pos({current_gejala})")
        pertanyaan_selanjutnya()
    else:
        prolog.assertz(f"gejala_neg({current_gejala})")
        pertanyaan_selanjutnya(ganti_penyakit=True)

def hasil_diagnosa(penyakit=""):
    if penyakit:
        messagebox.showinfo("Hasil Diagnosa", f"Anda kemungkinan mengalami: {penyakit}.")
    else:
        messagebox.showinfo("Hasil Diagnosa", "Tidak terdeteksi gangguan tidur.")

    start_btn.config(state=tk.NORMAL)
    yes_btn.config(state=tk.DISABLED)
    no_btn.config(state=tk.DISABLED)

# GUI
root = tk.Tk()
root.title("Sistem Pakar Diagnosa Gangguan Tidur")
root.geometry("600x400")
root.configure(bg="#e0f7fa")  # Warna biru muda lembut

# Frame utama
mainframe = tk.Frame(root, bg="#e0f7fa")
mainframe.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

judul = tk.Label(mainframe, text="🧠 Sistem Pakar Diagnosa Gangguan Tidur", font=("Helvetica", 16, "bold"), bg="#e0f7fa", fg="#01579b")
judul.pack(pady=10)

kotak_pertanyaan = tk.Text(mainframe, width=60, height=4, state=tk.DISABLED, font=("Arial", 12), wrap="word", bg="#ffffff", fg="#000000", bd=2, relief=tk.SOLID)
kotak_pertanyaan.pack(pady=10)

tombol_frame = tk.Frame(mainframe, bg="#e0f7fa")
tombol_frame.pack(pady=10)

yes_btn = tk.Button(tombol_frame, text="✔ Ya", width=15, state=tk.DISABLED, font=("Arial", 11), bg="#81c784", fg="white", activebackground="#66bb6a", command=lambda: jawaban(True))
yes_btn.grid(row=0, column=0, padx=10, pady=5)

no_btn = tk.Button(tombol_frame, text="✘ Tidak", width=15, state=tk.DISABLED, font=("Arial", 11), bg="#e57373", fg="white", activebackground="#ef5350", command=lambda: jawaban(False))
no_btn.grid(row=0, column=1, padx=10, pady=5)

start_btn = tk.Button(mainframe, text="Mulai Diagnosa", width=20, font=("Arial", 12, "bold"), bg="#29b6f6", fg="white", activebackground="#0288d1", command=mulai_diagnosa)
start_btn.pack(pady=15)

root.mainloop()
# End of the code