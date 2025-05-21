import requests_mock
from openAPI import get_hello_message  # Importiamo la funzione dal file api_client.py

# Funzione di test per l'endpoint /hello
def test_hello_api():
    with requests_mock.Mocker() as m:
        # Mockiamo la risposta 200 per l'endpoint /hello
        m.get('https://api.example.com/hello', json={'message': 'Ciao, come va?'})

        # Chiamiamo la funzione che fa la richiesta all'API
        response = get_hello_message()

        # Verifica che la risposta sia corretta
        assert response == {'message': 'Ciao, come va?'}
        print("Test superato! Risposta mock ricevuta:", response)

# Funzione di test per simulare errore 404
def test_hello_api_error():
    with requests_mock.Mocker() as m:
        m.get('https://api.example.com/hello', status_code=404)

        response = get_hello_message()

        assert response is None
        print("Test errore superato! Risposta con codice 404")

# Esegui i test
test_hello_api()
test_hello_api_error()
