**ESPAÑOL- # Scraper de Amazon - Laptops**

Este script realiza un scraping de productos de la categoría laptops en Amazon.com, utilizando Selenium en modo "headless".
Extrae datos de los 10 primeros productos listados en los resultados de búsqueda y te los guarda.

**Información extraída:**
- Nombre del producto
- Precio (si está disponible)
- Valoraciones
- Compras estimadas este mes
- Enlace directo al producto
- Captura de pantalla del producto

**Toda esta información se guarda en un archivo ".csv" y, adicionalmente, se genera:**
- Una captura global de la pàgina
- El HTML de la búsqueda guardado en un archivo ".html"
- Una captura individual para cada producto

**Estructura de carpetas generadas:**
````
CarpetaScrap/
├── CSV/
│   └── infoordinadors.csv
├── HTML/
│   └── Htmlamazon.html
├── Imatges/
│   ├── producte_1.png
│   ├── producte_2.png...
│   └── capturaGeneral.png
`````

**Requisitos:**
- Python 3.7 o superior
- Google Chrome instalado

**Dependencias (instalación):**
pip install selenium pandas webdriver_manager beautifulsoup4

ENGLISH - #Amazon Scraper - Laptops

This script performs scraping of laptop products on Amazon.com using Selenium in headless mode. 
It extracts data from the first 10 products listed in the search results.

**Extracted information:**
- Product name
- Price (if available)
- Ratings
- Estimated purchases this month
- Direct product link
- Screenshot of the product

**All collected data is saved to a .csv file. Additionally:**
- The full HTML page is saved
- A general page screenshot is generated
- Each product has its own image capture

**Folder structure generated:**
````
CarpetaScrap/
├── CSV/
│   └── infoordinadors.csv
├── HTML/
│   └── Htmlamazon.html
├── Imatges/
│   ├── producte_1.png
│   ├── producte_2.png
│   └── capturaGenerel.png
`````
**System Requirements:**
- Python 3.7 or higher
- Google Chrome installed

**Required libraries**
pip install selenium pandas webdriver_manager beautifulsoup4


Thanks for reading, Gracias por leer.

Ismael Lasri
