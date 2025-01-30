from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Obter a URL do banco de dados do arquivo .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Criando a engine do banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criando a SessionLocal para sessões de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criando a base para os modelos
Base = declarative_base()

# Definindo o esquema padrão para as tabelas
Base.metadata.schema = "crm_data"
