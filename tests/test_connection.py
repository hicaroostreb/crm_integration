import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Pegar a URL do banco de dados do .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ Erro: DATABASE_URL não encontrada no .env")

# Testar a conexão
try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("✅ Conexão bem-sucedida!")
    connection.close()
except Exception as e:
    print("❌ Erro ao conectar:", e)
