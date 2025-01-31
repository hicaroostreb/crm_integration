import os
import sys
import requests
from dotenv import load_dotenv
from app.models.contact import Contact
from app.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError

# Adiciona o diretório crm_integration ao caminho de busca de módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Carregar variáveis de ambiente
load_dotenv()

# Acessar as variáveis de ambiente
CRM_URL_CONTACTS = os.getenv("CRM_URL_CONTACTS")


# Função para buscar os contatos
def fetch_contacts():
    try:
        response = requests.get(CRM_URL_CONTACTS)
        response.raise_for_status()  # Levanta uma exceção para códigos 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return []  # Retorna uma lista vazia em caso de erro


def insert_or_update_contacts(contacts_data):
    db = SessionLocal()

    try:
        # Carregar todos os contatos existentes no banco de dados em um dicionário
        existing_contacts = {contact.Id: contact for contact in db.query(Contact).all()}

        new_contacts = []
        updated_contacts = []

        for contact_data in contacts_data:
            contact_id = contact_data["Id"]
            existing_contact = existing_contacts.get(contact_id)

            if existing_contact:
                updated = False
                fields_to_update = {
                    "name": "Nome",
                    "birthday": "Data de nascimento",
                    "responsible": "Responsável",
                    "account_manager": "Gerente de Conta",
                    "opportunity": "Oportunidade",
                    "account_safra": "Conta Safra",
                    "city": "Cidade",
                    "state": "Estado",
                    "gender": "Gênero",
                    "marital_status": "Estado civil",
                    "has_children": "Tem filhos?",
                    "profession": "Profissão / Cargo",
                    "profile": "Perfil",
                    "contact_type": "Tipo",
                    "journey_stage": "Estágio da Jornada",
                    "lead_status": "Status do Lead",
                }

                for field, key in fields_to_update.items():
                    new_value = contact_data.get(key)
                    if getattr(existing_contact, field) != new_value:
                        setattr(existing_contact, field, new_value)
                        updated = True

                if updated:
                    updated_contacts.append(existing_contact)

            else:
                new_contact = Contact(
                    Id=contact_data["Id"],
                    name=contact_data["Nome"],
                    birthday=contact_data.get("Data de nascimento"),
                    responsible=contact_data.get("Responsável"),
                    account_manager=contact_data.get("Gerente de Conta"),
                    opportunity=contact_data.get("Oportunidade"),
                    account_safra=contact_data.get("Conta Safra"),
                    city=contact_data.get("Cidade"),
                    state=contact_data.get("Estado"),
                    gender=contact_data.get("Gênero"),
                    marital_status=contact_data.get("Estado civil"),
                    has_children=contact_data.get("Tem filhos?"),
                    profession=contact_data.get("Profissão / Cargo"),
                    profile=contact_data.get("Perfil"),
                    contact_type=contact_data.get("Tipo"),
                    journey_stage=contact_data.get("Estágio da Jornada"),
                    lead_status=contact_data.get("Status do Lead"),
                )
                new_contacts.append(new_contact)

        # Inserir novos contatos em lotes de 500
        if new_contacts:
            for i in range(0, len(new_contacts), 500):
                db.bulk_save_objects(new_contacts[i : i + 500], return_defaults=False)

        # Atualizar contatos em lotes de 500
        if updated_contacts:
            for i in range(0, len(updated_contacts), 500):
                db.bulk_save_objects(
                    updated_contacts[i : i + 500], return_defaults=False
                )

        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Erro ao inserir ou atualizar contatos: {e}")
    finally:
        db.close()


# Função principal
def main():
    try:
        contacts_data = fetch_contacts()  # Busca os dados dos contatos
        if contacts_data:
            insert_or_update_contacts(contacts_data)  # Insere ou atualiza os contatos
            print("Contatos inseridos/atualizados com sucesso!")
        else:
            print("Nenhum dado de contato foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir/atualizar os contatos: {e}")


if __name__ == "__main__":
    main()
