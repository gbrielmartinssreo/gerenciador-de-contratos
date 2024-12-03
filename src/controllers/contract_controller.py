import os
import csv  # Corrige o erro: Adicionando a importação do módulo CSV.

class ContractController:
    def __init__(self, file_path="data/contratos.csv"):
        self.file_path = file_path
        self.ensure_data_directory_exists()

    def ensure_data_directory_exists(self):
        """Garante que o diretório para o arquivo CSV exista."""
        dir_path = os.path.dirname(self.file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def load_contracts(self):
        """Carrega contratos do arquivo CSV."""
        contracts = []
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.DictReader(file)
                contracts = [row for row in reader]
        except FileNotFoundError:
            pass  # Arquivo ainda não existe
        return contracts

    def save_contracts(self, contracts):
        """Salva a lista de contratos no arquivo CSV."""
        with open(self.file_path, mode='w', newline='') as file:
            fieldnames = ["ID", "Cliente", "Data de Início", "Data de Término", "Status", "Valor"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contracts)

    def add_contract(self, contract):
        """Adiciona um novo contrato ao CSV."""
        contracts = self.load_contracts()
        contracts.append(contract)
        self.save_contracts(contracts)
