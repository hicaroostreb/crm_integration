from api import fetch_data
from db import insert_or_update_data, create_dynamic_class
import json


def main():
    # Passo 1: Buscar dados da API (agora já filtrados)
    contacts = fetch_data()  # Agora já retorna os contatos filtrados

    # Passo 2: Inserir no SQLite
    if contacts:  # Verifica se há contatos para inserir
        contacts_json = json.dumps(
            contacts
        )  # Converte a lista de contatos em uma string JSON

        # Passo 3: Criação da tabela dinamicamente e inserção dos dados
        table_name = "contacts"
        dynamic_class = create_dynamic_class(
            table_name, contacts
        )  # Cria a tabela dinâmica
        insert_or_update_data(
            dynamic_class, contacts
        )  # Insere os dados na tabela criada
        print("Dados inseridos com sucesso!")
    else:
        print("Nenhum dado para inserir.")


if __name__ == "__main__":
    main()
