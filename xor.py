import tkinter as tk

class XOR(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback
        
        # Etiqueta y campo de texto para la entrada
        self.label = tk.Label(self, text="Este es el Frame XOR")
        self.label.pack(pady=5)
        
        # Campo de entrada para el mensaje
        tk.Label(self, text="Mensaje para Cifrar:").pack(pady=5)
        self.mensaje_entry = tk.Entry(self, width=30)
        self.mensaje_entry.pack(pady=5)
        
        # Selector de versión
        tk.Label(self, text="Seleccionar Versión:").pack(pady=5)
        self.version_var = tk.StringVar(value="XOR Estándar")  # Valor predeterminado
        versiones = ["XOR Estándar", "Clases"]
        self.version_selector = tk.OptionMenu(self, self.version_var, *versiones, command=self.version_seleccionada)
        self.version_selector.pack(pady=5)
        
        # Etiqueta y campo de entrada para la clave
        self.clave_label = tk.Label(self, text="Clave para Cifrar:")
        self.clave_entry = tk.Entry(self, width=30)
        
        # Inicialmente ocultar campo de clave
        self.clave_label.pack_forget()
        self.clave_entry.pack_forget()
        
        # Botón para cifrar
        button_cifrar = tk.Button(self, text="Cifrar", command=self.cifrar_texto)
        button_cifrar.pack(pady=5)

        # Área de texto para mostrar el resultado del cifrado
        self.resultado_cifrar = tk.Text(self, height=10, width=50)
        self.resultado_cifrar.pack(pady=5)
        self.resultado_cifrar.config(state=tk.DISABLED)  # Inicialmente deshabilitado para solo lectura

        # Botón para volver al menú
        self.button = tk.Button(self, text="Regresar al Menu", command=self.switch_frame_callback)
        self.button.pack(pady=5)
        
    def version_seleccionada(self, version):
        """Muestra u oculta el campo de entrada de clave basado en la versión seleccionada."""
        if version == "XOR Estándar":
            self.clave_label.pack(pady=5)
            self.clave_entry.pack(pady=5)
        else:
            self.clave_label.pack_forget()
            self.clave_entry.pack_forget()
    
    def cifrar_texto(self):
        version = self.version_var.get()
        mensaje = self.mensaje_entry.get().upper()  # Convertir a mayúsculas
        
        if version == "Clases":
            self.cifrar_clases(mensaje)
        elif version == "XOR Estándar":
            clave = self.clave_entry.get()
            self.cifrar_xor_estandar(mensaje, clave)
    
    def cifrar_clases(self, mensaje):
        # Tabla de conversión
        conversion_table = {
            'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100',
            'F': '00101', 'G': '00110', 'H': '00111', 'L': '01011', 'O': '01110',
            '+': '11010', '|': '11011', '*': '11100', '/': '11101', '#': '11110', '_': '11111'
        }

        # Crear un diccionario inverso para binario a texto
        bin_to_char = {v: k for k, v in conversion_table.items()}

        def text_to_bin(text):
            """Convierte un texto a una cadena de bits usando la tabla de conversión."""
            return ' '.join(conversion_table.get(char, '') for char in text)

        def bin_to_text(bin_str):
            """Convierte una cadena de bits a texto usando la tabla de conversión inversa."""
            bin_str = bin_str.replace(' ', '')
            try:
                return ''.join(bin_to_char[bin_str[i:i+5]] for i in range(0, len(bin_str), 5))
            except KeyError as e:
                raise ValueError(f"Binario inválido encontrado: {e}")

        def xor(bin1, bin2):
            """Realiza la operación XOR entre dos cadenas binarias de igual longitud separadas por espacios."""
            bin1 = bin1.replace(' ', '')  # Elimina los espacios
            bin2 = bin2.replace(' ', '')  # Elimina los espacios
            return ' '.join('1' if b1 != b2 else '0' for b1, b2 in zip(bin1, bin2))

        def format_bin(bin_str, group_size=5):
            """Formatea la cadena binaria en bloques del tamaño especificado separados por espacios."""
            return ' '.join(bin_str[i:i+group_size] for i in range(0, len(bin_str), group_size))

        # Convertir el mensaje a binario
        mensaje_bin = text_to_bin(mensaje)

        # Generar la clave con la misma longitud que el mensaje
        mensaje_bin_no_spaces = mensaje_bin.replace(' ', '')
        clave_bin = ' '.join(['1'*5] * (len(mensaje_bin_no_spaces) // 5))  # Clave de unos

        # Cifrar
        mensaje_cifrado_bin = xor(mensaje_bin, clave_bin)

        # Formatear los resultados
        mensaje_bin_formatted = format_bin(mensaje_bin.replace(' ', ''))
        clave_bin_formatted = format_bin(clave_bin.replace(' ', ''))
        mensaje_cifrado_bin_formatted = format_bin(mensaje_cifrado_bin.replace(' ', ''))

        # Mostrar resultados
        resultado = (
            f"Mensaje: {mensaje}\n"
            f"Mensaje A: {mensaje_bin_formatted}\n"
            f"Clave:    {clave_bin_formatted}\n"  # Mostrar la clave
            f"Resp. C:  {mensaje_cifrado_bin_formatted}\n"
            f"Clave:    {clave_bin_formatted}\n"
            f"Mensaje A: {mensaje_bin_formatted}\n"
        )
        self.mostrar_resultado(resultado)

    def cifrar_xor_estandar(self, mensaje, clave):
        def text_to_bin(text):
            return ''.join(format(ord(c), '08b') for c in text)

        def bin_to_text(bin_str):
            return ''.join(chr(int(bin_str[i:i+8], 2)) for i in range(0, len(bin_str), 8))

        def xor(bin1, bin2):
            """Realiza la operación XOR entre dos cadenas binarias de igual longitud sin espacios."""
            return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bin1, bin2))

        def format_bin(bin_str, group_size=8):
            """Formatea la cadena binaria en bloques del tamaño especificado separados por espacios."""
            return ' '.join(bin_str[i:i+group_size] for i in range(0, len(bin_str), group_size))

        clave_bin = text_to_bin(clave)
        mensaje_bin = text_to_bin(mensaje)
        
        # Asegurarse de que la clave sea de la misma longitud que el mensaje
        if len(clave_bin) < len(mensaje_bin):
            clave_bin = (clave_bin * (len(mensaje_bin) // len(clave_bin) + 1))[:len(mensaje_bin)]
        
        mensaje_cifrado_bin = xor(mensaje_bin, clave_bin)
        
        # Formatear los resultados
        mensaje_descifrado_bin = xor(mensaje_cifrado_bin, clave_bin)
        mensaje_cifrado = bin_to_text(mensaje_cifrado_bin)
        mensaje_descifrado = bin_to_text(mensaje_descifrado_bin)
        
        resultado = (
            f"Mensaje: {mensaje}\n"
            f"Mensaje A: {format_bin(mensaje_bin)}\n"
            f"Clave:    {format_bin(clave_bin)}\n"  # Mostrar la clave
            f"Resp. C:  {format_bin(mensaje_cifrado_bin)}\n"
            f"Clave:    {format_bin(clave_bin)}\n"
            f"Mensaje A: {format_bin(mensaje_bin)}\n"
            f"Mensaje Descifrado: {mensaje_descifrado}\n"
        )
        self.mostrar_resultado(resultado)
    
    def mostrar_resultado(self, resultado):
        """Muestra el resultado en el área de texto."""
        self.resultado_cifrar.config(state=tk.NORMAL)
        self.resultado_cifrar.delete(1.0, tk.END)
        self.resultado_cifrar.insert(tk.END, resultado)
        self.resultado_cifrar.config(state=tk.DISABLED)

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Aplicación XOR")
    
    def switch_frame():
        print("Regresando al menú...")

    app = XOR(root, switch_frame)
    app.pack(fill="both", expand=True)
    
    root.mainloop()
