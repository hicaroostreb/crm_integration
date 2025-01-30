# crm_integration

CRM Integration

Este projeto tem como objetivo integrar dados de diversas fontes para um banco de dados central, utilizando o FastAPI e consumindo APIs externas.

Estrutura do Projeto
O projeto está organizado da seguinte maneira:

bash
Copiar
Editar
crm_integration/
│
├── app/                   # Código principal da aplicação FastAPI
│   ├── main.py            # Arquivo principal para a FastAPI
│   ├── models/            # Definições de modelos de dados
│   ├── schemas/           # Schemas para comunicação de dados
│   └── services/          # Funções auxiliares para integração com API
│
├── data/                  # Arquivos de configuração e de dados estáticos
│   └── config.json        # Configurações gerais do sistema
│
├── .gitignore             # Arquivos para ignorar no versionamento
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
app/
main.py: Este é o arquivo principal da aplicação FastAPI. Aqui você configura as rotas e inicia o servidor.
models/: Contém os modelos de dados usados para representar as entidades do CRM (como contacts, tasks, deals, etc.).
schemas/: Contém os schemas que definem como os dados devem ser estruturados quando enviados e recebidos pela API.
services/: Contém funções auxiliares para integração com APIs externas e manipulação de dados.
data/
config.json: Arquivo de configuração para armazenar informações de conexão com as APIs e outras configurações necessárias.
Requisitos
Antes de rodar o projeto, você precisa instalar as dependências. Para isso, execute o seguinte comando dentro do diretório do projeto:

bash
Copiar
Editar
pip install -r requirements.txt
Rodando a Aplicação
Para rodar a aplicação, use o comando:

bash
Copiar
Editar
uvicorn app.main:app --reload
Isso vai iniciar o servidor FastAPI no seu localhost (por padrão, na porta 8000). Você pode acessar a documentação interativa da API em:

http://localhost:8000/docs

Estrutura de API
GET /api/contacts/: Recupera todos os contatos.
POST /api/contacts/: Adiciona um novo contato.
Note: As APIs externas (como o Ploomes) são consumidas por meio de integrações definidas nos arquivos de serviço.

Desenvolvimento
Configurações
As configurações do projeto podem ser alteradas no arquivo data/config.json. Aqui, você pode configurar URLs de APIs, autenticações e outras configurações do sistema.

Contribuição
Se deseja contribuir para o projeto, siga as etapas:

Faça um fork do repositório.
Crie uma branch para sua feature: git checkout -b feature/feature-name.
Commit suas mudanças: git commit -am 'Add new feature'.
Push para sua branch: git push origin feature/feature-name.
Abra um Pull Request.