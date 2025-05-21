import requests

# Funzione che fa una chiamata GET all'endpoint /hello
def get_hello_message():
    url = 'https://api.example.com/hello'
    response = requests.get(url)
    
    # Se la risposta è valida, ritorniamo il contenuto in formato JSON
    if response.status_code == 200:
        return response.json()
    else:
        return None
