import subprocess
import sys
import os

# Adiciona o diretório 'crm_integration' ao caminho de busca de módulos
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Verifique os caminhos adicionados ao sys.path
print("Caminhos no sys.path:", sys.path)

# Lista de scripts de inserção que precisam rodar
scripts = [
    "insert_contacts.py",
    "insert_deals.py",
    "insert_tasks.py",
    "insert_users.py",
]

# Caminho dos scripts
scripts_path = os.path.join(os.path.dirname(__file__), "data_insert")

# Executando os scripts
for script in scripts:
    script_path = os.path.join(scripts_path, script)
    print(f"Executando {script}...")

    # Executa o script com python, garantindo que ele encontre a pasta 'app'
    result = subprocess.run(
        [sys.executable, "-m", f"app.data_insert.{script.replace('.py', '')}"],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        print(f"{script} executado com sucesso.")
        print(f"Saída: {result.stdout}")  # Exibe a saída padrão
    else:
        print(f"Erro ao executar {script}: {result.stderr}")  # Exibe o erro, se houver
