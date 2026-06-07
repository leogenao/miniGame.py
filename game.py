from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Contenedor para los bloques
boxes = []

# Crear el suelo inicial
for i in range(20):
    for j in range(20):
        box = Button(
            color=color.white, 
            model='cube', 
            position=(j, 0, i),
            texture='white_cube', # Cambiado a textura por defecto de Ursina para evitar errores si no tienes 'grass.png'
            parent=scene, 
            origin_y=0.5
        )
        boxes.append(box)

player = FirstPersonController()
Sky()

# En Ursina, es mucho más eficiente usar la función update() o 
# dejar que el motor maneje el "mouse.hovered_entity" directamente.
def input(key):
    # Verificamos si el ratón está apuntando a algo válido
    if mouse.hovered_entity and mouse.hovered_entity in boxes:
        hit_box = mouse.hovered_entity
        
        # Clonar / Construir bloque (Click izquierdo)
        if key == 'left mouse down':
            new = Button(
                color=color.white, 
                model='cube', 
                position=hit_box.position + mouse.normal, # Usa la normal del vector para saber qué cara tocaste
                texture='white_cube', 
                parent=scene, 
                origin_y=0.5
            )
            boxes.append(new)
            
        # Destruir bloque (Click derecho)
        if key == 'right mouse down':
            boxes.remove(hit_box)
            destroy(hit_box)

app.run()
