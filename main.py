import sqlite3

coneccion = sqlite3.connect("inventario.db")
cursor = coneccion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        autor TEXT NOT NULL,
        genero TEXT NOT NULL,
        precio FLOAT NOT NULL,
        stock INTEGER NOT NULL
    )
""")
print("Tabla creada o ya existe.")

coneccion.commit()
coneccion.close()

def agregarLibro(nombre,autor,genero,precio,stock):
    coneccion = sqlite3.connect("inventario.db")
    cursor = coneccion.cursor()
    cursor.execute("INSERT INTO libros (nombre, autor, genero, precio, stock) VALUES(?,?,?,?,?)",(nombre,autor,genero,precio,stock))
    coneccion.commit()
    print("Se agrego el libro exitosamente.")
    coneccion.close()

def borrarLibro(id):
    coneccion = sqlite3.connect("inventario.db")
    cursor = coneccion.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?",(id,))
    coneccion.commit()
    print("Libro eliminado.")
    coneccion.close()

def actualizarStock(id,nuevoStock):
    coneccion = sqlite3.connect("inventario.db")
    cursor = coneccion.cursor()
    cursor.execute("UPDATE libros SET stock = ? WHERE id = ?",(nuevoStock,id))
    coneccion.commit()
    print("Stock actualizado.")
    coneccion.close()

def menu():
    while True:
        print("\n---------Menu de inventario.---------\n1.Ver stock detallado.\n2.Reporte de bajo stock.\n3.Agregar un nuevo libro.\n4.Borrar un libro.\n5.Actualizar stock.\n0.Salir.")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            coneccion = sqlite3.connect("inventario.db")
            cursor = coneccion.cursor()
            cursor.execute("SELECT * FROM libros")
            filas = cursor.fetchall()
            for fila in filas:
                print(f"ID:{fila[0]} | Nombre:{fila[1]} | Autor:{fila[2]} | Genero:{fila[3]} | Precio:{fila[4]} | Stock:{fila[5]}")
            coneccion.close()
        elif opcion == "2":
            coneccion = sqlite3.connect("inventario.db")
            cursor = coneccion.cursor()
            cursor.execute("SELECT * FROM libros")
            filas = cursor.fetchall()
            print("Lista de libros con bajo stock:")
            for fila in filas:
                if fila[5] < 25:
                    print(f"ID:{fila[0]} | Nombre:{fila[1]} | Stock:{fila[5]}")
            coneccion.close()
        elif opcion == "3":
            nombre = input ("Nombre del libro: ")
            autor = input("Autor del libro: ")
            genero = input("Genero: ")
            precio = float(input("Valor unitario del libro: "))
            stock = int(input("Stock disponible:"))
            agregarLibro(nombre,autor,genero,precio,stock)
            print("Nuevo stock: ")
            coneccion = sqlite3.connect("inventario.db")
            cursor = coneccion.cursor()
            cursor.execute("SELECT * FROM libros")
            filas = cursor.fetchall()
            for fila in filas:
                print(f"ID:{fila[0]} | Nombre:{fila[1]} | Autor:{fila[2]} | Genero:{fila[3]} | Precio:{fila[4]} | Stock:{fila[5]}")
            coneccion.close()

        elif opcion == "4":
            coneccion = sqlite3.connect("inventario.db")
            cursor = coneccion.cursor()
            cursor.execute("SELECT * FROM libros")
            filas = cursor.fetchall()
            for fila in filas:
                print(f"ID:{fila[0]} | Nombre:{fila[1]}")
            coneccion.close()
            id = int(input("ID del libro a eliminar:"))
            borrarLibro(id)
        elif opcion == "5":
            coneccion = sqlite3.connect("inventario.db")
            cursor = coneccion.cursor()
            cursor.execute("SELECT * FROM libros")
            filas = cursor.fetchall()
            for fila in filas:
                print(f"ID:{fila[0]} | Nombre:{fila[1]} | Stock:{fila[5]}")
            coneccion.close()
            id = int(input("ID del stock a actualizar: "))
            nuevoStock = int(input("Nuevo stock: "))
            actualizarStock(id,nuevoStock)
        elif opcion == "0":
            print("Saliendo del menu.")
            break
        else:
            print("Opcion invalida. Ingrese un valor valido.")
        
menu()

