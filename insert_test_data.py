import os
import requests
import time
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
        start_time = time.time()  # Medir o tempo de resposta da API
        response = requests.get(CRM_URL_TASKS)
        response.raise_for_status()  # Levanta uma exceção para códigos 4xx/5xx
        print(f"Tempo de resposta da API: {time.time() - start_time} segundos")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return []  # Retorna uma lista vazia em caso de erro


def insert_tasks(tasks_data):
    db = SessionLocal()

    try:
        # Inserir todas as tarefas de uma vez em lotes de 100 (ou menos)
        tasks = [
            Task(
                Id=task_data["Id"],
                is_completed=task_data.get("Finalizada"),
                date=task_data.get("Data"),
                created_at=task_data.get("Data de criação"),
                card_id=task_data.get("Id do Card"),
                client_id=task_data.get("Id do Cliente"),
                task_type=task_data.get("Tipo"),
                users=task_data.get("Usuários"),
                client_name=task_data.get("Cliente"),
                tags=task_data.get("Marcadores"),
                joiners=task_data.get("Jointers"),
            )
            for task_data in tasks_data
        ]

        # Inserir em lotes de 100
        for i in range(0, len(tasks), 100):
            print(f"Inserindo tarefas de {i} a {i + 100}")
            start_time = time.time()
            db.bulk_save_objects(tasks[i : i + 100], return_defaults=False)
            db.commit()
            print(
                f"Tempo para inserir lote {i} a {i + 100}: {time.time() - start_time} segundos"
            )

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Erro ao inserir tarefas: {e}")
    finally:
        db.close()


# Função principal
def main():
    try:
        tasks_data = fetch_tasks()  # Busca os dados das tarefas
        if tasks_data:
            insert_tasks(tasks_data)  # Insere as tarefas
            print("Tarefas inseridas com sucesso!")
        else:
            print("Nenhum dado de tarefa foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir as tarefas: {e}")


if __name__ == "__main__":
    main()
