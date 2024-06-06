"""
TRABAJO FIN DE CURSO DE PYTHON IBM.
ANGEL GUTIERREZ DEL CASTILLO.
"""
class Tarea:
    def __init__(self, descripcion):
        # Crea una tarea con una descripción y establece su estado de no completada.
        self.descripcion = descripcion  
        self.completada = False

    def completar_tarea(self):
        # Cambia el estado de la tarea a completada.
     self.completada = True

    def __str__(self):
        # Devuelve una cadena que nos indica el estado de la tarea si esta completada o pendiente.
        if self.completada:
            estado = f'Completada'
        else:
            estado = f'Pendiente'
        return f'{self.descripcion} está {estado}'


class GestordeTareas():
    def __init__(self):
        # Inicia una lista vacía para las tareas.
        self.tareas = []

    def añadir_tarea(self, descripcion):
        try:
            if descripcion.strip():  
                # Crea una nueva tarea y la agrega a la lista.
                nueva_tarea = Tarea(descripcion)       
                self.tareas.append(nueva_tarea)
                print(f'Tarea "{nueva_tarea.descripcion}" añadida correctamente.')
            else:
            # Nos dice si la descripción de la tarea está vacía.
                print(f'La descripción no puede estar vacía.')
        except Exception as e:
            # Maneja cualquier error que ocurra al añadir una tarea.
            print(f"Error al añadir tarea: {e}")

    def eliminar_tarea(self, descripcion):
        for tarea in self.tareas:
            # Busca la tarea con la descripcion dada.
            if tarea.descripcion == descripcion:
                # Confirma antes de eliminar la tarea.
                confirmacion = input(f'¿Está seguro que desea eliminar la tarea "{descripcion}"? (s/n): ')
                if confirmacion.lower() == 's':
                    # Elimina la tarea si se confirma.
                    self.tareas.remove(tarea)
                    print(f'Tarea "{descripcion}" eliminada.')
                else:
                    print('Eliminación cancelada.')
                return
        # notifica si no encuentra la tarea.
        print(f'Tarea "{descripcion}" no encontrada.')

    def mostrar_tareas(self):
        if self.tareas:
            # Muestra todas las tareas con su índice.
            for indice, tarea in enumerate(self.tareas, start = 1):
                print(f'- {indice}. {tarea}')
        else:
            # Notifica si no hay tareas en la lista.
            print('No hay tareas en la lista')
        
    def marcar_completada(self, descripcion):
        try:
            for tarea in self.tareas:
                if tarea.descripcion == descripcion:
                    # Marca la tarea como completada
                    tarea.completar_tarea()
                    print(f'Tarea "{descripcion}" marcada como completada.')
                    return
            # Informa si no encuentra la tarea.
            print(f'Tarea "{descripcion}" no encontrada.')
        except Exception as e:
            # Maneja cualquier error que ocurra al marcar una tarea como completada.
            print(f"Error al marcar tarea como completada: {e}")

def main():
    # Crea una instancia del gestor de tareas.
    gestor_tareas = GestordeTareas()

    while True:
        # Muestra el menú del Gestor de tareas.
        print('\n||| GESTOR DE TAREAS |||')
        print('-- 1. Agregar tarea')
        print('-- 2. Marcar tarea como completada')
        print('-- 3. Ver todas las tareas')
        print('-- 4. Eliminar tarea')
        print('-- 5. Salir')
        print('LISTA DE TAREAS')
        gestor_tareas.mostrar_tareas()  #Muestra la lista de tareas en pantalla. 

        # Solicita una opción al usuario.
        seleccion = input(f'Seleccione una opción: ')

        if seleccion == '1':
            # Pide una nueva tarea para añadir.
            tarea = input(f'Introduzca la nueva tarea: ')
            gestor_tareas.añadir_tarea(tarea)
        elif seleccion == '2':
            # Pide una tarea para marcar como completada.
            tarea = (input(f'Introduzca la tarea completada: '))
            gestor_tareas.marcar_completada(tarea)
        elif seleccion == '3':
            # Muestra todas las tareas.
            gestor_tareas.mostrar_tareas()
        elif seleccion == '4':
            # Solicita una tarea para eliminar
            tarea = input(f'Introduzca tarea a eliminar: ')
            gestor_tareas.eliminar_tarea(tarea)
        elif seleccion == '5':
            #Sale del programa
            print(f'Saliendo del gestor de tareas.')
            break
        else:
            # Notifica si la opción no es válida.
            print(f'Opción no válida. Inténtelo de nuevo.')

# Ejecuta la funcion principal.
main()