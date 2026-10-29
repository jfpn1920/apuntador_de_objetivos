import random
ids = []
nombres = []
descripciones = []
categorias = []
fechas_inicio = [] 
fechas_limite = []
prioridades = []
estados = []
observaciones = []
#-------------------------------------------#
#--|menu_principal_apuntador_de_objetivos|--#
#-------------------------------------------#
while True:
    print("menu principal apuntador de objetivos")
    print("1) crear objetivo")
    print("2) editar objetivo")
    print("3) eliminar objetivo")
    print("4) buscar objetivo")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_objetivo|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_objetivo = 1
        else:
            id_objetivo = ids[-1] + 1
        nombre = input("nombre del objetivo: ")
        descripcion = input("descripción: ")
        categoria = input("categoría: ")
        fecha_inicio = input("fecha de inicio: ")
        fecha_limite = input("fecha límite: ")
        prioridad = input("prioridad (alta, media o baja): ")
        estado = input("estado (pendiente, en progreso o completado): ")
        observacion = input("observación: ")
        ids.append(id_objetivo)
        nombres.append(nombre)
        descripciones.append(descripcion)
        categorias.append(categoria)
        fechas_inicio.append(fecha_inicio)
        fechas_limite.append(fecha_limite)
        prioridades.append(prioridad)
        estados.append(estado)
        observaciones.append(observacion)
        print("objetivo registrado correctamente.")
        print("id:", id_objetivo)
    #---------------------#
    #--|editar_objetivo|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen objetivos registrados.")
        else:
            print("editar objetivo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {prioridades[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del objetivo: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {estados[posicion]}")
                nombres[posicion] = input("nuevo nombre: ")
                descripciones[posicion] = input("nueva descripción: ")
                categorias[posicion] = input("nueva categoría: ")
                fechas_inicio[posicion] = input("nueva fecha de inicio: ")
                fechas_limite[posicion] = input("nueva fecha límite: ")
                prioridades[posicion] = input("nueva prioridad: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("objetivo actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_objetivo|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen objetivos registrados.")
        else:
            print("eliminar objetivo")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del objetivo: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del objetivo")
                print(f"{ids[posicion]} | {nombres[posicion]} | {estados[posicion]}")
                respuesta = input("¿desea eliminar este objetivo? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    descripciones.pop(posicion)
                    categorias.pop(posicion)
                    fechas_inicio.pop(posicion)
                    fechas_limite.pop(posicion)
                    prioridades.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("objetivo eliminado correctamente.")
                else:
                    print("el objetivo no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_objetivo|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen objetivos registrados.")
        else:
            print("buscar objetivo")
            id_buscar = int(input("ingrese la id del objetivo: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("descripción:", descripciones[posicion])
                print("categoría:", categorias[posicion])
                print("fecha de inicio:", fechas_inicio[posicion])
                print("fecha límite:", fechas_limite[posicion])
                print("prioridad:", prioridades[posicion])
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen objetivos registrados.")
        else:
            pendientes = 0
            en_progreso = 0
            completados = 0
            prioridad_alta = 0
            prioridad_media = 0
            prioridad_baja = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {prioridades[i]} | {estados[i]}")
                if estados[i].lower() == "pendiente":
                    pendientes += 1
                elif estados[i].lower() == "en progreso":
                    en_progreso += 1
                elif estados[i].lower() == "completado":
                    completados += 1
                if prioridades[i].lower() == "alta":
                    prioridad_alta += 1
                elif prioridades[i].lower() == "media":
                    prioridad_media += 1
                elif prioridades[i].lower() == "baja":
                    prioridad_baja += 1
            print("estadísticas apuntador de objetivos")
            print("cantidad de objetivos:", len(ids))
            print("pendientes:", pendientes)
            print("en progreso:", en_progreso)
            print("completados:", completados)
            print("prioridad alta:", prioridad_alta)
            print("prioridad media:", prioridad_media)
            print("prioridad baja:", prioridad_baja)
            posicion = random.randint(0, len(ids) - 1)
            print("objetivo seleccionado")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("descripción:", descripciones[posicion])
            print("categoría:", categorias[posicion])
            print("fecha de inicio:", fechas_inicio[posicion])
            print("fecha límite:", fechas_limite[posicion])
            print("prioridad:", prioridades[posicion])
            print("estado:", estados[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el apuntador de objetivos.")
        break
    else:
        print("opción no válida.")