from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_PATH

Base = declarative_base()


def map_type(value):
    """Retorna o tipo de dado do SQLAlchemy correspondente ao tipo Python."""
    if isinstance(value, int):
        return Integer
    elif isinstance(value, float):
        return Float
    elif isinstance(value, str):
        return String
    else:
        return String  # Por padrão, tratamos como String


def create_dynamic_class(table_name, json_data):
    """Cria uma classe dinâmica de tabela baseada no JSON recebido."""
    columns = {
        "id": Column(
            Integer, primary_key=True
        )  # Garante que a coluna 'id' seja a chave primária
    }

    # A primeira entrada do JSON vai ser usada para descobrir as colunas
    first_item = json_data[0] if json_data else {}

    # Para cada chave do primeiro item do JSON, cria uma coluna com o tipo adequado
    for key, value in first_item.items():
        # Ignora a chave 'Id' do JSON, já que temos uma coluna 'id' como chave primária
        if key.lower() == "id":
            continue

        # Cria uma coluna para o campo
        columns[key] = Column(
            map_type(value), nullable=True
        )  # Permite valores nulos (None) nas colunas

    # Define a classe dinamicamente
    dynamic_class = type(table_name, (Base,), {"__tablename__": table_name, **columns})

    # Cria a tabela no banco de dados
    engine = create_engine(f"sqlite:///{DATABASE_PATH}", echo=False)
    Base.metadata.create_all(engine)

    return dynamic_class


def insert_or_update_data(dynamic_class, json_data):
    """Insere ou atualiza os dados na tabela criada dinamicamente."""
    engine = create_engine(f"sqlite:///{DATABASE_PATH}", echo=False)
    session = sessionmaker(bind=engine)()

    try:
        for item in json_data:
            # Adiciona o valor de 'Id' do JSON à chave primária 'id'
            item["id"] = item.get("Id")  # Atribui o valor de 'Id' do JSON à coluna 'id'

            # Remove a chave 'Id' para não causar conflito na inserção
            item.pop("Id", None)

            # Verifica se o registro já existe com o mesmo id
            existing_record = (
                session.query(dynamic_class).filter_by(id=item["id"]).first()
            )

            if existing_record:
                # Atualiza os campos do registro existente
                print(f"Atualizando contato com ID {item['id']}.")
                for key, value in item.items():
                    setattr(
                        existing_record, key, value
                    )  # Atualiza os campos do contato existente
            else:
                # Cria uma instância da tabela com os dados e adiciona à sessão
                record = dynamic_class(**item)
                session.add(record)

        session.commit()
        print("Dados inseridos ou atualizados com sucesso.")
    except Exception as e:
        print(f"Erro ao inserir ou atualizar dados: {e}")
        session.rollback()
    finally:
        session.close()


# Conexão com o banco de dados
engine = create_engine(f"sqlite:///{DATABASE_PATH}", echo=False)
