import tkinter as tk

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            desplazamiento_base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - desplazamiento_base + (-desplazamiento-1)) % 26 + desplazamiento_base)
        else:
            resultado += char
    return resultado

def descifrado_cesar(texto, desplazamiento):
    # Aplica cifrado con desplazamiento inverso para descifrar
    return cifrado_cesar(texto, (-desplazamiento - 28))

class Cesar(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback
        
        # Etiqueta para el título
        label = tk.Label(self, text="Cifrado y Descifrado César")
        label.pack(pady=5)
        
        # Campo de entrada de texto para cifrar
        tk.Label(self, text="Texto para Cifrar:").pack(pady=5)
        self.texto_cifrar = tk.Entry(self, width=30)
        self.texto_cifrar.pack(pady=5)

        # Campo de entrada para el desplazamiento para cifrar
        tk.Label(self, text="Desplazamiento para Cifrar:").pack(pady=5)
        self.desplazamiento = tk.Entry(self, width=10)
        self.desplazamiento.pack(pady=5)
        
        # Botón para cifrar
        button_cifrar = tk.Button(self, text="Cifrar", command=self.cifrar_texto)
        button_cifrar.pack(pady=5)
        
        # Área de texto para mostrar el resultado del cifrado
        self.resultado_cifrar = tk.Text(self, height=2, width=30)
        self.resultado_cifrar.pack(pady=5)
        self.resultado_cifrar.config(state=tk.DISABLED)  # Inicialmente deshabilitado para solo lectura

        # Campo de entrada de texto para descifrar
        tk.Label(self, text="Texto para Descifrar:").pack(pady=5)
        self.texto_descifrar = tk.Entry(self, width=30)
        self.texto_descifrar.pack(pady=5)

        
        # Botón para descifrar
        button_descifrar = tk.Button(self, text="Descifrar", command=self.descifrar_texto)
        button_descifrar.pack(pady=5)
        
        # Área de texto para mostrar el resultado del descifrado
        self.resultado_descifrar = tk.Text(self, height=2, width=30)
        self.resultado_descifrar.pack(pady=5)
        self.resultado_descifrar.config(state=tk.DISABLED)  # Inicialmente deshabilitado para solo lectura
        
        # Botón para regresar al menú
        button_menu = tk.Button(self, text="Regresar al Menu", command=self.switch_frame_callback)
        button_menu.pack(pady=5)

    def cifrar_texto(self):
        texto = self.texto_cifrar.get()
        try:
            desplazamiento = int(self.desplazamiento.get())
        except ValueError:
            self.resultado_cifrar.config(state=tk.NORMAL)  # Habilitar el texto para mostrar el mensaje de error
            self.resultado_cifrar.delete(1.0, tk.END)
            self.resultado_cifrar.insert(tk.END, "Desplazamiento inválido")
            self.resultado_cifrar.config(state=tk.DISABLED)  # Deshabilitar el texto nuevamente
            return

        resultado = cifrado_cesar(texto, desplazamiento)
        self.resultado_cifrar.config(state=tk.NORMAL)  # Habilitar el texto para actualizar el resultado
        self.resultado_cifrar.delete(1.0, tk.END)  # Limpiar el área de texto
        self.resultado_cifrar.insert(tk.END, resultado)
        self.resultado_cifrar.config(state=tk.DISABLED)  # Deshabilitar el texto nuevamente

    def descifrar_texto(self):
        texto = self.texto_descifrar.get()
        try:
            desplazamiento = int(self.desplazamiento.get())
        except ValueError:
            self.resultado_descifrar.config(state=tk.NORMAL)  # Habilitar el texto para mostrar el mensaje de error
            self.resultado_descifrar.delete(1.0, tk.END)
            self.resultado_descifrar.insert(tk.END, "Desplazamiento inválido")
            self.resultado_descifrar.config(state=tk.DISABLED)  # Deshabilitar el texto nuevamente
            return

        resultado = descifrado_cesar(texto, desplazamiento)
        self.resultado_descifrar.config(state=tk.NORMAL)  # Habilitar el texto para actualizar el resultado
        self.resultado_descifrar.delete(1.0, tk.END)  # Limpiar el área de texto
        self.resultado_descifrar.insert(tk.END, resultado)
        self.resultado_descifrar.config(state=tk.DISABLED)  # Deshabilitar el texto nuevamente
