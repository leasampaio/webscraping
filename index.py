# Importando bibliotecas
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# Obtendo o HTML
html = urlopen("https://alura-site-scraping.herokuapp.com/hello-world.php")
bs = BeautifulSoup(html, 'html.parser')
dataset = pd.DataFrame(bs)
dataset.to_html('./dataset.html')
dataset