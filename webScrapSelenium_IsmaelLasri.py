import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

 # Configuro el navegador perquè funcioni en mode headless, sense interfície

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Entro a la pàgina de resultats de "laptops" a Amazon

driver.get("https://www.amazon.com/s?k=laptops")
time.sleep(5)
print("Titol de la pàgina:", driver.title)

# Agafo els elements que interessen de cada producte.

elements = driver.find_elements(By.CLASS_NAME, "a-size-medium")
precios = driver.find_elements(By.CLASS_NAME, "a-price-whole")
centimillos = driver.find_elements(By.CLASS_NAME, "a-price-fraction")
link = driver.find_elements(By.CSS_SELECTOR, "a.a-link-normal.s-line-clamp-2.s-link-style.a-text-normal")
foto = driver.find_elements(By.CSS_SELECTOR, "img.s-image")
valoracions = driver.find_elements(By.CSS_SELECTOR, "span.a-size-base.s-underline-text")
comprasMeS= driver.find_elements(By.XPATH, ".//span[contains(text(),'comprados')]") #he utilitzat xpath per a filtrar i aixi aconseguir un resultat precís, he filtrar per "comprados".


# Creo les carpetes i subcarpetes.

if not os.path.exists("CarpetaScrap"):
    os.mkdir("CarpetaScrap")

if not os.path.exists("CarpetaScrap/Imatges"):
    os.mkdir("CarpetaScrap/Imatges")

if not os.path.exists("CarpetaScrap/CSV"):
    os.mkdir("CarpetaScrap/CSV")

if not os.path.exists("CarpetaScrap/HTML"):
    os.mkdir("CarpetaScrap/HTML")

a=0
laptops = []


for nombre in elements[:10]: # Agafo informació dels primers 10 productes
    nom = nombre.text
    
    try:
        valor = valoracions[a].text
    except:
        valor = "No disponible"

    try:
        compras = comprasMeS[a].text
    except:
        compras = "No disponible"

    try:
        preu = precios[a].text + "," + centimillos[a].text
    except:
        preu = "No disponible"

    try:
        enllaç = link[a].get_attribute("href")
    except:
        enllaç = "No disponible"

 # Mostro la info per pantalla per veure que tot va bé.
 
    print(f"Producte {a +1}: {nom}, PREU: ---- {preu} euros, Valoracions: {valor}\n Compras aquest mes: {compras} \nlink: {enllaç}\n\n  ") #he posat aquests guions nomes per separr el preu de les especificacions i sigui mes comode de llegir
    imatge = foto[a+1]  # (agafo a+1 perquè normalment la primera foto correspon a un anunci de Amazon)
    imatge.screenshot(f"CarpetaScrap/Imatges/producte_{a+1}.png")
    laptops.append({"Producte": nom, "Preu": preu, "Valoracions": valor, "Compras aquest mes": compras, "Link": enllaç, "Imatge":imatge})
    a+= 1

# Creo un CSV amb tota la informació

dataframe= pd.DataFrame(laptops)
dataframe.to_csv("CarpetaScrap/CSV/infoordinadors.csv", index=False)

# Guardo el codi HTML sencer de la pàgina laptops d'Amazon i ho guardo a la subcarpeta HTML.
htmlamazon = driver.page_source
with open("CarpetaScrap/HTML/Htmlamazon.html","w", encoding="utf-8") as f:
    f.write(htmlamazon)

driver.save_screenshot("CarpetaScrap/Imatges/capturaGenerel.png") #Captura de pantalla de la web.
driver.quit()     
