import random
import pyperclip
import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.geometry("400x480")
ventana.title("Generador de Contraseñas")

# Variables para almacenar la longitud y la contraseña generada
longitud_contraseña = tk.StringVar()
contraseña_generada = tk.StringVar()


# Función para generar una contraseña segura
def generar_contraseña():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    # Validar si el usuario ingresó un número válido
    if longitud_contraseña.get().isdigit():
        longitud = int(longitud_contraseña.get())
        if 8 <= longitud <= 50:  # Se ajustó el rango, permitiendo más caracteres si es necesario
            contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
            contraseña_generada.set(contraseña)
        else:
            contraseña_generada.set("Error: debe tener entre 8 y 50 caracteres")
    else:
        contraseña_generada.set("Error: ingrese un número válido")


# Función para copiar la contraseña generada al portapapeles
def copiar_al_portapapeles():
    contraseña = contraseña_generada.get()
    if contraseña and "Error" not in contraseña:
        pyperclip.copy(contraseña)
        etiqueta_copiado.config(text="¡Copiado al portapapeles!", fg="green")
    else:
        etiqueta_copiado.config(text="Nada que copiar", fg="red")


# Etiqueta con instrucciones para el usuario
tk.Label(
    ventana,
    text="Ingrese la longitud de la contraseña \n(Debe ser entre 8 y 50 caracteres)",
    bg="blue",
    fg="white",
    font=("Arial", 10, "bold"),
    pady=5
).pack()

# Entrada para la longitud de la contraseña
entrada_longitud = tk.Entry(ventana, textvariable=longitud_contraseña)
entrada_longitud.pack(pady=5)

# Botón para generar la contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña)
boton_generar.pack(pady=5)

# Etiqueta para mostrar la contraseña generada
etiqueta_contraseña = tk.Label(ventana, textvariable=contraseña_generada, font=("Arial", 12, "bold"))
etiqueta_contraseña.pack(pady=5)

# Botón para copiar la contraseña al portapapeles
boton_copiar = tk.Button(ventana, text="Copiar al Portapapeles", command=copiar_al_portapapeles)
boton_copiar.pack(pady=5)

# Etiqueta para mostrar el estado de copiado
etiqueta_copiado = tk.Label(ventana, text="", font=("Arial", 10))
etiqueta_copiado.pack()

# Iniciar la interfaz gráfica
ventana.mainloop()
