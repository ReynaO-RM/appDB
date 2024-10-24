import tkinter as tk
import requests


# Función para obtener el último registro de la base de datos
def obtener_ultimo_registro():
    url = 'https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:  # Verifica que la lista no esté vacía
            return data[-1]  # Obtiene el último registro de la lista
    return None


# Función para mostrar los datos en la interfaz
def mostrar_datos():
    ultimo_registro = obtener_ultimo_registro()

    if ultimo_registro:
        # Actualizamos las etiquetas con los datos del último registro
        label_id.config(text=f"ID: {ultimo_registro['id']}")
        label_nombre.config(text=f"Nombre: {ultimo_registro['nombre']}")
        label_apellido.config(text=f"Apellido: {ultimo_registro['apellido']}")
        label_ciudad.config(text=f"Ciudad: {ultimo_registro['ciudad']}")
        label_calle.config(text=f"Calle: {ultimo_registro['calle']}")
    else:
        label_id.config(text="Error al obtener datos")


# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title("Último Registro del Estudiante")
ventana.geometry("300x250")

# Crear etiquetas para mostrar los datos
label_id = tk.Label(ventana, text="ID: ", font=("Arial", 12))
label_id.pack(pady=5)

label_nombre = tk.Label(ventana, text="Nombre: ", font=("Arial", 12))
label_nombre.pack(pady=5)

label_apellido = tk.Label(ventana, text="Apellido: ", font=("Arial", 12))
label_apellido.pack(pady=5)

label_ciudad = tk.Label(ventana, text="Ciudad: ", font=("Arial", 12))
label_ciudad.pack(pady=5)

label_calle = tk.Label(ventana, text="Calle: ", font=("Arial", 12))
label_calle.pack(pady=5)

# Botón para refrescar los datos
boton_refrescar = tk.Button(ventana, text="Obtener Último Registro", command=mostrar_datos)
boton_refrescar.pack(pady=10)

# Mostrar los datos al iniciar la aplicación
mostrar_datos()

# Iniciar la aplicación
ventana.mainloop()

