#diccionarios

#producto = {"nombre":"Pollo","Precio":20,"Stock":"5"}

#print(f"nombre: {producto["nombre"]}")  
#print(f"Precio: ${producto["Precio"]}")  
#print(f"Stock: {producto["Stock"]} unidades")  

productos = [{"nombre": "Laptop", "precio": 999, "stock": 5},{"nombre": "Mouse", "precio": 25, "stock": 50},{"nombre": "Teclado", "precio": 45, "stock": 30}]

for i in productos:
    print(f"{i["nombre"]} -",f"${i["precio"]}", f"({i["stock"]} unidades)")