# Ejercicio-001

### Generar un ejemplo en lenguaje Python que permita leer la información de un archivo txt

- Solo se debe usar la librería estándar de Python (no instalar librerías adicionales).
- Leer la información del archivo **informacion.txt**
- El script generado debe imprimir de forma detallada la información de cada línea de archivo.

### Desarrollo del ejercicio

**Opción 1**

```python
archivo = open("informacion.txt")
print(archivo.read())
```

**Opción 2**

```python
with open("informacion.txt") as archivo:
    for linea in archivo:
        print(linea)
```

**Opción 3**

**Tomado de <a href="https://github.com/herramientas-ia-maestria-aa2024/ejercicio-001-isaiasilvadh" target="_blank">isaiasilvadh</a> por manejo de excepciones**

```python
nombre_archivo = "informacion.txt"
try:
    # Abrir el archivo
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea.rstrip())
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se encontró.")
```
