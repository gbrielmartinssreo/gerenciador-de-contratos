import customtkinter as ctk
from controllers.contract_controller import ContractController

class AddContractView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)  
        self.controller = controller 
        self.pack(fill="both", expand=True) 
        self.create_widgets() 

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text="Adicionar Novo Contrato", font=("Arial", 24))
        title_label.pack(pady=20)

        self.description_entry = ctk.CTkEntry(self, placeholder_text="Descrição do Contrato")
        self.description_entry.pack(pady=5, padx=20, fill="x")

        self.category_entry = ctk.CTkEntry(self, placeholder_text="Categoria")
        self.category_entry.pack(pady=5, padx=20, fill="x")

        self.due_date_entry = ctk.CTkEntry(self, placeholder_text="Data de Vencimento (YYYY-MM-DD)")
        self.due_date_entry.pack(pady=5, padx=20, fill="x")

        self.supplier_entry = ctk.CTkEntry(self, placeholder_text="Fornecedor")
        self.supplier_entry.pack(pady=5, padx=20, fill="x")

        save_button = ctk.CTkButton(self, text="Salvar Contrato", command=self.save_contract)
        save_button.pack(pady=10)

        back_button = ctk.CTkButton(self, text="Voltar", command=self.controller.show_home_view)
        back_button.pack(pady=10)

    def save_contract(self):
        contract = {
            "Descrição do Contrato": self.description_entry.get(),
            "Categoria": self.category_entry.get(),
            "Data de Vencimento": self.due_date_entry.get(),
            "Fornecedor": self.supplier_entry.get(),
        }

        contract_controller = ContractController()
        contract_controller.add_contract(contract)

        self.controller.show_contract_view()
