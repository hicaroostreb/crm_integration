import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Acessar as variáveis de ambiente
CRM_URL_TASKS = os.getenv("CRM_URL_TASKS")


def fetch_contacts(limit=10):
    url = CRM_URL_TASKS
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()  # Tenta ler o JSON
            print(f"Exibindo os primeiros {limit} resultados:")
            # Exibe apenas os primeiros "limit" itens
            for i, item in enumerate(data[:limit]):
                print(f"{i + 1}. {item}")  # Exibe cada item
        except ValueError:
            print("Erro: A resposta não é um JSON válido.")
    else:
        print(f"Erro ao acessar a URL. Status code: {response.status_code}")


if __name__ == "__main__":
    fetch_contacts(10)
