import os
import requests
from dotenv import load_dotenv
from app.models.user import User  # Modelo de usuários
from app.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError

# Carregar variáveis de ambiente
load_dotenv()

# Acessar as variáveis de ambiente
CRM_URL_USERS = os.getenv("CRM_URL_USERS")  # URL dos usuários


# Função para buscar os usuários
def fetch_users():
    try:
        response = requests.get(CRM_URL_USERS)
        response.raise_for_status()  # Levanta uma exceção para códigos 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return []  # Retorna uma lista vazia em caso de erro


def insert_or_update_users(users_data):
    db = SessionLocal()

    try:
        # Carregar todos os usuários existentes no banco de dados em um dicionário
        existing_users = {user.Id: user for user in db.query(User).all()}

        new_users = []
        updated_users = []

        for user_data in users_data:
            user_id = user_data["Id"]
            existing_user = existing_users.get(user_id)

            if existing_user:
                updated = False
                fields_to_update = {
                    "name": "Nome",
                    "position": "Cargo",
                    "teams": "Equipes",
                    "profile": "Perfil",
                }

                for field, key in fields_to_update.items():
                    new_value = user_data.get(key)
                    if getattr(existing_user, field) != new_value:
                        setattr(existing_user, field, new_value)
                        updated = True

                if updated:
                    updated_users.append(existing_user)

            else:
                new_user = User(
                    Id=user_data["Id"],
                    name=user_data["Nome"],
                    position=user_data.get("Cargo"),
                    teams=user_data.get("Equipes"),
                    profile=user_data.get("Perfil"),
                )
                new_users.append(new_user)

        # Inserir novos usuários em lotes de 500
        if new_users:
            for i in range(0, len(new_users), 500):
                db.bulk_save_objects(new_users[i : i + 500], return_defaults=False)

        # Atualizar usuários em lotes de 500
        if updated_users:
            for i in range(0, len(updated_users), 500):
                db.bulk_save_objects(updated_users[i : i + 500], return_defaults=False)

        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Erro ao inserir ou atualizar usuários: {e}")
    finally:
        db.close()


# Função principal
def main():
    try:
        users_data = fetch_users()  # Busca os dados dos usuários
        if users_data:
            insert_or_update_users(users_data)  # Insere ou atualiza os usuários
            print("Usuários inseridos/atualizados com sucesso!")
        else:
            print("Nenhum dado de usuário foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir/atualizar os usuários: {e}")


if __name__ == "__main__":
    main()
