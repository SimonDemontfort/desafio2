from dia3.models import Tarea, SubTarea

def crear_tarea (descripcion):
  t = Tarea(descripcion=descripcion)
  t.save()
  imprimir_en_pantalla()


def recuperar_tareas_y_subtareas():
  tareas = Tarea.objects.filter(eliminada=False)
  return tareas

def eliminar_tarea(tarea_id):
  # 1. Obtengo la tarea que deseo eliminar
  t = Tarea.objects.get(id=tarea_id)
  # 2. Modifico su atributo "eliminada"
  t.eliminada = True
  # 3. Guardo los cambios ebn base de datos
  t.save()

def crear_sub_tarea(tarea_id, descripcion):
  # 1. Obtengo la tarea
  t = Tarea.objects.get(id=tarea_id)
  # 2. Creo una nueva sub-tarea
  st = SubTarea(descripcion=descripcion, tarea=t)
  # 3. Guardamos la subtarea
  st.save()

  imprimir_en_pantalla()


def imprimir_en_pantalla():
  tareas = recuperar_tareas_y_subtareas()
  for t in tareas:
    print (f'{t.id} {t.descripcion}')
    for st in t.subtareas.filter(eliminada=False):
      print (f'  {t.id} {st.id} {st.descripcion}')