import requests

#https://es.proxyscrape.com/

with open("http_proxies.txt","r") as arch1:
	proxs=arch1.readlines()

print(f"La cantidad de proxis disponibles es {len(proxs)}")

for prox in proxs:

    proxy = {
        'http': f'http://{prox}',
        'https': f'http://{prox}'
    }

    print(proxy)

    url = "https://www.thecrag.com/"

    try:
        response = requests.get(url, proxies=proxy, timeout=5)
        if response.status_code == 200:
            print("********************************************************************")
            print(f"El proxy funciona correctamente: {prox}")
            print("********************************************************************")
            
            with open('respuesta.txt', 'w', encoding='utf-8') as file:
                file.write(response.text)
        else:
            print("El proxy no pudo acceder al sitio")
    except requests.RequestException as e:
        print("Error al conectar al proxy:", e)