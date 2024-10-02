import tkinter as tk

def on_button_click():
    print("¡Botón clicado!")

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz Gráfica")

# Configurar el tamaño de la ventana
root.geometry("400x400")

# Crear un marco para la parte superior
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP, padx=10, pady=10)

# Crear dos ventanas de colores en la parte superior
ventana1 = tk.Frame(top_frame, bg="#FF5733", width=500, height=300)
ventana1.pack(side=tk.LEFT, padx=5)

ventana2 = tk.Frame(top_frame, bg="#33FF57", width=500, height=300)
ventana2.pack(side=tk.LEFT, padx=5)

# Crear un marco para la parte inferior
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

# Crear dos ventanas de colores en la parte inferior
ventana3 = tk.Frame(bottom_frame, bg="#3357FF", width=500, height=300)
ventana3.pack(side=tk.LEFT, padx=5)

ventana4 = tk.Frame(bottom_frame, bg="#FF33A8", width=500, height=300)
ventana4.pack(side=tk.LEFT, padx=5)

# Etiqueta en la ventana inferior izquierda
etiqueta = tk.Label(ventana3, text="Mi Etiqueta", bg="#3357FF", fg="white")
etiqueta.pack(pady=20)

etiqueta = tk.Label(ventana4, text="Mi Etiqueta", bg="#FF33A8", fg="white")
etiqueta.pack(pady=20)

# Ventana inferior derecha con botón
boton = tk.Button(ventana4, text="Haz clic aquí", command=on_button_click)
boton.pack(pady=10)

# Hacer que todos los cuadros tengan el mismo tamaño
ventana1.pack_propagate(False)
ventana2.pack_propagate(False)
ventana3.pack_propagate(False)
ventana4.pack_propagate(False)

# Iniciar el bucle principal de la interfaz
root.mainloop()
