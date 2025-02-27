# main.py
from api import fetch_data
from db import process_data


def main():
    endpoints = [
        "Contacts",
        "Tasks",
        "Users",
        "Deals",
    ]  # Lista de endpoints a serem processados

    for endpoint in endpoints:
        print(f"Iniciando a busca de dados para o endpoint '{endpoint}'...")

        # Busca os dados de cada endpoint
        data = fetch_data(endpoint)

        # Processa os dados recebidos
        process_data(endpoint, data)

    print("Processamento concluído para todos os endpoints.")


if __name__ == "__main__":
    main()
