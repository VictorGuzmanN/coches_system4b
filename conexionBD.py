import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_coches'
    )   
    cursor=conexion.cursor(buffered=True) 
except:
    messagebox.showinfo(tittle="Sistema gestor de BD...", message=f"¡Por el momento no es posible conectarse con la BD, intentelo mas tarde")

     