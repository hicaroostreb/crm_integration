from sqlalchemy import Column, BigInteger, String, Date
from app.database import Base


class Contact(Base):
    __tablename__ = "crm_contacts"
    __table_args__ = {"schema": "crm_data"}

    Id = Column("Id", BigInteger, primary_key=True, index=True)
    name = Column("Nome", String, nullable=True)
    birthday = Column("Data de nascimento", Date, nullable=True)
    responsible = Column("Responsável", String, nullable=True)
    account_manager = Column("Gerente de Conta", String, nullable=True)
    opportunity = Column("Oportunidade", String, nullable=True)
    account_safra = Column("Conta Safra", String, nullable=True)
    city = Column("Cidade", String, nullable=True)
    state = Column("Estado", String, nullable=True)
    gender = Column("Gênero", String, nullable=True)
    marital_status = Column("Estado civil", String, nullable=True)
    has_children = Column("Tem filhos?", String, nullable=True)
    profession = Column("Profissão / Cargo", String, nullable=True)
    profile = Column("Perfil", String, nullable=True)
    contact_type = Column("Tipo", String, nullable=True)
    journey_stage = Column("Estágio da Jornada", String, nullable=True)
    lead_status = Column("Status do Lead", String, nullable=True)
