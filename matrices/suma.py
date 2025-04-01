def obtener_dimensiones():
    """Solicita al usuario las dimensiones de las matrices y las valida"""
    while True:
        try:
            filas = int(input("Ingrese el número de filas: "))
            columnas = int(input("Ingrese el número de columnas: "))
            
            if filas <= 0 or columnas <= 0:
                print("Error: Las dimensiones deben ser números positivos.")
                continue
                
            return filas, columnas
        except ValueError:
            print("Error: Por favor ingrese números enteros válidos.")

def crear_matriz(filas, columnas, nombre_matriz):
    """Crea una matriz con las dimensiones especificadas"""
    matriz = []
    print(f"\nIngrese los valores para la {nombre_matriz}:")
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"Valor en posición [{i+1}][{j+1}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Por favor ingrese un número válido.")
        matriz.append(fila)
    
    return matriz

def mostrar_matriz(matriz, nombre_matriz=""):
    """Muestra una matriz en la consola"""
    if nombre_matriz:
        print(f"\n{nombre_matriz}:")
    
    for fila in matriz:
        print("[",end=" ")
        for valor in fila:
            # Si el valor es entero, mostrar sin decimales
            if valor == int(valor):
                print(f"{int(valor):4}", end=" ")
            else:
                print(f"{valor:4.1f}", end=" ")
        print("]")

def sumar_matrices(matriz1, matriz2):
    """Suma dos matrices y devuelve el resultado"""
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    
    for i in range(filas):
        fila_resultado = []
        for j in range(columnas):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    
    return resultado

def main():
    print("=== SUMA DE MATRICES ===")
    print("Primero, vamos a definir las dimensiones de las matrices.")
    
    # Paso 1: Obtener dimensiones
    filas, columnas = obtener_dimensiones()
    
    # Paso 2: Crear las matrices
    matriz1 = crear_matriz(filas, columnas, "Matriz 1")
    matriz2 = crear_matriz(filas, columnas, "Matriz 2")
    
    # Mostrar las matrices ingresadas
    print("\nMatrices ingresadas:")
    mostrar_matriz(matriz1, "Matriz 1")
    mostrar_matriz(matriz2, "Matriz 2")
    
    # Paso 3: Sumar las matrices
    resultado = sumar_matrices(matriz1, matriz2)
    
    # Paso 4: Mostrar el resultado
    mostrar_matriz(resultado, "Matriz Resultante (Suma)")
    
    print("\n¡Operación completada con éxito!")

if __name__ == "__main__":
    main()