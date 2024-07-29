from dia3.models import Tarea, SubTarea

def crear_tarea (descripcion):
  t = Tarea(descripcion=descripcion)
  t.save()
  imprimir_en_pantalla()


def recuperar_tareas_y_subtareas():
  tareas = Tarea.objects.filter(eliminada=False)
  return tareas

def eliminar_tarea(tarea_id):
  t = Tarea.objects.get(id=tarea_id)
  t.eliminada = True
  t.save()

def crear_sub_tarea(tarea_id, descripcion):
  t = Tarea.objects.get(id=tarea_id)
  st = SubTarea(descripcion=descripcion, tarea=t)
  st.save()

  imprimir_en_pantalla()


def imprimir_en_pantalla():
  tareas = recuperar_tareas_y_subtareas()
  for t in tareas:
    print (f'{t.id} {t.descripcion}')
    for st in t.subtareas.filter(eliminada=False):
      print (f'  {t.id} {st.id} {st.descripcion}')