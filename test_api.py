import requests
from config import CRM_API_URL, CRM_API_KEY  # Importa as variáveis de config.py


def test_api():
    url = f"{CRM_API_URL}/Contacts"  # A requisição inicial sem limitar o número de contatos

    headers = {
        "User-Key": CRM_API_KEY,  # Usa "User-Key" em vez de "Authorization"
        "Content-Type": "application/json",
    }

    all_contacts = []  # Lista para armazenar todos os contatos recebidos

    while url:  # Enquanto houver uma URL para a próxima página
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()  # Converte a resposta para JSON
            if "value" in data and data["value"]:
                all_contacts.extend(
                    data["value"]
                )  # Adiciona os contatos da página atual à lista de todos os contatos
                print(
                    f"Recebidos {len(data['value'])} contatos. Total de contatos até agora: {len(all_contacts)}"
                )
            else:
                print("Nenhum contato encontrado.")

            # Verifica se existe a chave '@odata.nextLink' para paginação
            url = data.get(
                "@odata.nextLink", None
            )  # Atualiza a URL para a próxima página de contatos (se houver)

        else:
            print(f"Erro ao acessar a API. Status Code: {response.status_code}")
            break

    # Ao final, mostra o total de contatos recebidos
    print(f"Total de contatos recebidos: {len(all_contacts)}")
    if all_contacts:
        print(
            f"Exemplo de contato recebido: {all_contacts[0]}"
        )  # Exibe o primeiro contato


if __name__ == "__main__":
    test_api()
