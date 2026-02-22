## 👋 ¡Bienvenidos usuarios a mi proyecto! gestor de tareas

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en el desarrollo de un sistema básico de registro y gestión de tareas utilizando Python. El programa permite almacenar tareas junto con su estado, que puede ser `pendiente` o `completada`, utilizando un diccionario para mantener la información organizada y accesible.

Cada tarea se guarda como clave dentro del diccionario, mientras que su estado se almacena como valor asociado. Esta estructura facilita la administración y seguimiento de las actividades, permitiendo actualizar dinámicamente el estado de cada tarea según se vaya completando o reabriendo.

El sistema funciona mediante un menú interactivo en consola que permite agregar nuevas tareas, cambiar su estado y mostrar todas las tareas registradas en cualquier momento, proporcionando una visión clara del progreso.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar diccionarios para almacenar tareas y su estado.
- Aplicar funciones para organizar la lógica del programa.
- Utilizar bucles para crear un menú interactivo continuo.
- Cambiar dinámicamente el estado de las tareas.
- Validar entradas del usuario y existencia de tareas.
- Simular un sistema básico de gestión de actividades.

#
### 🧠 Temas que se a aplicado
- Diccionarios
- Funciones
- Condicionales (`if`, `else`)
- Bucles `while`
- Recorrido de diccionarios con `for`
- Validación de existencia de claves
- Actualización de valores en diccionarios

#
### ⚙️ Funcionamiento
1. Se crea un diccionario llamado `tareas` donde:
   - La clave representa el nombre de la tarea.
   - El valor representa el estado (`pendiente` o `completada`).

2. El sistema muestra un menú con las siguientes opciones:
   - Agregar tarea.
   - Actualizar estado de tarea.
   - Mostrar todas las tareas.
   - Salir.

3. Al agregar una tarea:
   - Se valida que la tarea no exista previamente.
   - Se registra automáticamente como `pendiente`.

4. Al actualizar una tarea:
   - Se cambia su estado de `pendiente` a `completada` o viceversa.
   - Si la tarea no existe, se muestra un mensaje de advertencia.

5. El programa se ejecuta de forma continua hasta que el usuario decide salir, permitiendo administrar el flujo de tareas de manera dinámica.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```