import requests
from config import CRM_API_URL, CRM_API_KEY


def fetch_data(endpoint):
    headers = {
        "User-Key": CRM_API_KEY,
        "Content-Type": "application/json",
    }

    url = (
        f"{CRM_API_URL}/{endpoint}"  # Usa o endpoint fornecido (Tasks, Contacts, etc.)
    )

    all_data = []  # Lista para armazenar todos os dados
    page_count = 0  # Contador para acompanhar quantas páginas foram buscadas
    total_count = None  # Variável para armazenar o total de registros (se a API fornecer essa informação)

    while url:  # Continuar enquanto houver a URL para a próxima página
        page_count += 1
        print(f"Buscando página {page_count}...")

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()  # Converte a resposta para JSON

            # Verifica se o campo "odata.count" existe na resposta
            if "odata.count" in data:
                total_count = data["odata.count"]  # Se a API fornecer o total, armazena
                print(f"Total de registros (odata.count): {total_count}")

            records = data.get("value", [])  # Dados encontrados na chave "value"
            all_data.extend(records)  # Adiciona os dados à lista

            # Exibe o total de registros na resposta atual
            print(f"Registros recebidos nesta página: {len(records)}")

            # Verifica se há uma próxima página de dados
            next_link = data.get("@odata.nextLink", None)  # Link para a próxima página
            if next_link:
                print(f"Próxima página encontrada: {next_link}")
            else:
                print("Não há mais páginas. Fim da busca.")

            url = next_link  # Atualiza a URL para a próxima página, caso exista
        else:
            print(f"Erro ao acessar a API. Status Code: {response.status_code}")
            break  # Interrompe o loop em caso de erro

    # Exibe informações sobre o total de registros na API, se disponível
    if total_count:
        print(f"Total de registros esperado: {total_count}")

    print(f"Total de dados recebidos: {len(all_data)}")
    return all_data


if __name__ == "__main__":
    print("Iniciando a busca de dados para o endpoint 'Tasks'...")

    tasks_data = fetch_data("Tasks")
    print(f"Total de registros de 'Tasks' recebidos: {len(tasks_data)}")
    print(tasks_data[:1])  # Exibe o primeiro registro para verificação
