from app.database import SessionLocal
from app.models.contact import Contact

# Criando uma sessão de banco
db = SessionLocal()

# Consultando todos os contatos
contacts = db.query(Contact).all()

# Exibindo os contatos
for contact in contacts:
    print(contact.name)

# Fechar a sessão
db.close()
