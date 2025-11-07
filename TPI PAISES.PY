import csv
import os

# Constantes Globales (solo lectura)
ARCHIVO_DATOS = 'paises.csv'
CAMPOS_CSV = ['nombre', 'poblacion', 'superficie', 'continente']

# Datos base para crear el archivo CSV si no existe
DATOS_BASE = [
    ['Argentina', 45376763, 2780400, 'América'],
    ['Japón', 125800000, 377975, 'Asia'],
    ['Brasil', 213993437, 8515767, 'América'],
    ['Alemania', 83149300, 357022, 'Europa'],
    ['Egipto', 102334404, 1002450, 'África'],
    ['Australia', 25687041, 7692024, 'Oceanía'],
    ['Rusia', 145934462, 17098242, 'Europa'],
    ['India', 1380004385, 3287263, 'Asia']
]

# Funciones de Utilidad y Validación

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_entero_positivo(mensaje):
    """Solicita un entero positivo válido y lo devuelve."""
    while True:
        valor_str = input(mensaje)
        # .isdigit() comprueba si todos los caracteres son números y es positivo
        if valor_str.isdigit():
            return int(valor_str)
        else:
            print("Error: Debe ingresar un número entero positivo.")

def validar_string_no_vacio(mensaje):
    """Solicita un string no vacío y lo devuelve."""
    while True:
        valor = input(mensaje).strip()
        if valor: # Si el string no está vacío
            return valor
        else:
            print("Error: Este campo no puede estar vacío.")

def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\nPresione Enter para continuar...")

def buscar_pais_por_nombre(paises, nombre):
    """Busca un país por nombre exacto (ignorando mayúsculas/minúsculas)."""
    nombre_lower = nombre.lower()
    for pais in paises:
        if pais['nombre'].lower() == nombre_lower:
            return pais
    return None # Devuelve None si no encuentra nada

def formatear_pais(pais):
    """Devuelve un string formateado con los datos de un país."""
    # Usamos f-strings para formatear. Los ':' agregan separadores de miles
    return f"  - {pais['nombre']} (Cont: {pais['continente']}):\n" \
           f"    Población: {pais['poblacion']:,} hab.\n" \
           f"    Superficie: {pais['superficie']:,} km²"

def mostrar_paises(lista_paises):
    """Imprime una lista de países de forma legible."""
    if not lista_paises:
        print("\nNo se encontraron países que coincidan con la búsqueda.")
        return
    
    print(f"\n----- {len(lista_paises)} Países Encontrados ---")
    for pais in lista_paises:
        print(formatear_pais(pais))
    print("---------------------------------")

# Funciones para Ordenamiento

def obtener_nombre(pais):
    """Devuelve el nombre de un país (para usar en 'key' de sorted)."""
    return pais['nombre']

def obtener_poblacion(pais):
    """Devuelve la población de un país (para usar en 'key' de sorted)."""
    return pais['poblacion']

def obtener_superficie(pais):
    """Devuelve la superficie de un país (para usar en 'key' de sorted)."""
    return pais['superficie']

# Funciones de Carga y Guardado

def inicializar_datos():
    """
    Crea el archivo CSV con datos base si no existe.
    Esta función cumple con el requisito de crear el CSV con 8 países.
    """
    if not os.path.exists(ARCHIVO_DATOS):
        print(f"No se encontró '{ARCHIVO_DATOS}'. Creando archivo con datos base...")
        # Usamos 'with open' para crear y escribir en el archivo de forma segura
        with open(ARCHIVO_DATOS, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(CAMPOS_CSV) # Escribe el encabezado
            writer.writerows(DATOS_BASE) # Escribe los 8 países
        print("Archivo creado exitosamente.")

def cargar_datos(archivo):
    """Carga los datos de países desde un archivo CSV (sin try/except)."""
    paises = []
    
    # Si el archivo no existe (aunque inicializar_datos ya lo creó)
    if not os.path.exists(archivo):
        print(f"Error fatal: Archivo '{archivo}' no encontrado.")
        return []

    with open(archivo, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # Validamos que las cabeceras sean correctas
        if reader.fieldnames != CAMPOS_CSV:
            print(f"Error: Cabeceras del CSV incorrectas. Se esperaba: {CAMPOS_CSV}")
            return [] # Devolvemos lista vacía

        for row in reader:
            nombre = row.get('nombre', '').strip()
            poblacion_str = row.get('poblacion', '')
            superficie_str = row.get('superficie', '')
            continente = row.get('continente', '').strip()

            # Verificamos que los campos de texto no estén vacíos
            # y que los campos numéricos sean dígitos
            if (nombre and continente and 
                poblacion_str.isdigit() and 
                superficie_str.isdigit()):
                
                pais = {
                    'nombre': nombre,
                    'poblacion': int(poblacion_str),
                    'superficie': int(superficie_str),
                    'continente': continente
                }
                paises.append(pais)
            else:
                # Control de errores de formato en el CSV (línea por línea)
                print(f"Advertencia: Se omitió una línea del CSV por formato incorrecto.")
    
    return paises

def guardar_datos(archivo, paises):
    """Guarda la lista de países en el archivo CSV (sin try/except)."""
    with open(archivo, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS_CSV)
        writer.writeheader() # Escribe la cabecera
        writer.writerows(paises) # Escribe todos los datos
    print(f"Datos guardados exitosamente en '{archivo}'.")

# Funcionalidades del Menú

def agregar_pais(paises):
    """Agrega un nuevo país a la lista."""
    print("----- 1. Agregar País -----")
    nombre = validar_string_no_vacio("Nombre del país: ").capitalize()
    
    # Validar que el país no exista ya
    if buscar_pais_por_nombre(paises, nombre):
        print("Error: Ya existe un país con ese nombre.")
        return

    poblacion = validar_entero_positivo("Población: ")
    superficie = validar_entero_positivo("Superficie (km²): ")
    continente = validar_string_no_vacio("Continente: ").capitalize()
    
    nuevo_pais = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    paises.append(nuevo_pais)
    print(f"\n¡País '{nombre}' agregado con éxito!")

def actualizar_pais(paises):
    """Actualiza la población y superficie de un país existente."""
    print("----- 2. Actualizar País -----")
    nombre = validar_string_no_vacio("Ingrese el nombre del país a actualizar: ")
    
    pais_encontrado = buscar_pais_por_nombre(paises, nombre)
    
    if pais_encontrado:
        print("\nDatos actuales:")
        print(formatear_pais(pais_encontrado))
        print("\nIngrese los nuevos datos (deje en blanco para no cambiar):")

        # Actualizar Población
        nueva_poblacion_str = input(f"Nueva población (actual: {pais_encontrado['poblacion']:,}): ").strip()
        if nueva_poblacion_str: # Si el usuario escribió algo
            if nueva_poblacion_str.isdigit():
                pais_encontrado['poblacion'] = int(nueva_poblacion_str)
            else:
                print("Entrada de población inválida. No se actualizó.")

        # Actualizar Superficie 
        nueva_superficie_str = input(f"Nueva superficie (actual: {pais_encontrado['superficie']:,}): ").strip()
        if nueva_superficie_str: # Si el usuario escribió algo
            if nueva_superficie_str.isdigit():
                pais_encontrado['superficie'] = int(nueva_superficie_str)
            else:
                print("Entrada de superficie inválida. No se actualizó.")

        print("\n¡País actualizado con éxito!")
        print(formatear_pais(pais_encontrado))
    else:
        print("Error: País no encontrado.")

def buscar_pais(paises):
    """Busca países por coincidencia parcial o exacta."""
    print("----- 3. Buscar País por Nombre -----")
    termino = validar_string_no_vacio("Ingrese el nombre (o parte) a buscar: ").lower()
    
    resultados = []
    for pais in paises:
        if termino in pais['nombre'].lower():
            resultados.append(pais)
            
    mostrar_paises(resultados)

def filtrar_paises(paises):
    """Filtra países por continente, rango de población o superficie."""
    print("----- 4. Filtrar Países -----")
    print("Opciones de filtro:")
    print("  1. Por Continente")
    print("  2. Por Rango de Población")
    print("  3. Por Rango de Superficie")
    opcion = input("Seleccione una opción: ")

    resultados = []
    if opcion == '1':
        continente = validar_string_no_vacio("Ingrese el continente: ").lower()
        # Usamos un bucle for normal para el filtro
        for p in paises:
            if p['continente'].lower() == continente:
                resultados.append(p)
    
    elif opcion == '2':
        min_pob = validar_entero_positivo("Población mínima: ")
        max_pob = validar_entero_positivo(f"Población máxima (mín: {min_pob:,}): ")
        if max_pob < min_pob:
            print("Error: La población máxima no puede ser menor a la mínima.")
            return
        
        for p in paises:
            if min_pob <= p['poblacion'] <= max_pob:
                resultados.append(p)

    elif opcion == '3':
        min_sup = validar_entero_positivo("Superficie mínima: ")
        max_sup = validar_entero_positivo(f"Superficie máxima (mín: {min_sup:,}): ")
        if max_sup < min_sup:
            print("Error: La superficie máxima no puede ser menor a la mínima.")
            return
        
        for p in paises:
            if min_sup <= p['superficie'] <= max_sup:
                resultados.append(p)
    
    else:
        print("Opción inválida.")
        return

    mostrar_paises(resultados)

def ordenar_paises(paises):
    """Ordena la lista de países por el criterio y orden seleccionados."""
    print("----- 5. Ordenar Países -----")
    print("Criterio de orden:")
    print("  1. Nombre")
    print("  2. Población")
    print("  3. Superficie")
    criterio = input("Seleccione un criterio: ")

    if criterio not in ['1', '2', '3']:
        print("Criterio inválido.")
        return

    print("\nOrden:")
    print("  1. Ascendente (A-Z, Menor a Mayor)")
    print("  2. Descendente (Z-A, Mayor a Menor)")
    orden = input("Seleccione un orden: ")

    if orden not in ['1', '2']:
        print("Orden inválido.")
        return

    # Determinar si el orden es descendente (reverse=True)
    descendente = (orden == '2')
    
    # Asignamos la FUNCIÓN adecuada
    if criterio == '1':
        clave_orden = obtener_nombre
        print("\n----- Países ordenados por Nombre -----")
    elif criterio == '2':
        clave_orden = obtener_poblacion
        print("\n----- Países ordenados por Población -----")
    else: # criterio == '3'
        clave_orden = obtener_superficie
        print("\n----- Países ordenados por Superficie -----")

    # Creamos una *nueva* lista ordenada (sorted)
    # y le pasamos el nombre de nuestra función en 'key'
    paises_ordenados = sorted(paises, key=clave_orden, reverse=descendente)
    
    mostrar_paises(paises_ordenados)

def mostrar_estadisticas(paises):
    """Calcula y muestra estadísticas clave sobre los datos."""
    print("----- 6. Mostrar Estadísticas -----")
    
    if not paises:
        print("No hay datos para calcular estadísticas.")
        return

    # 1. País con mayor y menor población (usando las funciones helper)
    pais_max_pob = max(paises, key=obtener_poblacion)
    pais_min_pob = min(paises, key=obtener_poblacion)
    
    print("\nPoblación:")
    print(f"  Mayor población: {pais_max_pob['nombre']} ({pais_max_pob['poblacion']:,} hab.)")
    print(f"  Menor población: {pais_min_pob['nombre']} ({pais_min_pob['poblacion']:,} hab.)")

    # 2. Promedio de población
    total_poblacion = 0
    for p in paises:
        total_poblacion += p['poblacion']
    promedio_poblacion = total_poblacion / len(paises)
    print(f"Población promedio: {promedio_poblacion:,.2f} hab.")

    # 3. Promedio de superficie
    total_superficie = 0
    for p in paises:
        total_superficie += p['superficie']
    promedio_superficie = total_superficie / len(paises)
    print(f"\nSuperficie:")
    print(f" Superficie promedio: {promedio_superficie:,.2f} km²")

    # 4. Cantidad de países por continente
    print("\nPaíses por Continente:")
    conteo_continentes = {}
    for pais in paises:
        continente = pais['continente']
        # .get(continente, 0) devuelve el valor actual o 0 si no existe
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1
    
    # Imprimimos el diccionario de conteo
    for continente, cantidad in conteo_continentes.items():
        print(f"  - {continente}: {cantidad} país(es)")

# Función Principal (Main)

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    limpiar_pantalla()
    print("========================================")
    print("Sistema de Gestión de Países")
    print("========================================")
    print(" 1. Agregar País")
    print(" 2. Actualizar Datos de País")
    print(" 3. Buscar País por Nombre")
    print(" 4. Filtrar Países")
    print(" 5. Ordenar Países")
    print(" 6. Mostrar Estadísticas")
    print(" 7. Mostrar Todos los Países")
    print(" 8. Salir (y Guardar Cambios)")
    print("----------------------------------------")

def main():
    """Función principal que ejecuta el bucle del programa."""
    
    # 1. Verificamos y creamos el CSV si es necesario
    inicializar_datos()
    
    # 2. Cargamos los datos del CSV
    lista_paises = cargar_datos(ARCHIVO_DATOS)
    
    print(f"Cargados {len(lista_paises)} países.")
    pausar()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            agregar_pais(lista_paises)
        elif opcion == '2':
            actualizar_pais(lista_paises)
        elif opcion == '3':
            buscar_pais(lista_paises)
        elif opcion == '4':
            filtrar_paises(lista_paises)
        elif opcion == '5':
            ordenar_paises(lista_paises)
        elif opcion == '6':
            mostrar_estadisticas(lista_paises)
        elif opcion == '7':
            print("\n--- Listado Completo de Países ---")
            # Ordenamos por nombre por defecto para la vista completa
            paises_ordenados = sorted(lista_paises, key=obtener_nombre)
            mostrar_paises(paises_ordenados)
        elif opcion == '8':
            guardar_datos(ARCHIVO_DATOS, lista_paises)
            print("¡Hasta luego!")
            break # Termina el bucle while
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        
        pausar()

# --- Punto de Entrada del Script ---
# Esto asegura que main() solo se ejecute cuando se corre el script directamente
if __name__ == "__main__":
    main()