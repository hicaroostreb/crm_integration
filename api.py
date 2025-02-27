# api.py
import requests
from config import CRM_API_URL, CRM_API_KEY


def fetch_data(endpoint):
    """Busca dados da API para o endpoint fornecido."""
    headers = {
        "User-Key": CRM_API_KEY,
        "Content-Type": "application/json",
    }

    url = f"{CRM_API_URL}/{endpoint}"  # Usando o endpoint passado para a URL
    all_data = []  # Lista para armazenar todos os dados

    while url:  # Continuar enquanto houver a URL para a próxima página
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()  # Converte a resposta para JSON

            # A resposta deve ter os dados na chave 'value' ou similar
            data_items = data.get("value", [])  # Busca os itens de dados
            all_data.extend(data_items)  # Adiciona os dados à lista

            # Verifica se há uma próxima página de dados
            url = data.get(
                "@odata.nextLink", None
            )  # Obtém o link para a próxima página
        else:
            print(f"Erro ao acessar a API. Status Code: {response.status_code}")
            break  # Interrompe o loop em caso de erro

    print(f"Total de dados recebidos do endpoint '{endpoint}': {len(all_data)}")
    return all_data  # Retorna todos os dados recebidos
