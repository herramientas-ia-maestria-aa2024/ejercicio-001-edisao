#Opción 1
with open("informacion.txt") as archivo:
    for linea in archivo:
        print(linea)
        
#Opción 2
#archivo = open("informacion.txt")
#print(archivo.read())

# Opción 3 (Tomada de isaiasilvadh por el manejo de excepciones)
'''
nombre_archivo = "informacion.txt"
try:
    # Abrir el archivo
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea.rstrip())
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
    '''