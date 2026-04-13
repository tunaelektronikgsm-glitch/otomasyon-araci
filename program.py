import tkinter as tk
from tkinter import messagebox
import threading
import time
from pywinauto import Application

class OtoTus:
    def __init__(self, root):
        self.root = root
        self.root.title("Özel Otomasyon Paneli")
        self.root.geometry("300x250")
        
        tk.Label(root, text="Hedef Pencere Adı:").pack(pady=5)
        self.ent_pencere = tk.Entry(root)
        self.ent_pencere.pack()

        tk.Label(root, text="Basılacak Tuş (Örn: {ENTER} veya a):").pack(pady=5)
        self.ent_tus = tk.Entry(root)
        self.ent_tus.pack()

        tk.Label(root, text="Saniye Aralığı:").pack(pady=5)
        self.ent_sure = tk.Entry(root)
        self.ent_sure.insert(0, "5")
        self.ent_sure.pack()

        self.btn_baslat = tk.Button(root, text="BAŞLAT", command=self.baslat_thread, bg="green", fg="white")
        self.btn_baslat.pack(pady=10)
        
        self.calisiyor = False

    def baslat_thread(self):
        if not self.calisiyor:
            self.calisiyor = True
            self.btn_baslat.config(text="DURDUR", bg="red")
            threading.Thread(target=self.dongu, daemon=True).start()
        else:
            self.calisiyor = False
            self.btn_baslat.config(text="BAŞLAT", bg="green")

    def dongu(self):
        try:
            app = Application().connect(title_re=self.ent_pencere.get())
            dlg = app.window(title_re=self.ent_pencere.get())
            while self.calisiyor:
                dlg.send_keystrokes(self.ent_tus.get())
                time.sleep(float(self.ent_sure.get()))
        except Exception as e:
            self.calisiyor = False
            self.btn_baslat.config(text="BAŞLAT", bg="green")
            messagebox.showerror("Hata", f"Pencere bulunamadı veya hata oluştu: {e}")

root = tk.Tk()
app = OtoTus(root)
root.mainloop()
