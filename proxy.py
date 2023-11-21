import requests
import pandas as pd

df=pd.read_csv("lista.csv")

proxy=f"{df.iloc[1,0]}:{df.iloc[1,1]}"
print(proxy)

r = requests.get("http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm",proxies=proxy)
print(r.status_code)
----------------------------
import requests

proxy = {
    'http': 'http://IP_DEL_PROXY:PUERTO_DEL_PROXY',
    'https': 'https://IP_DEL_PROXY:PUERTO_DEL_PROXY'
}

url = 'https://www.ejemplo.com'

try:
    response = requests.get(url, proxies=proxy, timeout=10)
    if response.status_code == 200:
        print("El proxy funciona correctamente")
    else:
        print("El proxy no pudo acceder al sitio")
except requests.RequestException as e:
    print("Error al conectar al proxy:", e)

-----------------------------------------------------