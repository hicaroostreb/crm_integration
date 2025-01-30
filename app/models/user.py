from sqlalchemy import Column, BigInteger, String
from ..database import Base


class User(Base):
    __tablename__ = "crm_users"
    __table_args__ = {"schema": "crm_data"}

    Id = Column("Id", BigInteger, primary_key=True, index=True)
    name = Column("Nome", String, nullable=True)
    position = Column("Cargo", String, nullable=True)
    teams = Column("Equipes", String, nullable=True)
    profile = Column("Perfil", String, nullable=True)
