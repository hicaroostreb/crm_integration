import requests
from config import CRM_API_URL, CRM_API_KEY  # Importa as variáveis de config.py


def test_api():
    url = f"{CRM_API_URL}/Contacts?$top=1"  # Limita o retorno a apenas 1 contato

    headers = {
        "User-Key": CRM_API_KEY,  # Usa "User-Key" em vez de "Authorization"
        "Content-Type": "application/json",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()  # Converte a resposta para JSON
        if "value" in data and data["value"]:
            print(
                "Exemplo de contato recebido:", data["value"][0]
            )  # Exibe o primeiro contato
        else:
            print("Nenhum contato encontrado.")
    else:
        print(f"Erro ao acessar a API. Status Code: {response.status_code}")


if __name__ == "__main__":
    test_api()
