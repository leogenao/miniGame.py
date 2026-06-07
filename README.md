# ⛏️ Minecraft Clone en Python (Ursina Engine)

¡Un clon minimalista y funcional de Minecraft desarrollado en Python!

Este proyecto utiliza el motor de videojuegos **Ursina Engine** para crear un entorno 3D interactivo con mecánicas básicas inspiradas en Minecraft. Incluye movimiento en primera persona, generación de terreno, construcción y destrucción de bloques.

---

## 🚀 Características

- 🎮 **Control en Primera Persona**
  - Camina, salta y explora el mundo de forma fluida.

- 🌍 **Generación de Terreno**
  - Crea automáticamente un suelo inicial de **20 × 20 bloques** al iniciar el juego.

- 🧱 **Construcción de Bloques**
  - Coloca nuevos bloques sobre cualquier cara de un bloque existente utilizando el vector normal del cursor.

- 💥 **Destrucción de Bloques**
  - Elimina bloques del escenario en tiempo real.

- 🎨 **Texturas por Defecto**
  - Utiliza `white_cube`, por lo que no requiere assets externos para funcionar.

---

## 🛠️ Requisitos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.7 o superior
- Ursina Engine

---

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO
```

### 2. Instalar dependencias

```bash
pip install ursina
```

### 3. Ejecutar el juego

```bash
python main.py
```

---

## 🎮 Controles

| Acción | Tecla / Botón |
|----------|-------------|
| Moverse | `W`, `A`, `S`, `D` |
| Saltar | `Espacio` |
| Mirar alrededor | Mover el ratón |
| Colocar bloque | Click izquierdo |
| Romper bloque | Click derecho |
| Salir del juego | `Shift + Q` |

---

## 📝 Explicación del Código

### Construcción Inteligente de Bloques

El sistema de construcción utiliza la propiedad `mouse.normal` de Ursina para detectar automáticamente la cara seleccionada de un bloque y colocar uno nuevo justo al lado.

```python
# Suma la posición del bloque seleccionado
# con el vector normal de la cara clicada
position = hit_box.position + mouse.normal
```

### Eliminación de Bloques

Cuando un bloque es destruido, se elimina tanto de la escena 3D como de la lista interna que almacena los bloques activos.

```python
boxes.remove(hit_box)
destroy(hit_box)
```

---

## 💡 Posibles Mejoras

Algunas ideas para futuras versiones:

- Diferentes tipos de bloques.
- Sistema de inventario.
- Guardado y carga de mundos.
- Generación infinita mediante ruido Perlin.
- Sistema de iluminación dinámica.
- Multijugador local o en red.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas.

Si deseas mejorar el proyecto:

1. Haz un Fork del repositorio.
2. Crea una nueva rama para tu funcionalidad.
3. Realiza tus cambios.
4. Envía un Pull Request.

También puedes abrir un Issue para reportar errores o sugerir mejoras.

---

## 📄 Licencia

Este proyecto está distribuido bajo la licencia **MIT**.

Puedes usarlo, modificarlo y distribuirlo libremente respetando los términos de dicha licencia.

---

### ⭐ Si este proyecto te resulta útil, considera darle una estrella al repositorio.
