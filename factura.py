import os
import csv
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

    try:
        descuento = float(input("¿Qué porcentaje de descuento aplicar? (Ej: 10 para 10%) [0 si ninguno]: "))
    except ValueError:
        print("Descuento inválido. Se aplicará 0%.")
        descuento = 0.0

    subtotal = sum(p["precio"] * p["cantidad"] for p in productos)
    monto_descuento = subtotal * (descuento / 100)
    subtotal_descuento = subtotal - monto_descuento
    iva = subtotal_descuento * 0.16
    total = subtotal_descuento + iva

    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_txt = f"facturas/factura_{fecha}.txt"
    nombre_csv = f"facturas/factura_{fecha}.csv"

    # Guardar en .txt
    with open(nombre_txt, "w", encoding="utf-8") as f:
        f.write("FACTURA\n")
        f.write("--------\n")
        for prod in productos:
            f.write(f"{prod['nombre']} - ${prod['precio']} x {prod['cantidad']}\n")
        f.write("\n")
        f.write(f"Subtotal: ${subtotal:.2f}\n")
        f.write(f"Descuento ({descuento}%): -${monto_descuento:.2f}\n")
        f.write(f"Subtotal con descuento: ${subtotal_descuento:.2f}\n")
        f.write(f"IVA (16%): ${iva:.2f}\n")
        f.write(f"TOTAL: ${total:.2f}\n")

    # Guardar en .csv
    with open(nombre_csv, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Producto", "Precio Unitario", "Cantidad", "Total"])
        for prod in productos:
            total_prod = prod["precio"] * prod["cantidad"]
            writer.writerow([prod["nombre"], prod["precio"], prod["cantidad"], total_prod])
        writer.writerow([])
        writer.writerow(["Subtotal", subtotal])
        writer.writerow(["Descuento", f"-{monto_descuento}"])
        writer.writerow(["Subtotal con descuento", subtotal_descuento])
        writer.writerow(["IVA (16%)", iva])
        writer.writerow(["TOTAL", total])

    print(f"\nFactura generada en:")
    print(f" - {nombre_txt}")
    print(f" - {nombre_csv}")
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
