import customtkinter as ctk
from controllers.contract_controller import ContractController

class AddContractView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        # Título
        title_label = ctk.CTkLabel(self, text="Adicionar Novo Contrato", font=("Arial", 24))
        title_label.pack(pady=20)

        # Campos para os dados do contrato
        self.client_entry = ctk.CTkEntry(self, placeholder_text="Cliente")
        self.client_entry.pack(pady=5, padx=20, fill="x")

        self.start_date_entry = ctk.CTkEntry(self, placeholder_text="Data de Início (YYYY-MM-DD)")
        self.start_date_entry.pack(pady=5, padx=20, fill="x")

        self.end_date_entry = ctk.CTkEntry(self, placeholder_text="Data de Término (YYYY-MM-DD)")
        self.end_date_entry.pack(pady=5, padx=20, fill="x")

        self.status_entry = ctk.CTkEntry(self, placeholder_text="Status")
        self.status_entry.pack(pady=5, padx=20, fill="x")

        self.value_entry = ctk.CTkEntry(self, placeholder_text="Valor")
        self.value_entry.pack(pady=5, padx=20, fill="x")

        # Botão para salvar o contrato
        save_button = ctk.CTkButton(self, text="Salvar Contrato", command=self.save_contract)
        save_button.pack(pady=10)

        # Botão para voltar para a tela de contratos
        back_button = ctk.CTkButton(self, text="Voltar", command=self.controller.show_contract_view)
        back_button.pack(pady=10)

    def save_contract(self):
        # Coleta os dados do formulário
        contract = {
            "ID": str(len(ContractController().load_contracts()) + 1),
            "Cliente": self.client_entry.get(),
            "Data de Início": self.start_date_entry.get(),
            "Data de Término": self.end_date_entry.get(),
            "Status": self.status_entry.get(),
            "Valor": self.value_entry.get(),
        }

        # Salva o contrato
        contract_controller = ContractController()
        contract_controller.add_contract(contract)

        # Limpa os campos após salvar
        self.client_entry.delete(0, "end")
        self.start_date_entry.delete(0, "end")
        self.end_date_entry.delete(0, "end")
        self.status_entry.delete(0, "end")
        self.value_entry.delete(0, "end")
        
        # Atualiza a visualização de contratos
        self.controller.show_contract_view()
