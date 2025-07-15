import os
from datetime import datetime

productos = []

def agregar_producto(nombre, precio, cantidad):
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado.")

def mostrar_productos():
    print("\nProductos agregados:")
    for i, prod in enumerate(productos, start=1):
        print(f"{i}. {prod['nombre']} - ${prod['precio']} x {prod['cantidad']}")

def generar_factura():
    if not productos:
        print("No hay productos para facturar.")
        return

    subtotal = sum(p["precio"] * p["cantidad"] for p in productos)
    iva = subtotal * 0.16
    total = subtotal + iva

    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"facturas/factura_{fecha}.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("FACTURA\n")
        f.write("--------\n")
        for prod in productos:
            f.write(f"{prod['nombre']} - ${prod['precio']} x {prod['cantidad']}\n")
        f.write("\n")
        f.write(f"Subtotal: ${subtotal:.2f}\n")
        f.write(f"IVA (16%): ${iva:.2f}\n")
        f.write(f"TOTAL: ${total:.2f}\n")

    print(f"Factura generada: {nombre_archivo}")
    productos.clear()

while True:
    print("\n1. Agregar producto")
    print("2. Ver productos")
    print("3. Generar factura")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio: $"))
            cantidad = int(input("Cantidad: "))
            agregar_producto(nombre, precio, cantidad)
        except ValueError:
            print("Datos inválidos.")
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        generar_factura()
    elif opcion == "4":
        break
    else:
        print("Opción no válida.")
