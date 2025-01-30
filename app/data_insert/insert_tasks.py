import os
import requests
from dotenv import load_dotenv
from app.models.task import Task
from app.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError

# Carregar variáveis de ambiente
load_dotenv()

# Acessar as variáveis de ambiente
CRM_URL_TASKS = os.getenv("CRM_URL_TASKS")


# Função para buscar as tarefas
def fetch_tasks():
    try:
        response = requests.get(CRM_URL_TASKS)
        response.raise_for_status()  # Levanta uma exceção para códigos 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return []  # Retorna uma lista vazia em caso de erro


def insert_or_update_tasks(tasks_data):
    db = SessionLocal()

    try:
        # Carregar todas as tarefas existentes no banco de dados em um dicionário
        existing_tasks = {task.Id: task for task in db.query(Task).all()}

        new_tasks = []
        updated_tasks = []

        # Preparar os dados de tarefa para inserção ou atualização
        for task_data in tasks_data:
            task_id = task_data["Id"]
            existing_task = existing_tasks.get(task_id)

            if existing_task:
                # Atualizar campos diretamente se necessário
                fields_to_update = {
                    "is_completed": "Finalizada",
                    "date": "Data",
                    "created_at": "Data de criação",
                    "card_id": "Id do Card",
                    "client_id": "Id do Cliente",
                    "task_type": "Tipo",
                    "users": "Usuários",
                    "client_name": "Cliente",
                    "tags": "Marcadores",
                    "joiners": "Jointers",
                }

                updated = False
                update_data = {}

                for field, key in fields_to_update.items():
                    new_value = task_data.get(key)
                    if getattr(existing_task, field) != new_value:
                        update_data[field] = new_value
                        updated = True

                if updated:
                    updated_tasks.append({"Id": task_id, **update_data})

            else:
                new_task = {
                    "Id": task_data["Id"],
                    "is_completed": task_data.get("Finalizada"),
                    "date": task_data.get("Data"),
                    "created_at": task_data.get("Data de criação"),
                    "card_id": task_data.get("Id do Card"),
                    "client_id": task_data.get("Id do Cliente"),
                    "task_type": task_data.get("Tipo"),
                    "users": task_data.get("Usuários"),
                    "client_name": task_data.get("Cliente"),
                    "tags": task_data.get("Marcadores"),
                    "joiners": task_data.get("Jointers"),
                }
                new_tasks.append(new_task)

        # Inserir novas tarefas em lotes de 500 usando bulk_insert_mappings para maior eficiência
        if new_tasks:
            for i in range(0, len(new_tasks), 500):
                db.bulk_insert_mappings(Task, new_tasks[i : i + 500])

        # Atualizar tarefas em lotes de 500 com bulk_update_mappings
        if updated_tasks:
            for i in range(0, len(updated_tasks), 500):
                db.bulk_update_mappings(Task, updated_tasks[i : i + 500])

        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Erro ao inserir ou atualizar tarefas: {e}")
    finally:
        db.close()


# Função principal
def main():
    try:
        tasks_data = fetch_tasks()  # Busca os dados das tarefas
        if tasks_data:
            insert_or_update_tasks(tasks_data)  # Insere ou atualiza as tarefas
            print("Tarefas inseridas/atualizadas com sucesso!")
        else:
            print("Nenhum dado de tarefa foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir/atualizar as tarefas: {e}")


if __name__ == "__main__":
    main()
