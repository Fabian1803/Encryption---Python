import tkinter as tk

class Polybios(tk.Frame):
    def __init__(self, master, switch_frame_callback):
        super().__init__(master)
        self.switch_frame_callback = switch_frame_callback
        
        label = tk.Label(self, text="Polybios")
        label.pack(pady=5)
        
        # Campo de entrada de texto para cifrar
        tk.Label(self, text="Texto para Cifrar:").pack(pady=5)
        self.texto_cifrar = tk.Entry(self, width=30)
        self.texto_cifrar.pack(pady=5)

        # Botón para cifrar
        button_cifrar = tk.Button(self, text="Cifrar", command=self.cifrar_texto)
        button_cifrar.pack(pady=5)

        # Área de texto para mostrar el resultado del cifrado
        self.resultado_cifrar = tk.Text(self, height=10, width=30)
        self.resultado_cifrar.pack(pady=5)
        self.resultado_cifrar.config(state=tk.DISABLED)  # Inicialmente deshabilitado para solo lectura
        
        # Botón para regresar al Frame 1
        button = tk.Button(self, text="menu", command=self.switch_frame_callback)
        button.pack(pady=5)

    def create_grid(self):
        grid = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I/J', 'K'],
            ['L', 'M', 'N', 'O', 'P'],
            ['Q', 'R', 'S', 'T', 'U'],
            ['V', 'W', 'X', 'Y', 'Z']
        ]
        
        coordinates = {}
        for row_index, row in enumerate(grid):
            for col_index, char in enumerate(row):
                if char == 'I/J':
                    coordinates['I'] = (row_index + 1, col_index + 1)
                    coordinates['J'] = (row_index + 1, col_index + 1)
                else:
                    coordinates[char] = (row_index + 1, col_index + 1)
        
        return coordinates

    def cipher_text(self, text, coordinates, use_numbers=False):
        result = []
        text = text.upper()
        for char in text:
            if char == ' ':
                result.append(' ')
            elif char in coordinates:
                row, col = coordinates[char]
                if use_numbers:
                    result.append(f"{row}{col}")
                else:
                    result.append(chr(ord('A') + row - 1) + chr(ord('A') + col - 1))
        
        return ''.join(result)

    def cifrar_texto(self):
        text = self.texto_cifrar.get()
        coordinates = self.create_grid()
        # Encrypt using numbers
        encrypted_text_numbers = self.cipher_text(text, coordinates, use_numbers=True)
        # Encrypt using letters
        encrypted_text_letters = self.cipher_text(text, coordinates, use_numbers=False)
        # Set the result in the text area
        self.resultado_cifrar.config(state=tk.NORMAL)
        self.resultado_cifrar.delete(1.0, tk.END)  # Clear previous text
        self.resultado_cifrar.insert(tk.END, f"Texto cifrado (Letras):\n{encrypted_text_letters}\n\n")
        self.resultado_cifrar.insert(tk.END, f"Texto cifrado (Números):\n{encrypted_text_numbers}")
        self.resultado_cifrar.config(state=tk.DISABLED)

