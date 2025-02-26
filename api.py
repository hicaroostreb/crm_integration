import requests
from config import CRM_API_URL, CRM_API_KEY


def fetch_data():
    headers = {
        "User-Key": CRM_API_KEY,
        "Content-Type": "application/json",
    }

    # Modifique a URL para buscar contatos diretamente
    url = f"{CRM_API_URL}/Contacts"  # Pode adicionar mais parâmetros, como $top para limitar a quantidade de registros

    response = requests.get(url, headers=headers)

    # Verificando o status e a resposta da API
    print(f"Status da resposta da API: {response.status_code}")
    print(
        "Resposta completa da API:", response.json()
    )  # Verificando a resposta completa

    if response.status_code == 200:
        # A resposta agora deve ter os contatos na chave 'value' ou similar
        contacts = response.json().get(
            "value", []
        )  # Supondo que os contatos estejam na chave "value"
        print(f"Total de contatos recebidos da API: {len(contacts)}")

        # Retorna os contatos para serem processados
        return contacts
    else:
        raise Exception(f"Error fetching data: {response.status_code}")
