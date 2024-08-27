import tkinter as tk

class Menu(tk.Frame):
    def __init__(self, master, show_polybios_callback, show_vigenere_callback, show_transposicion_callback, show_xor_callback, show_cesar_callback):
        super().__init__(master)
        self.show_polybios_callback = show_polybios_callback
        self.show_vigenere_callback = show_vigenere_callback
        self.show_transposicion_callback = show_transposicion_callback
        self.show_xor_callback = show_xor_callback
        self.show_cesar_callback = show_cesar_callback
        
        label = tk.Label(self, text="Menu de Encriptación")
        label.pack(pady=5)
        
        tk.Button(self, text="Cifrado de César", command=self.show_cesar_callback).pack(pady=5)
        tk.Button(self, text="Cifrado de Polybios", command=self.show_polybios_callback).pack(pady=5)
        tk.Button(self, text="Cifrado de Vigenere", command=self.show_vigenere_callback).pack(pady=5)
        tk.Button(self, text="Cifrado de Transposición", command=self.show_transposicion_callback).pack(pady=5)
        tk.Button(self, text="Cifrado de XOR", command=self.show_xor_callback).pack(pady=5)
