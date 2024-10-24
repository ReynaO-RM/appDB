import tkinter as tk
class ShowRecord:
    def __init__(self, master):
        self.master = master
        self.__textoRegistro = None

        # Crear un label para mostrar los datos
        self.resultado_label = tk.Label(master, text="", font=("Arial", 12))
        self.resultado_label.pack(pady=10)

    def mostrar_datos(self, registro):
        self.__textoRegistro = registro
        self.resultado_label.config(text=self.__textoRegistro)  # Usa self.resultado_label
