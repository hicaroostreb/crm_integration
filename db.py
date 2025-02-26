# db.py
import sqlite3
from config import DATABASE_PATH


# Função para criar a tabela de contatos
def create_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        type_id INTEGER,
        name TEXT,
        legal_name TEXT,
        register TEXT,
        cnpj TEXT,
        cpf TEXT,
        status_id INTEGER,
        company_id INTEGER,
        relationship_id INTEGER,
        line_of_business_id INTEGER,
        origin_id INTEGER,
        number_of_employees_id INTEGER,
        class_id INTEGER,
        owner_id INTEGER,
        birthday TEXT,
        next_anniversary TEXT,
        previous_anniversary TEXT,
        note TEXT,
        email TEXT,
        website TEXT,
        role_id INTEGER,
        department_id INTEGER,
        skype TEXT,
        facebook TEXT,
        street_address TEXT,
        street_address_number TEXT,
        street_address_line2 TEXT,
        neighborhood TEXT,
        zip_code TEXT,
        foreign_zip_code TEXT,
        foreign_zip_code_country_id INTEGER,
        foreign_zip_code_without_mask TEXT,
        city_id INTEGER,
        state_id INTEGER,
        country_id INTEGER,
        currency_id INTEGER,
        email_marketing TEXT,
        cnae_code TEXT,
        cnae_name TEXT,
        cnae_secondary TEXT,
        latitude REAL,
        longitude REAL,
        import_id TEXT,
        create_importation_id TEXT,
        update_importation_id TEXT,
        first_task_id INTEGER,
        first_task_date TEXT,
        last_interaction_record_id INTEGER,
        last_deal_id INTEGER,
        last_order_id INTEGER,
        tasks_ordination INTEGER,
        lead_id INTEGER,
        editable INTEGER,
        deletable INTEGER,
        creator_id INTEGER,
        updater_id INTEGER,
        create_date TEXT,
        last_update_date TEXT,
        key TEXT,
        last_document_id INTEGER,
        avatar_url TEXT,
        last_company_id INTEGER,
        identity_document TEXT,
        has_scheduled_tasks INTEGER,
        importation_id_create TEXT,
        importation_id_update TEXT,
        public_form_id_create TEXT,
        public_form_id_update TEXT
    )""")
    conn.commit()
    conn.close()


def insert_contacts(contacts):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Inserir ou atualizar os contatos
    for contact in contacts:
        # Imprimir o contato para verificar a estrutura
        print("Contato recebido:", contact)

        cursor.execute(
            """
            INSERT OR REPLACE INTO contacts (
                id, type_id, name, legal_name, register, cnpj, cpf, status_id, company_id,
                relationship_id, line_of_business_id, origin_id, number_of_employees_id,
                class_id, owner_id, birthday, next_anniversary, previous_anniversary,
                note, email, website, role_id, department_id, skype, facebook,
                street_address, street_address_number, street_address_line2, neighborhood,
                zip_code, foreign_zip_code, foreign_zip_code_country_id, foreign_zip_code_without_mask,
                city_id, state_id, country_id, currency_id, email_marketing, cnae_code,
                cnae_name, cnae_secondary, latitude, longitude, import_id, create_importation_id,
                update_importation_id, first_task_id, first_task_date, last_interaction_record_id,
                last_deal_id, last_order_id, tasks_ordination, lead_id, editable, deletable,
                creator_id, updater_id, create_date, last_update_date, key, last_document_id,
                avatar_url, last_company_id, identity_document, has_scheduled_tasks, importation_id_create,
                importation_id_update, public_form_id_create, public_form_id_update
            ) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                contact["Id"],
                contact["TypeId"],
                contact["Name"],
                contact["LegalName"],
                contact["Register"],
                contact["CNPJ"],
                contact["CPF"],
                contact["StatusId"],
                contact["CompanyId"],
                contact["RelationshipId"],
                contact["LineOfBusinessId"],
                contact["OriginId"],
                contact["NumberOfEmployeesId"],
                contact["ClassId"],
                contact["OwnerId"],
                contact["Birthday"],
                contact["NextAnniversary"],
                contact["PreviousAnniversary"],
                contact["Note"],
                contact["Email"],
                contact["Website"],
                contact["RoleId"],
                contact["DepartmentId"],
                contact["Skype"],
                contact["Facebook"],
                contact["StreetAddress"],
                contact["StreetAddressNumber"],
                contact["StreetAddressLine2"],
                contact["Neighborhood"],
                contact["ZipCode"],
                contact["ForeignZipCode"],
                contact["ForeignZipCodeCountryId"],
                contact["ForeignZipCodeWithoutMask"],
                contact["CityId"],
                contact["StateId"],
                contact["CountryId"],
                contact["CurrencyId"],
                contact["EmailMarketing"],
                contact["CNAECode"],
                contact["CNAEName"],
                contact["CNAESecondary"],
                contact["Latitude"],
                contact["Longitude"],
                contact["ImportId"],
                contact["CreateImportationId"],
                contact["UpdateImportationId"],
                contact["FirstTaskId"],
                contact["FirstTaskDate"],
                contact["LastInteractionRecordId"],
                contact["LastDealId"],
                contact["LastOrderId"],
                contact["TasksOrdination"],
                contact["LeadId"],
                contact["Editable"],
                contact["Deletable"],
                contact["CreatorId"],
                contact["UpdaterId"],
                contact["CreateDate"],
                contact["LastUpdateDate"],
                contact["Key"],
                contact["LastDocumentId"],
                contact["AvatarUrl"],
                contact["LastCompanyId"],
                contact["IdentityDocument"],
                contact["HasScheduledTasks"],
                contact["ImportationIdCreate"],
                contact["ImportationIdUpdate"],
                contact["PublicFormIdCreate"],
                contact["PublicFormIdUpdate"],
            ),
        )
    conn.commit()
    conn.close()
