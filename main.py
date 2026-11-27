# from models import coches_model
# from tkinter import Tk, Label, Entry, Button, messagebox, Menu, Frame, ttk


# class App:
#     def __init__(self, ventana):
#         self.ventana = ventana
#         self.ventana.title("Gestión de Coches")
#         self.ventana.geometry("600x700")
#         self.ventana.resizable(0, 0)
#         self.main()
    
#     # .... Vistas o Views del Sistema ....
#     def borrarPantalla(self):
#         for widget in self.ventana.winfo_children():
#             widget.destroy()
    
#     def main(self):
#         self.borrarPantalla()
#         self.barraMenu()
#         Label(self.ventana, text="::: MENU PRINCIPAL :::").pack(pady=20)
#         Button(self.ventana, text="1.- Coches", width=15, height=2, command=self.menu_acciones).pack(pady=10)
#         Button(self.ventana, text="2.- Salir", width=15, height=2, command=self.ventana.quit).pack(pady=10)
    
#     def menu_acciones(self):
#         self.borrarPantalla()
#         self.barraMenu()
#         tipo = "Coche"
#         Label(self.ventana, text=f"...::: Menu de {tipo} :::...").pack(pady=10)
        
#         self.frame1 = Frame(self.ventana)
#         self.frame1.pack(pady=10)

#         Button(self.frame1, text="1.- Agregar", command=self.insertar_coche_view, width=12, height=3).grid(row=0, column=0, pady=10, padx=10)
#         Button(self.frame1, text="2.- Borrar", command=self.eliminar_coche_view, width=12, height=3).grid(row=1, column=0, pady=10, padx=10)
#         Button(self.frame1, text="3.- Modificar", command=self.modificar_coche_view, width=12, height=3).grid(row=2, column=0, pady=10, padx=10)
#         Button(self.frame1, text="4.- Mostrar", command=self.consultar_coche_view, width=12, height=3).grid(row=3, column=0, pady=10, padx=10)
#         Button(self.frame1, text="5.- Regresar", command=self.main, width=12, height=3).grid(row=4, column=0, pady=10, padx=10)
        
#     def insertar_coche_view(self):
#         self.borrarPantalla()
#         self.barraMenu()
#         Label(self.ventana, text="...Ingresar los datos del Coche").pack(pady=10)

#         self.frame1 = Frame(self.ventana)
#         self.frame1.pack(pady=10)
        
#         Label(self.frame1, text="Marca: ").grid(row=0, column=0, pady=5, padx=5, sticky="e")
#         self.marca = Entry(self.frame1)
#         self.marca.focus()
#         self.marca.grid(row=0, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame1, text="Color: ").grid(row=1, column=0, pady=5, padx=5, sticky="e")
#         self.color = Entry(self.frame1)
#         self.color.grid(row=1, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame1, text="Modelo: ").grid(row=2, column=0, pady=5, padx=5, sticky="e")
#         self.modelo = Entry(self.frame1)
#         self.modelo.grid(row=2, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame1, text="Velocidad: ").grid(row=3, column=0, pady=5, padx=5, sticky="e")
#         self.velocidad = Entry(self.frame1)
#         self.velocidad.grid(row=3, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame1, text="Potencia: ").grid(row=4, column=0, pady=5, padx=5, sticky="e")
#         self.potencia = Entry(self.frame1)
#         self.potencia.grid(row=4, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame1, text="# de Asientos: ").grid(row=5, column=0, pady=5, padx=5, sticky="e")
#         self.asientos = Entry(self.frame1)
#         self.asientos.grid(row=5, column=1, pady=5, padx=5, sticky="w")
        
#         self.frame_botones = Frame(self.ventana)
#         self.frame_botones.pack(pady=10)

#         Button(self.frame_botones, text=":: Agregar ::", command=lambda: [self.insertar_coche_controller(), self.insertar_coche_view()]).grid(row=0, column=0, pady=10, padx=5)
#         Button(self.frame_botones, text=":: Regresar ::", command=self.menu_acciones).grid(row=0, column=1, pady=10, padx=5)
       
#     def eliminar_coche_view(self):
#         self.borrarPantalla()
#         self.barraMenu()
#         Label(self.ventana, text="...Ingresar el ID del coche a eliminar").pack(pady=10)

#         self.frame1 = Frame(self.ventana)
#         self.frame1.pack(pady=10)

#         Label(self.frame1, text="ID: ").grid(row=0, column=0, pady=5, padx=5, sticky="e")
#         self.id = Entry(self.frame1)
#         self.id.focus()
#         self.id.grid(row=0, column=1, pady=5, padx=5, sticky="w")

#         self.btn_buscar = Button(self.frame1, text=":: Buscar ::", command=lambda: self.buscar_controller("eliminar"))
#         self.btn_buscar.grid(row=0, column=2, pady=5, padx=5)

#         self.frame_botones = Frame(self.ventana)
#         self.frame_botones.pack(pady=10)

#         self.btn_eliminar = Button(self.frame_botones, text=":: Eliminar ::", state="disabled", command=lambda: [self.eliminar_coche_controller(), self.eliminar_coche_view()])
#         self.btn_eliminar.grid(row=0, column=0, pady=5, padx=5)

#         Button(self.frame_botones, text=":: Regresar ::", command=self.menu_acciones).grid(row=0, column=1, pady=5, padx=5)

#     def consultar_coche_view(self):
#         self.borrarPantalla()
#         self.barraMenu()
#         Label(self.ventana, text="..:: Consultar Coches ::..").pack(pady=10)

#         # Tabla
#         self.tree = ttk.Treeview(self.ventana, columns=("ID", "Marca", "Color", "Modelo", "Velocidad", "Potencia", "Asientos"), show="headings")
#         self.tree.heading("ID", text="ID")
#         self.tree.heading("Marca", text="Marca")
#         self.tree.heading("Color", text="Color")
#         self.tree.heading("Modelo", text="Modelo")
#         self.tree.heading("Velocidad", text="Velocidad")
#         self.tree.heading("Potencia", text="Potencia")
#         self.tree.heading("Asientos", text="Asientos")

#         # Ajuste de ancho de columnas para ventana de 600px
#         self.tree.column("ID", width=45, anchor="center")
#         self.tree.column("Marca", width=95, anchor="center")
#         self.tree.column("Color", width=85, anchor="center")
#         self.tree.column("Modelo", width=95, anchor="center")
#         self.tree.column("Velocidad", width=85, anchor="center")
#         self.tree.column("Potencia", width=85, anchor="center")
#         self.tree.column("Asientos", width=80, anchor="center")

#         self.tree.pack(fill="both", expand=False, padx=15, pady=10)

#         # Llenar la tabla con los registros de la BD
#         self.consultar_coche_controller()

#         Button(self.ventana, text=":: Regresar ::", command=self.menu_acciones).pack(pady=10)
    
#     def modificar_coche_view(self):
#         self.borrarPantalla()
#         self.barraMenu()
#         Label(self.ventana, text="...Ingresar el ID del coche a modificar").pack(pady=10)

#         self.frame1 = Frame(self.ventana)
#         self.frame1.pack(pady=10)
        
#         Label(self.frame1, text="ID: ").grid(row=0, column=0, pady=5, padx=5, sticky="e")
#         self.id = Entry(self.frame1)
#         self.id.focus()
#         self.id.grid(row=0, column=1, pady=5, padx=5, sticky="w")

#         self.btn_buscar = Button(self.frame1, text=":: Buscar ::", command=lambda: self.buscar_controller("modificar"))
#         self.btn_buscar.grid(row=0, column=2, pady=5, padx=5)
        
#         Label(self.ventana, text="...Datos del Coche").pack(pady=10)

#         self.frame2 = Frame(self.ventana)
#         self.frame2.pack(pady=10)
        
#         Label(self.frame2, text="Marca: ").grid(row=1, column=0, pady=5, padx=5, sticky="e")
#         self.marca = Entry(self.frame2)
#         self.marca.grid(row=1, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame2, text="Color: ").grid(row=2, column=0, pady=5, padx=5, sticky="e")
#         self.color = Entry(self.frame2)
#         self.color.grid(row=2, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame2, text="Modelo: ").grid(row=3, column=0, pady=5, padx=5, sticky="e")
#         self.modelo = Entry(self.frame2)
#         self.modelo.grid(row=3, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame2, text="Velocidad: ").grid(row=4, column=0, pady=5, padx=5, sticky="e")
#         self.velocidad = Entry(self.frame2)
#         self.velocidad.grid(row=4, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame2, text="Potencia: ").grid(row=5, column=0, pady=5, padx=5, sticky="e")
#         self.potencia = Entry(self.frame2)
#         self.potencia.grid(row=5, column=1, pady=5, padx=5, sticky="w")
        
#         Label(self.frame2, text="# de Asientos: ").grid(row=6, column=0, pady=5, padx=5, sticky="e")
#         self.asientos = Entry(self.frame2)
#         self.asientos.grid(row=6, column=1, pady=5, padx=5, sticky="w")
        
#         self.btn_modificar = Button(self.frame2, text=":: Modificar ::", state="disabled", command=lambda: [self.modificar_coche_controller(), self.modificar_coche_view()])
#         self.btn_modificar.grid(row=7, column=0, pady=10, padx=5, sticky="e")
        
#         Button(self.frame2, text=":: Regresar ::", command=self.menu_acciones).grid(row=7, column=1, pady=10, padx=5, sticky="w")
        
#     # .... Controlador o Controller del Sistema ....
#     def respuesta_sql(self, respuesta):
#         if respuesta:
#             messagebox.showinfo(title=":: Exitoso ::", message="...¡Accion Realizada con Exito!...")
#         else:
#             messagebox.showerror(title=":: Verifique por favor ::", message="...¡Esta Accion no pudo realizarse en este momento!...")
    
#     def insertar_coche_controller(self):
#         coches1 = coches_model.Coches(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())                   
#         respuesta = coches1.insertar()
#         self.respuesta_sql(respuesta)
#         del coches1

#     def eliminar_coche_controller(self):
#         id = self.id.get()
#         resp = self.confirmar_eliminacion("eliminar")
#         if resp:
#             respuesta = coches_model.Coches.eliminar(id)
#         else:
#             respuesta = False
#         self.respuesta_sql(respuesta)
        
#     def consultar_coche_controller(self):
#         for row in self.tree.get_children():
#             self.tree.delete(row)
#         for row in coches_model.Coches.consultar():
#             self.tree.insert("", "end", values=row)
      
#     def modificar_coche_controller(self):
#         id = self.id.get()
#         coches1 = coches_model.Coches(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())  
#         respuesta = coches1.actualizar(id)
#         self.respuesta_sql(respuesta)
#         del coches1

#     def buscar_controller(self, tipo_accion):
#         id = self.id.get()
#         coche1 = coches_model.Coches.buscar(id)
#         if len(coche1) > 0:
#             messagebox.showinfo(title="...¡ Registro Encontrado !...", message=f"...¡El registro fue encontrado con exito, puedes {tipo_accion}!...")
#             self.cambiar_estado_btn(True, tipo_accion)
#             if tipo_accion == "modificar":
#                 self.marca.delete(0, "end")
#                 self.color.delete(0, "end")
#                 self.modelo.delete(0, "end")
#                 self.velocidad.delete(0, "end")
#                 self.potencia.delete(0, "end")
#                 self.asientos.delete(0, "end")

#                 self.marca.insert(0, coche1[0][1])
#                 self.color.insert(0, coche1[0][2])
#                 self.modelo.insert(0, coche1[0][3])
#                 self.velocidad.insert(0, coche1[0][4])
#                 self.potencia.insert(0, coche1[0][5])
#                 self.asientos.insert(0, coche1[0][6])
#         else:
#             messagebox.showerror(title="...¡Verifica por favor!...", message=f"...¡El registro no fue encontrado, no es posible {tipo_accion}!...")
#             self.cambiar_estado_btn(False, tipo_accion)

#     def barraMenu(self):
#         # Menu de Opciones
#         menuBar = Menu(self.ventana)
#         self.ventana.config(menu=menuBar)

#         menuPrincipal = Menu(menuBar, tearoff=False)
#         menuBar.add_cascade(label="Principal", menu=menuPrincipal)
#         menuPrincipal.add_command(label="Menu Principal", command=self.main)
#         menuPrincipal.add_command(label="Menu Acciones", command=self.menu_acciones)
#         menuPrincipal.add_separator()
#         menuPrincipal.add_command(label="Salir", command=self.ventana.quit)
                
#         accionesMenu = Menu(menuBar, tearoff=False)
#         menuBar.add_cascade(label="Acciones", menu=accionesMenu)
#         accionesMenu.add_command(label="Agregar", command=self.insertar_coche_view)
#         accionesMenu.add_command(label="Borrar", command=self.eliminar_coche_view)
#         accionesMenu.add_command(label="Modificar", command=self.modificar_coche_view)
#         accionesMenu.add_command(label="Mostrar", command=self.consultar_coche_view)
#         accionesMenu.add_separator()
#         accionesMenu.add_command(label="Regresar", command=self.main)

#     def cambiar_estado_btn(self, estado, tipo_accion):
#         nuevo_estado = "normal" if estado else "disabled"
#         if tipo_accion == "eliminar":
#             self.btn_eliminar.config(state=nuevo_estado)
#         elif tipo_accion == "modificar":
#             self.btn_modificar.config(state=nuevo_estado)

#     def confirmar_eliminacion(self, tipo):
#         resp = messagebox.askquestion(title="...¡Atencion!...", message=f"...¿Desea {tipo} este registro?...")
#         return resp == "yes"


# if __name__ == "__main__":
#     ventana = Tk()
#     app = App(ventana)
#     ventana.mainloop()

from tkinter import Tk
from views.coches_view import CochesView

if __name__ == "__main__":
    ventana = Tk()
    app = CochesView(ventana)
    ventana.mainloop()