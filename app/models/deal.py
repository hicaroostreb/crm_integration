from sqlalchemy import Column, BigInteger, String, Date, Numeric, Double
from ..database import Base


class Deal(Base):
    __tablename__ = "crm_deals"
    __table_args__ = {"schema": "crm_data"}

    Id = Column("Id", BigInteger, primary_key=True, index=True)
    value = Column("Valor", Numeric, nullable=True)
    created_at = Column("Data de criação", Date, nullable=True)
    start_date = Column("Início", Date, nullable=True)
    end_date = Column("Término", Date, nullable=True)
    duration = Column("Duração", Double, nullable=True)
    days_in_stage = Column("Dias no estágio", Double, nullable=True)
    forecasted_closing = Column("Previsão de fechamento", Date, nullable=True)
    client_id = Column("Id do Cliente", BigInteger, nullable=True)
    responsible = Column("Responsável", String, nullable=True)
    pipeline = Column("Pipeline", String, nullable=True)
    stage = Column("Estágio", String, nullable=True)
    opportunity_type = Column("Tipo de oportunidade", String, nullable=True)
    client_type = Column("Tipo do Cliente", String, nullable=True)
    client_name = Column("Cliente", String, nullable=True)
    status = Column("Situação", String, nullable=True)
    reason_for_loss = Column("Motivo de perda", String, nullable=True)
    product = Column("Produto", String, nullable=True)
