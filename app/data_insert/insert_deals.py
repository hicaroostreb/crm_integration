import os
import requests
from dotenv import load_dotenv
from app.models.deal import Deal
from app.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError

# Carregar variáveis de ambiente
load_dotenv()

# Acessar as variáveis de ambiente
CRM_URL_DEALS = os.getenv("CRM_URL_DEALS")


# Função para buscar as oportunidades (deals)
def fetch_deals():
    try:
        response = requests.get(CRM_URL_DEALS)
        response.raise_for_status()  # Levanta uma exceção para códigos 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return []  # Retorna uma lista vazia em caso de erro


def insert_or_update_deals(deals_data):
    db = SessionLocal()

    try:
        # Carregar todas as oportunidades existentes no banco de dados em um dicionário
        existing_deals = {deal.Id: deal for deal in db.query(Deal).all()}

        new_deals = []
        updated_deals = []

        # Preparar os dados de oportunidade para inserção ou atualização
        for deal_data in deals_data:
            deal_id = deal_data["Id"]
            existing_deal = existing_deals.get(deal_id)

            if existing_deal:
                # Atualizar campos diretamente se necessário
                fields_to_update = {
                    "value": "Valor",
                    "created_at": "Data de criação",
                    "start_date": "Início",
                    "end_date": "Término",
                    "duration": "Duração",
                    "days_in_stage": "Dias no estágio",
                    "forecasted_closing": "Previsão de fechamento",
                    "client_id": "Id do Cliente",
                    "responsible": "Responsável",
                    "pipeline": "Pipeline",
                    "stage": "Estágio",
                    "opportunity_type": "Tipo de oportunidade",
                    "client_type": "Tipo do Cliente",
                    "client_name": "Cliente",
                    "status": "Situação",
                    "reason_for_loss": "Motivo de perda",
                    "product": "Produto",
                }

                updated = False
                update_data = {}

                for field, key in fields_to_update.items():
                    new_value = deal_data.get(key)
                    if getattr(existing_deal, field) != new_value:
                        update_data[field] = new_value
                        updated = True

                if updated:
                    updated_deals.append({"Id": deal_id, **update_data})

            else:
                new_deal = {
                    "Id": deal_data["Id"],
                    "value": deal_data.get("Valor"),
                    "created_at": deal_data.get("Data de criação"),
                    "start_date": deal_data.get("Início"),
                    "end_date": deal_data.get("Término"),
                    "duration": deal_data.get("Duração"),
                    "days_in_stage": deal_data.get("Dias no estágio"),
                    "forecasted_closing": deal_data.get("Previsão de fechamento"),
                    "client_id": deal_data.get("Id do Cliente"),
                    "responsible": deal_data.get("Responsável"),
                    "pipeline": deal_data.get("Pipeline"),
                    "stage": deal_data.get("Estágio"),
                    "opportunity_type": deal_data.get("Tipo de oportunidade"),
                    "client_type": deal_data.get("Tipo do Cliente"),
                    "client_name": deal_data.get("Cliente"),
                    "status": deal_data.get("Situação"),
                    "reason_for_loss": deal_data.get("Motivo de perda"),
                    "product": deal_data.get("Produto"),
                }
                new_deals.append(new_deal)

        # Inserir novas oportunidades em lotes de 500 usando bulk_insert_mappings para maior eficiência
        if new_deals:
            for i in range(0, len(new_deals), 500):
                db.bulk_insert_mappings(Deal, new_deals[i : i + 500])

        # Atualizar oportunidades em lotes de 500 com bulk_update_mappings
        if updated_deals:
            for i in range(0, len(updated_deals), 500):
                db.bulk_update_mappings(Deal, updated_deals[i : i + 500])

        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Erro ao inserir ou atualizar oportunidades: {e}")
    finally:
        db.close()


# Função principal
def main():
    try:
        deals_data = fetch_deals()  # Busca os dados das oportunidades
        if deals_data:
            insert_or_update_deals(deals_data)  # Insere ou atualiza as oportunidades
            print("Oportunidades inseridas/atualizadas com sucesso!")
        else:
            print("Nenhum dado de oportunidade foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao inserir/atualizar as oportunidades: {e}")


if __name__ == "__main__":
    main()
