import tkinter as tk
from menu import Menu
from polybios import Polybios
from vigenere import Vigenere
from transposición import Transposición
from xor import XOR
from cesar import Cesar  # Importa el nuevo frame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación con Múltiples Frames")

        # Crear instancias de los frames
        self.frameMenu = Menu(self, self.show_frame_políbios, self.show_frame_vigenere, self.show_frame_transposicion, self.show_frame_xor, self.show_frame_cesar)
        self.framePolybios = Polybios(self, self.show_frame_menu)
        self.frameVigenere = Vigenere(self, self.show_frame_menu)
        self.frameTransposicion = Transposición(self, self.show_frame_menu)
        self.frameXOR = XOR(self, self.show_frame_menu)
        self.frameCesar = Cesar(self, self.show_frame_menu)  # Añade el nuevo frame César

        # Mostrar el primer frame inicialmente
        self.frameMenu.pack(padx=50, pady=70)

    def show_frame_menu(self):
        self.framePolybios.pack_forget()
        self.frameVigenere.pack_forget()
        self.frameTransposicion.pack_forget()
        self.frameXOR.pack_forget()
        self.frameCesar.pack_forget()
        self.frameMenu.pack(padx=180, pady=150)

    def show_frame_políbios(self):
        self.frameMenu.pack_forget()
        self.frameVigenere.pack_forget()
        self.frameTransposicion.pack_forget()
        self.frameXOR.pack_forget()
        self.frameCesar.pack_forget()
        self.framePolybios.pack(padx=80, pady=60)

    def show_frame_vigenere(self):
        self.frameMenu.pack_forget()
        self.framePolybios.pack_forget()
        self.frameTransposicion.pack_forget()
        self.frameXOR.pack_forget()
        self.frameCesar.pack_forget()
        self.frameVigenere.pack(padx=80, pady=60)

    def show_frame_transposicion(self):
        self.frameMenu.pack_forget()
        self.framePolybios.pack_forget()
        self.frameVigenere.pack_forget()
        self.frameXOR.pack_forget()
        self.frameCesar.pack_forget()
        self.frameTransposicion.pack(padx=80, pady=60)

    def show_frame_xor(self):
        self.frameMenu.pack_forget()
        self.framePolybios.pack_forget()
        self.frameVigenere.pack_forget()
        self.frameTransposicion.pack_forget()
        self.frameCesar.pack_forget()
        self.frameXOR.pack(padx=80, pady=60)

    def show_frame_cesar(self):
        self.frameMenu.pack_forget()
        self.framePolybios.pack_forget()
        self.frameVigenere.pack_forget()
        self.frameTransposicion.pack_forget()
        self.frameXOR.pack_forget()
        self.frameCesar.pack(padx=80, pady=60)

if __name__ == "__main__":
    app = App()
    app.mainloop()
