import tkinter as tk
from models.product import Product

# Definir variables globales
entry_name = None
entry_price = None
entry_quantity = None
window = None


def validate_data(parent_window, product_list):
    # Acceder a las variables globales
    global entry_name, entry_price, entry_quantity

    new_product = Product(entry_name.get(), entry_price.get(), entry_quantity.get())

    product_list.append(new_product)
    tk.messagebox.showinfo("Producto agregado", new_product.view())
    print("Llegaaa")

    # Mostrar la ventana padre y cerrar la ventana actual
    parent_window.deiconify()
    print("lllll")
    window.destroy()
    print("aaaaaaa")


def add_product_view(parent_window, product_list):
    # Acceder a las variables globales
    global entry_name, entry_price, entry_quantity, window

    # Crear ventana
    window = tk.Toplevel()

    # Obtener dimensiones de la pantalla
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calcular la posición de la ventana en el centro de la pantalla
    x = int((screen_width - 300) / 2)
    y = int((screen_height - 200) / 2)

    # Establecer la geometría de la ventana
    window.geometry(f"300x200+{x}+{y}")

    # Ocultar la ventana padre
    parent_window.withdraw()

    # Crear etiquetas y campos de texto
    label_name = tk.Label(window, text="Ingrese el nombre:")
    entry_name = tk.Entry(window, justify="center")

    label_price = tk.Label(window, text="Ingrese el precio:")
    entry_price = tk.Entry(window, justify="center")

    label_quantity = tk.Label(window, text="Ingrese la cantidad:")
    entry_quantity = tk.Entry(window, justify="center")

    # Posicionar las etiquetas y campos de texto en la ventana
    label_name.pack()
    entry_name.pack()

    label_price.pack()
    entry_price.pack()

    label_quantity.pack()
    entry_quantity.pack()

    # Crear botón para confirmar datos
    confirm_button = tk.Button(
        window, text="Confirmar datos", command=lambda:  validate_data(parent_window, product_list)
    )

    confirm_button.pack()

    # Ejecutar la ventana
    window.mainloop()
