import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from models.product import Product
from views.add_product import add_product_view


# Función para obtener la fila seleccionada y mostrar los valores
def mostrar_valores():
    seleccion = treeview.focus()  # Obtener la fila seleccionada
    if seleccion:  # Si se seleccionó una fila
        valores = treeview.item(seleccion)["values"]  # Obtener los valores de la fila
        # Mostrar los valores en una ventana o cuadro de diálogo
        tk.messagebox.showinfo("Valores de la fila",
                               "\n".join([f"{col}: {val}" for col, val in zip(columnas, valores)]))
    else:  # Si no se seleccionó ninguna fila
        tk.messagebox.showwarning("No hay fila seleccionada", "Por favor seleccione una fila para ver los valores")


# Función para eliminar la fila seleccionada
def eliminar_fila(products: list[Product]):
    seleccion = treeview.focus()  # Obtener la fila seleccionada
    if seleccion:  # Si se seleccionó una fila
        # Mostrar mensaje de confirmación
        confirmacion = tk.messagebox.askyesno("Confirmar eliminación", "¿Está seguro de que desea eliminar esta fila?")
        if confirmacion:  # Si el usuario confirma la eliminación
            valores = treeview.item(seleccion)["values"]  # Obtener los valores de la fila
            treeview.delete(seleccion)  # Eliminar la fila del Treeview

            # Eliminar el producto con nombre "producto2"
            for product in products:
                if product.name == valores[0]:
                    products.remove(product)
                    break  # Si encontramos el producto, podemos salir del loop


def add_item(products: list[Product]):
    add_product_view(ventana_tabla, products)
    print("XXXXSDSDS")
    # Actualizar la tabla
    treeview.delete(*treeview.get_children())  # Eliminar todas las filas de la tabla
    show_table(products, ventana_tabla)  # Volver a llenar la tabla con la nueva lista de productos


def show_table(objetos, ventana_padre, titulo="Tabla"):
    # Crear nueva ventana
    global ventana_tabla
    ventana_tabla = tk.Toplevel(ventana_padre)
    ventana_tabla.title(titulo)

    # Ocultar ventana padre
    ventana_padre.withdraw()

    # Obtener tamaño de pantalla
    ancho_pantalla = ventana_padre.winfo_screenwidth()
    alto_pantalla = ventana_padre.winfo_screenheight()

    # Calcular posición de la ventana de la tabla
    ancho_ventana = 600
    alto_ventana = 400
    x_ventana = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y_ventana = (alto_pantalla // 2) - (alto_ventana // 2)

    # Configurar tamaño y posición de la ventana de la tabla
    ventana_tabla.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, x_ventana, y_ventana))

    # Definir estilo personalizado
    estilo = ttk.Style()
    estilo.configure("mi_estilo.Treeview", font=("Times New Roman", 16))

    # Crear Treeview
    global treeview
    treeview = ttk.Treeview(ventana_tabla, style="mi_estilo.Treeview")

    # Agregar columnas
    # Se asume que todos los objetos tienen las mismas propiedades
    # y que las propiedades son representadas por los nombres de las columnas
    global columnas
    columnas = list(objetos[0].__dict__.keys())
    treeview["columns"] = columnas
    treeview.column("#0", anchor=tk.CENTER, width=50, minwidth=50)
    treeview.heading("#0", text="ID")
    for col in columnas:
        treeview.column(col, anchor=tk.CENTER)
        treeview.heading(col, text=col.title())  # Convertir el nombre de la propiedad a título

    # Agregar filas
    indice = 1  # Variable para generar ids consecutivos
    for obj in objetos:
        valores = [getattr(obj, col) for col in columnas]
        treeview.insert("", "end", text=str(indice), values=valores)
        indice += 1

    # Agregar botones
    frame_botones = tk.Frame(ventana_tabla)

    btn_agregar = ttk.Button(frame_botones, text=f"Agregar $titulo", command=lambda: add_item(objetos))
    btn_mostrar = ttk.Button(frame_botones, text="Mostrar valores", command=mostrar_valores)
    btn_eliminar = ttk.Button(frame_botones, text="Eliminar fila", command=lambda: eliminar_fila(objetos))
    btn_cerrar = ttk.Button(frame_botones, text="Cerrar", command=lambda: close_window(ventana_padre))

    btn_agregar.pack(side=tk.LEFT, padx=10, pady=10)
    btn_mostrar.pack(side=tk.LEFT, padx=10, pady=10)
    btn_eliminar.pack(side=tk.LEFT, padx=10, pady=10)
    btn_cerrar.pack(side=tk.LEFT, padx=10, pady=10)

    frame_botones.pack(side=tk.BOTTOM)

    # Mostrar Treeview
    treeview.pack(expand=True, fill=tk.BOTH)

    # Mostrar ventana de la tabla
    ventana_tabla.mainloop()


def close_window(ventana_padre):
    ventana_tabla.destroy()
    ventana_padre.deiconify()
