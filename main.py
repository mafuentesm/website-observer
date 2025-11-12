import time
import requests
import platform
from bs4 import BeautifulSoup
from plyer import notification
from dotenv import load_dotenv
import os

# Cargar variables de entorno (opcional)
load_dotenv()

URL = "http://127.0.0.1:5500/portal-uc-observer-no-login/test_site.html"  # reemplaza con la página a monitorear
DIV_ID = "mi-div"         # ID del div que quieres vigilar
CHECK_INTERVAL = 10          # segundos entre revisiones

def fetch_page(url: str) -> str:
    """Descarga el HTML de una página."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error al acceder a la página: {e}")
        return ""

def extract_div_content(html: str, div_id: str) -> str:
    """Extrae el contenido del div especificado."""
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", id=div_id)
    return div.get_text(strip=True) if div else ""

def notify_change():
    """Notificación persistente con ventana modal en macOS."""
    message = f"¡Los horarios banner fueron subidos! El contenido del div '{DIV_ID}' ha cambiado."
    title = "⚠️ Cambio detectado en la página"

    if platform.system() == "Darwin":  # macOS
        script = f'''
        osascript -e 'display dialog "{message}" with title "{title}" buttons {{"OK"}} default button "OK"'
        '''
        os.system(script)
    else:
        try:
            from plyer import notification
            notification.notify(
                title=title,
                message=message,
                timeout=0  # no todos los SO respetan 0 = persistente
            )
        except Exception as e:
            print(f"(Aviso) No se pudo mostrar la notificación: {e}")

def monitor_page():
    """Monitorea la página y notifica si hay cambios."""
    last_content = None
    print(f"Iniciando monitoreo de {URL} cada {CHECK_INTERVAL} s...")

    while True:
        html = fetch_page(URL)
        if not html:
            time.sleep(CHECK_INTERVAL)
            continue

        current_content = extract_div_content(html, DIV_ID)

        if last_content is None:
            last_content = current_content
            print(f"Contenido inicial guardado: {current_content[:50]}...")
        elif current_content != last_content:
            print("⚠️ Cambio detectado en el div.")
            notify_change()
            last_content = current_content

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_page()
