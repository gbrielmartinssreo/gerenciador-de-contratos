import customtkinter as ctk
from controllers.contract_controller import ContractController

class AddContractView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller

        self.place(relx=0.5, rely=0.5, anchor="center")
        self.configure(width=600, height=400)

        self.create_widgets()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text="Adicionar Novo Contrato", font=("Arial", 24))
        title_label.pack(pady=20)

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

        save_button = ctk.CTkButton(self, text="Salvar Contrato", command=self.save_contract)
        save_button.pack(pady=10)

        back_button = ctk.CTkButton(self, text="Voltar", command=self.controller.show_home_view)
        back_button.pack(pady=10)

    def save_contract(self):
        contract = {
            "ID": str(len(ContractController().load_contracts()) + 1),
            "Cliente": self.client_entry.get(),
            "Data de Início": self.start_date_entry.get(),
            "Data de Término": self.end_date_entry.get(),
            "Status": self.status_entry.get(),
            "Valor": self.value_entry.get(),
        }

        contract_controller = ContractController()
        contract_controller.add_contract(contract)

        self.client_entry.delete(0, "end")
        self.start_date_entry.delete(0, "end")
        self.end_date_entry.delete(0, "end")
        self.status_entry.delete(0, "end")
        self.value_entry.delete(0, "end")
        
        self.controller.show_contract_view()
