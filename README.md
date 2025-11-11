# TP Integrador - Programación I
- Materia: Programación I
- Carrera: Tecnicatura en Programación (1° Año)
- Alumnas: Abigail Santillán - Maria Paz Couchot
- Comisión: 12
- Año: 2025
  
### Descripción del programa
Este es un programa de consola desarrollado en Python para la gestión de información de países. Permite al usuario realizar operaciones básicas de CRUD (Crear, Leer, Actualizar, Borrar - en este caso es Agregar, Leer, Actualizar) sobre un conjunto de datos almacenado en un archivo paises.csv.
El sistema está enfocado en la modularización a través de funciones y el manejo de estructuras de datos fundamentales como listas y diccionarios.

#### Archivo de Datos
- El programa lee y escribe los datos desde un archivo llamado paises.csv.

- Cada país se almacena con los campos: nombre, poblacion, superficie, continente. Importante: Si el archivo paises.csv no existe en la misma carpeta que el script, el programa lo creará automáticamente con 8 países de ejemplo la primera vez que se ejecute.

### Funcionalidades Principales
El menú principal ofrece las siguientes opciones:

1. Agregar País: Permite añadir un nuevo país validando que no esté vacío y que no exista previamente.

2. Actualizar Datos: Modifica la población y/o superficie de un país existente, buscándolo por nombre.

3. Buscar País: Realiza una búsqueda por nombre (parcial o exacta) y muestra los resultados.

4. Filtrar Países: Permite filtrar la lista por:

- Continente.

- Rango de población (mínimo y máximo).

- Rango de superficie (mínimo y máximo).

5. Ordenar Países: Muestra la lista completa ordenada (ascendente o descendente) por:

- Nombre.

- Población.

- Superficie.

6. Mostrar Estadísticas: Calcula y muestra:

- País con mayor y menor población.

- Promedio de población.

- Promedio de superficie.

- Conteo de países por continente.

7. Mostrar Todos los Países: Imprime un listado de todos los países (ordenados por nombre).

8. Salir (y Guardar Cambios): Termina el programa y guarda todos los cambios (países nuevos o actualizados) en el archivo paises.csv.

### Instrucciones de uso

Requisitos

- Tener Python 3 instalado.

#### Pasos para ejecutar
1. Guardar el archivo: Guarde el código Python en un archivo con el nombre main.py.

2. Abrir una terminal: Abra una consola o terminal.

3. Navegar a la carpeta: Use el comando cd para moverse a la carpeta donde guardó el archivo main.py.

4. Ejecutar el script: Inicie el programa usando Python.

5. Primera ejecución: La primera vez que lo ejecute, el programa detectará que paises.csv no existe, lo creará con 8 países de base y luego cargará los datos.

6. Usar el menú: Siga las instrucciones en pantalla. Ingrese el número de la opción que desea y presione Enter.

7. Guardar y Salir: Para asegurarse de que todos sus cambios (países agregados o actualizados) se guarden permanentemente, debe salir usando la opción 8. Si cierra la terminal directamente, los cambios de esa sesión se perderán.

#### Ejemplos de Entradas y Salidas
Aquí se muestran algunos ejemplos de interacción con el menú del programa:

### Ejemplo 1: Filtrar Países por Continente
El usuario selecciona la opción 4, luego la sub-opción 1 e ingresa "América".
Seleccione una opción (1-8): 4

----- 4. Filtrar Países -----

Opciones de filtro:

  1. Por Continente
  2. Por Rango de Población
  3. Por Rango de Superficie
     
Seleccione una opción: 1

Ingrese el continente: América

----- 2 Países Encontrados ---
  - Argentina (Cont: América):
    Población: 45,376,763 hab.
    Superficie: 2,780,400 km²
  - Brasil (Cont: América):
    Población: 213,993,437 hab.
    Superficie: 8,515,767 km²
---------------------------------

Presione Enter para continuar...

### Ejemplo 2: Mostrar Estadísticas
El usuario selecciona la opción 6 para ver un resumen de todos los datos cargados.

Seleccione una opción (1-8): 6

----- 6. Mostrar Estadísticas -----

 - Población:
   
  Mayor población: India (1,380,004,385 hab.)
  
  Menor población: Australia (25,687,041 hab.)
  
  Población promedio: 243,400,601.50 hab.

 - Superficie:
 
  Superficie promedio: 4,965,309.25 km²

 - Países por Continente:
 
  - América: 2 país(es)
    
  - Asia: 2 país(es)

  - Europa: 2 país(es)
    
  - África: 1 país(es)
    
  - Oceanía: 1 país(es)

Presione Enter para continuar...

### Integrantes y Participación

Abigail Santillán

- Armado del informe final.

- Colaboración en algunos puntos teóricos del informe.

- Participación en el armado del código.

- Video: Explicación de las entradas y salidas del menú.

Maria Paz Couchot

- Colaboración en algunos puntos teóricos del informe.

- Armado del documento README.

- Edición completa del video.

- Video: Explicación de las funciones principales del código.

