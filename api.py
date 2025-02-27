import requests
from config import CRM_API_URL, CRM_API_KEY


def fetch_data():
    headers = {
        "User-Key": CRM_API_KEY,
        "Content-Type": "application/json",
    }

    # Modifique a URL para buscar contatos diretamente
    url = f"{CRM_API_URL}/Contacts"  # URL inicial para buscar contatos

    all_contacts = []  # Lista para armazenar todos os contatos

    while url:  # Continuar enquanto houver a URL para a próxima página
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()  # Converte a resposta para JSON

            # A resposta deve ter os contatos na chave 'value' ou similar
            contacts = data.get("value", [])  # Contatos encontrados na chave "value"
            all_contacts.extend(contacts)  # Adiciona os contatos à lista

            # Verifica se há uma próxima página de dados
            url = data.get(
                "@odata.nextLink", None
            )  # Obtém o link para a próxima página
        else:
            print(f"Erro ao acessar a API. Status Code: {response.status_code}")
            break  # Interrompe o loop em caso de erro

    print(f"Total de contatos recebidos: {len(all_contacts)}")
    return all_contacts  # Retorna todos os contatos recebidos


# Exemplo de uso
if __name__ == "__main__":
    all_contacts = fetch_data()
    print(f"Total final de contatos: {len(all_contacts)}")
