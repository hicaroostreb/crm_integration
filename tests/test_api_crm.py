from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

CRM_SERVER = os.getenv("CRM_SERVER")
CRM_USER_KEY = os.getenv("CRM_USER_KEY")

app = FastAPI()


# Função para obter campos de uma entidade
def fetch_fields(entity_id):
    headers = {
        "User-Key": CRM_USER_KEY,  # Chave de usuário para autenticação
    }

    # Montar a URL para buscar os campos da entidade
    url = f"{CRM_SERVER}/Fields?$filter=EntityId+eq+{entity_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta um erro para status de falha (4xx, 5xx)

        # Verifica se a resposta tem a chave 'value'
        if "value" in response.json():
            return response.json()  # Retorna os dados dos campos
        else:
            print(f"Erro: Dados não encontrados na resposta. {response.json()}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None


# Endpoint para retornar os campos de uma entidade específica
@app.get("/fetch-fields/{entity_id}")
async def get_fields(entity_id: int):
    fields = fetch_fields(entity_id)
    if fields:
        return {"status": "success", "fields": fields}
    else:
        return {"status": "error", "message": "Não foi possível obter os campos."}
