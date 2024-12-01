from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
import os

# Configuración del WebDriver usando Service (Selenium 4.x)
service = Service(ChromeDriverManager().install())  # Usando webdriver_manager para obtener automáticamente el chromedriver
driver = webdriver.Chrome(service=service)

# Abre la página de inicio
driver.get("http://127.0.0.1:8000/blog")
time.sleep(2)  # Espera para que la página cargue completamente

# Toma una captura de pantalla de la página principal
screenshot_name = "home_page.png"
driver.save_screenshot(screenshot_name)

# Encuentra el enlace o la sección del artículo
article_title = "Introducción a la Programación Paralela: Beneficios y Retos"
article = driver.find_element(By.PARTIAL_LINK_TEXT, article_title)

# Da click en el enlace para entrar al artículo
ActionChains(driver).move_to_element(article).click().perform()
time.sleep(2)  # Espera para que la página cargue completamente

# Toma una captura de pantalla del artículo
screenshot_article_name = "article_page.png"
driver.save_screenshot(screenshot_article_name)

# Generar reporte HTML
report_html = f"""
<html>
<head>
    <title>Reporte de Prueba Automatizada</title>
</head>
<body>
    <h1>El Futuro de la Programación: Lenguajes y Frameworks a Tener en Cuenta</h1>
    <p><b>Fecha de la prueba:</b> {datetime.now()}</p>
    <p><b>URL visitada:</b> http://127.0.0.1:8000/blog</p>
    <p><b>Artículo Visitado:</b> {article_title}</p>
    <h2>Capturas de Pantalla:</h2>
    <p><b>Captura de la página de inicio:</b></p>
    <img src="{screenshot_name}" alt="Página de Inicio" width="600"/>
    <p><b>Captura del artículo:</b></p>
    <img src="{screenshot_article_name}" alt="Artículo" width="600"/>
</body>
</html>
"""

# Guardar el reporte en un archivo HTML
report_filename = "test_report.html"
with open(report_filename, "w") as report_file:
    report_file.write(report_html)

# Cerrar el navegador
driver.quit()

print(f"Prueba completada. El reporte se ha guardado como {report_filename}.")

