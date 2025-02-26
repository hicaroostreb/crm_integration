from api import fetch_data
from db import insert_contacts, create_table


def main():
    # Passo 1: Criar a tabela (caso não exista)
    create_table()

    # Passo 2: Buscar dados da API (agora já filtrados)
    contacts = fetch_data()  # Agora já retorna os contatos filtrados

    # Passo 3: Inserir no SQLite
    if contacts:  # Verifica se há contatos para inserir
        insert_contacts(contacts)
        print("Dados inseridos com sucesso!")
    else:
        print("Nenhum dado para inserir.")


if __name__ == "__main__":
    main()
