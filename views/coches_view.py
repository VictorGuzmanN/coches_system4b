# from controllers import coches_controller
# from controllers.coches_controller import CochesController

# class CochesView:
#     pass

from tkinter import Label, Entry, Button, messagebox, Menu, Frame, ttk
from controllers.coches_controller import CochesController

class CochesView:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Coches")
        self.ventana.geometry("600x700")
        self.ventana.resizable(0, 0)
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def barraMenu(self):
        menuBar = Menu(self.ventana)
        self.ventana.config(menu=menuBar)

        menuPrincipal = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Principal", menu=menuPrincipal)
        menuPrincipal.add_command(label="Menu Principal", command=self.main)
        menuPrincipal.add_command(label="Menu Acciones", command=self.menu_acciones)
        menuPrincipal.add_separator()
        menuPrincipal.add_command(label="Salir", command=self.ventana.quit)

        accionesMenu = Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label="Acciones", menu=accionesMenu)
        accionesMenu.add_command(label="Agregar", command=self.insertar_coche_view)
        accionesMenu.add_command(label="Borrar", command=self.eliminar_coche_view)
        accionesMenu.add_command(label="Modificar", command=self.modificar_coche_view)
        accionesMenu.add_command(label="Mostrar", command=self.consultar_coche_view)
        accionesMenu.add_separator()
        accionesMenu.add_command(label="Regresar", command=self.main)

    # .... Vistas Principales ....
    def main(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana, text="::: MENU PRINCIPAL :::").pack(pady=20)
        Button(self.ventana, text="1.- Coches", width=15, height=2, command=self.menu_acciones).pack(pady=10)
        Button(self.ventana, text="2.- Salir", width=15, height=2, command=self.ventana.quit).pack(pady=10)

    def menu_acciones(self):
        self.borrarPantalla()
        self.barraMenu()
        tipo = "Coche"
        Label(self.ventana, text=f"...::: Menu de {tipo} :::...").pack(pady=10)

        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)

        Button(self.frame1, text="1.- Agregar", command=self.insertar_coche_view, width=12, height=3).grid(row=0, column=0, pady=10, padx=10)
        Button(self.frame1, text="2.- Borrar", command=self.eliminar_coche_view, width=12, height=3).grid(row=1, column=0, pady=10, padx=10)
        Button(self.frame1, text="3.- Modificar", command=self.modificar_coche_view, width=12, height=3).grid(row=2, column=0, pady=10, padx=10)
        Button(self.frame1, text="4.- Mostrar", command=self.consultar_coche_view, width=12, height=3).grid(row=3, column=0, pady=10, padx=10)
        Button(self.frame1, text="5.- Regresar", command=self.main, width=12, height=3).grid(row=4, column=0, pady=10, padx=10)

    # .... Vista Insertar ....
    def insertar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana, text="...Ingresar los datos del Coche").pack(pady=10)

        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)

        Label(self.frame1, text="Marca: ").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.marca = Entry(self.frame1)
        self.marca.focus()
        self.marca.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1, text="Color: ").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.color = Entry(self.frame1)
        self.color.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1, text="Modelo: ").grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.modelo = Entry(self.frame1)
        self.modelo.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1, text="Velocidad: ").grid(row=3, column=0, pady=5, padx=5, sticky="e")
        self.velocidad = Entry(self.frame1)
        self.velocidad.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1, text="Potencia: ").grid(row=4, column=0, pady=5, padx=5, sticky="e")
        self.potencia = Entry(self.frame1)
        self.potencia.grid(row=4, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame1, text="# de Asientos: ").grid(row=5, column=0, pady=5, padx=5, sticky="e")
        self.asientos = Entry(self.frame1)
        self.asientos.grid(row=5, column=1, pady=5, padx=5, sticky="w")

        self.frame_botones = Frame(self.ventana)
        self.frame_botones.pack(pady=10)

        Button(self.frame_botones, text=":: Agregar ::", command=self.accion_insertar).grid(row=0, column=0, pady=10, padx=5)
        Button(self.frame_botones, text=":: Regresar ::", command=self.menu_acciones).grid(row=0, column=1, pady=10, padx=5)

    # .... Vista Eliminar ....
    def eliminar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana, text="...Ingresar el ID del coche a eliminar").pack(pady=10)

        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)

        Label(self.frame1, text="ID: ").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.id = Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        self.btn_buscar = Button(self.frame1, text=":: Buscar ::", command=lambda: self.accion_buscar("eliminar"))
        self.btn_buscar.grid(row=0, column=2, pady=5, padx=5)

        self.frame_botones = Frame(self.ventana)
        self.frame_botones.pack(pady=10)

        self.btn_eliminar = Button(self.frame_botones, text=":: Eliminar ::", state="disabled", command=self.accion_eliminar)
        self.btn_eliminar.grid(row=0, column=0, pady=5, padx=5)

        Button(self.frame_botones, text=":: Regresar ::", command=self.menu_acciones).grid(row=0, column=1, pady=5, padx=5)

    # .... Vista Consultar ....
    def consultar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana, text="..:: Consultar Coches ::..").pack(pady=10)

        self.tree = ttk.Treeview(
            self.ventana,
            columns=("ID", "Marca", "Color", "Modelo", "Velocidad", "Potencia", "Asientos"),
            show="headings"
        )
        for col in ("ID", "Marca", "Color", "Modelo", "Velocidad", "Potencia", "Asientos"):
            self.tree.heading(col, text=col)

        self.tree.column("ID", width=45, anchor="center")
        self.tree.column("Marca", width=95, anchor="center")
        self.tree.column("Color", width=85, anchor="center")
        self.tree.column("Modelo", width=95, anchor="center")
        self.tree.column("Velocidad", width=85, anchor="center")
        self.tree.column("Potencia", width=85, anchor="center")
        self.tree.column("Asientos", width=80, anchor="center")

        self.tree.pack(fill="both", expand=False, padx=15, pady=10)

        self.llenar_tabla()

        Button(self.ventana, text=":: Regresar ::", command=self.menu_acciones).pack(pady=10)

    # .... Vista Modificar ....
    def modificar_coche_view(self):
        self.borrarPantalla()
        self.barraMenu()
        Label(self.ventana, text="...Ingresar el ID del coche a modificar").pack(pady=10)

        self.frame1 = Frame(self.ventana)
        self.frame1.pack(pady=10)

        Label(self.frame1, text="ID: ").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.id = Entry(self.frame1)
        self.id.focus()
        self.id.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        self.btn_buscar = Button(self.frame1, text=":: Buscar ::", command=lambda: self.accion_buscar("modificar"))
        self.btn_buscar.grid(row=0, column=2, pady=5, padx=5)

        Label(self.ventana, text="...Datos del Coche").pack(pady=10)

        self.frame2 = Frame(self.ventana)
        self.frame2.pack(pady=10)

        Label(self.frame2, text="Marca: ").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.marca = Entry(self.frame2)
        self.marca.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame2, text="Color: ").grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.color = Entry(self.frame2)
        self.color.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame2, text="Modelo: ").grid(row=3, column=0, pady=5, padx=5, sticky="e")
        self.modelo = Entry(self.frame2)
        self.modelo.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame2, text="Velocidad: ").grid(row=4, column=0, pady=5, padx=5, sticky="e")
        self.velocidad = Entry(self.frame2)
        self.velocidad.grid(row=4, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame2, text="Potencia: ").grid(row=5, column=0, pady=5, padx=5, sticky="e")
        self.potencia = Entry(self.frame2)
        self.potencia.grid(row=5, column=1, pady=5, padx=5, sticky="w")

        Label(self.frame2, text="# de Asientos: ").grid(row=6, column=0, pady=5, padx=5, sticky="e")
        self.asientos = Entry(self.frame2)
        self.asientos.grid(row=6, column=1, pady=5, padx=5, sticky="w")

        self.btn_modificar = Button(self.frame2, text=":: Modificar ::", state="disabled", command=self.accion_modificar)
        self.btn_modificar.grid(row=7, column=0, pady=10, padx=5, sticky="e")

        Button(self.frame2, text=":: Regresar ::", command=self.menu_acciones).grid(row=7, column=1, pady=10, padx=5, sticky="w")

    # .... Métodos de enlace con el Controlador ....
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title=":: Exitoso ::", message="...¡Acción Realizada con Éxito!...")
        else:
            messagebox.showerror(title=":: Verifique por favor ::", message="...¡Esta Acción no pudo realizarse en este momento!...")

    def accion_insertar(self):
        respuesta = CochesController.insertar_coche(
            self.marca.get(),
            self.color.get(),
            self.modelo.get(),
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )
        self.respuesta_sql(respuesta)
        self.insertar_coche_view()

    def accion_eliminar(self):
        id_coche = self.id.get()
        if self.confirmar_eliminacion("eliminar"):
            respuesta = CochesController.eliminar_coche(id_coche)
        else:
            respuesta = False
        self.respuesta_sql(respuesta)
        self.eliminar_coche_view()

    def llenar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in CochesController.consultar_coches():
            self.tree.insert("", "end", values=row)

    def accion_modificar(self):
        respuesta = CochesController.modificar_coche(
            self.id.get(),
            self.marca.get(),
            self.color.get(),
            self.modelo.get(),
            self.velocidad.get(),
            self.potencia.get(),
            self.asientos.get()
        )
        self.respuesta_sql(respuesta)
        self.modificar_coche_view()

    def accion_buscar(self, tipo_accion):
        coche = CochesController.buscar_coche(self.id.get())
        if len(coche) > 0:
            messagebox.showinfo(
                title="...¡ Registro Encontrado !...",
                message=f"...¡El registro fue encontrado con éxito, puedes {tipo_accion}!..."
            )
            self.cambiar_estado_btn(True, tipo_accion)
            if tipo_accion == "modificar":
                campos = [self.marca, self.color, self.modelo, self.velocidad, self.potencia, self.asientos]
                for idx, campo in enumerate(campos, start=1):
                    campo.delete(0, "end")
                    campo.insert(0, coche[0][idx])
        else:
            messagebox.showerror(
                title="...¡Verifica por favor!...",
                message=f"...¡El registro no fue encontrado, no es posible {tipo_accion}!..."
            )
            self.cambiar_estado_btn(False, tipo_accion)

    def cambiar_estado_btn(self, estado, tipo_accion):
        nuevo_estado = "normal" if estado else "disabled"
        if tipo_accion == "eliminar":
            self.btn_eliminar.config(state=nuevo_estado)
        elif tipo_accion == "modificar":
            self.btn_modificar.config(state=nuevo_estado)

    def confirmar_eliminacion(self, tipo):
        resp = messagebox.askquestion(title="...¡Atención!...", message=f"...¿Desea {tipo} este registro?...")
        return resp == "yes"