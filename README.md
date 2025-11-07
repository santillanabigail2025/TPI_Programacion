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
- Cada país se almacena con los campos: nombre, poblacion, superficie, continente.
Importante: Si el archivo paises.csv no existe en la misma carpeta que el script, el programa lo creará automáticamente con 8 países de ejemplo la primera vez que se ejecute.

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
7. Mostrar Estadísticas: Calcula y muestra:
   - País con mayor y menor población.
   - Promedio de población.
   - Promedio de superficie.
   - Conteo de países por continente.
9. Mostrar Todos los Países: Imprime un listado de todos los países (ordenados por nombre).
10. Salir (y Guardar Cambios): Termina el programa y guarda todos los cambios (países nuevos o actualizados) en el archivo paises.csv.

### Instrucciones de uso
Requisitos
- Tener Python 3 instalado.

#### Pasos para ejecutar
1. Guardar el archivo: Guarde el código Python en un archivo con el nombre main.py (o el nombre que prefiera).
2. Abrir una terminal: Abra una consola o terminal.
3. Navegar a la carpeta: Use el comando cd para moverse a la carpeta donde guardó el archivo main.py.
4. Ejecutar el script: Inicie el programa usando Python
5. Primera ejecución: La primera vez que lo ejecute, el programa detectará que paises.csv no existe, lo creará con 8 países de base y luego cargará los datos.
6. Usar el menú: Siga las instrucciones en pantalla. Ingrese el número de la opción que desea y presione Enter.
7. Guardar y Salir: Para asegurarse de que todos sus cambios (países agregados o actualizados) se guarden permanentemente, debe salir usando la opción 8. Si cierra la terminal directamente, los cambios de esa sesión se perderán.
