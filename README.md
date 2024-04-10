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
