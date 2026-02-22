tareas = {}
def agregar_tarea():
    tarea = input("ingrese el nombre de la tarea: ").capitalize()
    if tarea in tareas:
        print("esta tarea ya esta registrada.")
    else:
        tareas[tarea] = "pendiente"
        print(f"tarea '{tarea}' agregada como pendiente.")
def actualizar_tarea():
    tarea = input("ingrese el nombre de la tarea a actualizar: ").capitalize()
    if tarea in tareas:
        estado_actual = tareas[tarea]
        nuevo_estado = "completada" if estado_actual == "pendiente" else "pendiente"
        tareas[tarea] = nuevo_estado
        print(f"tarea '{tarea}' actualizada a '{nuevo_estado}'.")
    else:
        print("no se encontro la tarea.")
def mostrar_tareas():
    if not tareas:
        print("no hay tareas registradas.")
        return
    print("\n lista de tareas:")
    for tarea, estado in tareas.items():
        print(f"- {tarea}: {estado}")
def menu():
    while True:
        print("\n registro de tareas ")
        print("1. agregar tarea")
        print("2. actualizar estado de tarea")
        print("3. mostrar tareas")
        print("4. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            actualizar_tarea()
        elif opcion == "3":
            mostrar_tareas()
        elif opcion == "4":
            print("saliendo del sistema de tareas.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()