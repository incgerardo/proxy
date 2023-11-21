import requests
import pandas as pd

df=pd.read_csv("lista.csv")

for fila in range(298):

    proxy = {
        'http': f'http://{df.iloc[1,0]}:{df.iloc[1,1]}',
        'https': f'http://{df.iloc[fila,0]}:{df.iloc[fila,1]}'
    }

    print(proxy)

    url = "https://www.thecrag.com/"

    try:
        response = requests.get(url, proxies=proxy, timeout=5)
        if response.status_code == 200:
            print("********************************************************************")
            print(f"El proxy funciona correctamente: {df.iloc[fila,0]}:{df.iloc[fila,1]}")
            print("********************************************************************")
        else:
            print("El proxy no pudo acceder al sitio")
    except requests.RequestException as e:
        print("Error al conectar al proxy:", e)



'''
110.34.3.229:3128
101.255.148.174:8085
91.206.229.251:3128
14.162.146.186:19132
185.169.183.9:8080
5.255.107.249:8080
143.110.190.83:8080
81.70.187.80:8080
117.187.18.136:3128
45.167.124.170:999
5.189.172.158:3128
175.24.214.128:80
200.71.109.105:999
175.24.215.79:80
181.188.247.202:999
38.51.235.213:999
38.51.235.214:999
167.71.41.76:8080




import requests



url = 'https://www.ejemplo.com'

try:
    response = requests.get(url, proxies=proxy, timeout=10)
    if response.status_code == 200:
        print("El proxy funciona correctamente")
    else:
        print("El proxy no pudo acceder al sitio")
except requests.RequestException as e:
    print("Error al conectar al proxy:", e)

'''
