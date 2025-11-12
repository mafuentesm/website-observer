# website-observer
Código que permite observar cambios en un sitio web —en su composición html—.

## Requisitos
- Python 3.8 o superior
- pip (administrador de paquetes)

Instala las dependencias con:
`pip install -r requirements.txt`

## Configuración

1. Abre el archivo `main.py.`

Modifica las siguientes variables según la página que quieras vigilar:

2. Modifica las siguientes variables según la página a observar:
```
URL = "http://localhost:8000/test_site.html"  # o una URL real
DIV_ID = "contenido"                          # id del div a monitorear
CHECK_INTERVAL = 10                           # segundos entre revisiones
```

## Ejecución

Simplemente ejecutar en la terminal: `python3 main.py`

Deberá aparecer en consola un mensaje como el siguiente:

```
Iniciando monitoreo de http://localhost:8000/test_site.html cada 10 s...
Contenido inicial guardado: Estado: inicial...
⚠️ Cambio detectado en el div.
```

## ¿Puedo hacer una prueba local?

Claro; basta con ejecutar el archivo `test_site.html` del repositorio. Para esto, ejecutar en terminal: `python3 -m http.server 8000` (Recuerda modificar la URL en main.py)

## Notas

- En macOS, las notificaciones se muestran con AppleScript (osascript), garantizando persistencia.
- En Windows/Linux, se usa `plyer` (si está instalado).
- Si la página no está disponible, el programa seguirá intentando cada CHECK_INTERVAL segundos.

## Autor
Prototipo desarrollado por Matias Fuentes.
