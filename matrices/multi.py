def main():
    while True:
        try:
            filas_m1 = int(input("Número de filas de la Matriz 1: "))
            columnas_m1 = int(input("Número de columnas de la Matriz 1: "))
            filas_m2 = int(input("Número de filas de la Matriz 2: "))
            columnas_m2 = int(input("Número de columnas de la Matriz 2: "))
            
            # Validar que las dimensiones sean válidas para la multiplicación
            if filas_m1 <= 0 or columnas_m1 <= 0 or filas_m2 <= 0 or columnas_m2 <= 0:
                print("Error: Las dimensiones deben ser números enteros positivos.")
                continue
                
            if columnas_m1 != filas_m2:
                print("Error: El número de columnas de la Matriz 1 debe ser igual al número de filas de la Matriz 2.")
                continue
                
            break
        except ValueError:
            print("Error: Por favor ingrese números enteros válidos.")
    
    # Paso 2: Crear las matrices
    print("\n=== INGRESO DE DATOS DE LA MATRIZ 1 ===")
    matriz1 = crear_matriz(filas_m1, columnas_m1)
    
    print("\n=== INGRESO DE DATOS DE LA MATRIZ 2 ===")
    matriz2 = crear_matriz(filas_m2, columnas_m2)
    
    # Paso 3: Realizar la multiplicación
    print("\n=== MULTIPLICANDO MATRICES... ===")
    resultado = multiplicar_matrices(matriz1, matriz2)
    
    # Paso 4: Mostrar el resultado
    print("\n=== MATRIZ RESULTANTE ===")
    mostrar_matriz(resultado)

def crear_matriz(filas, columnas):
    """Permite al usuario ingresar los valores de una matriz fila por fila"""
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"Ingrese el valor para la posición [{i+1},{j+1}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Por favor ingrese un valor numérico válido.")
        matriz.append(fila)
    
    return matriz

def multiplicar_matrices(matriz1, matriz2):
    """Multiplica dos matrices utilizando el método iterativo estándar"""
    filas_resultado = len(matriz1)
    columnas_resultado = len(matriz2[0])
    
    # Inicializar matriz de resultado con ceros
    resultado = []
    for i in range(filas_resultado):
        resultado.append([0] * columnas_resultado)
    
    # Realizar multiplicación
    for i in range(filas_resultado):
        for j in range(columnas_resultado):
            suma = 0
            for k in range(len(matriz2)):
                suma += matriz1[i][k] * matriz2[k][j]
            resultado[i][j] = suma
    
    return resultado

def mostrar_matriz(matriz):
    """Muestra una matriz de forma ordenada en la terminal"""
    if not matriz:
        print("La matriz está vacía.")
        return
    
    for fila in matriz:
        # Formatear cada número con 6 espacios y 2 decimales
        fila_formateada = [f"{num:6.2f1}" for num in fila]
        print("[", " ".join(fila_formateada), "]")

if __name__ == "__main__":
    main()