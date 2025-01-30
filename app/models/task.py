from sqlalchemy import Column, BigInteger, String, Date, Boolean
from ..database import Base


class Task(Base):
    __tablename__ = "crm_tasks"
    __table_args__ = {"schema": "crm_data"}

    Id = Column("Id", BigInteger, primary_key=True, index=True)
    is_completed = Column("Finalizada", Boolean, nullable=True)
    date = Column("Data", Date, nullable=True)
    created_at = Column("Data de criação", Date, nullable=True)
    card_id = Column("Id do Card", BigInteger, nullable=True)
    client_id = Column("Id do Cliente", BigInteger, nullable=True)
    task_type = Column("Tipo", String, nullable=True)
    users = Column("Usuários", String, nullable=True)
    client_name = Column("Cliente", String, nullable=True)
    tags = Column("Marcadores", String, nullable=True)
    joiners = Column("Jointers", String, nullable=True)
