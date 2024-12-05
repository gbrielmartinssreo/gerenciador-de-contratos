import customtkinter as ctk
from tkinter import ttk
from datetime import datetime

class ContractView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.pack(fill="both", expand=True)

        title_label = ctk.CTkLabel(self, text="Visualização de Contratos", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        self.create_table()

        back_button = ctk.CTkButton(self, text="Voltar", command=self.controller.show_home_view)
        back_button.pack(pady=10)

    def create_table(self):
        headers = ["Descrição do Contrato", "Categoria", "Data de Vencimento", "Fornecedor"]
        contracts = self.controller.contract_controller.load_contracts()

        contracts = sorted(
            contracts, 
            key=lambda x: datetime.strptime(x["Data de Vencimento"], "%d/%m/%Y")
        )

        tree = ttk.Treeview(self, columns=headers, show="headings", height=10)

        column_widths = {
            "Descrição do Contrato": 300,
            "Categoria": 150,
            "Data de Vencimento": 150,
            "Fornecedor": 200,
        }

        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, anchor="center", width=column_widths.get(header, 150))

        for contract in contracts:
            tree.insert("", "end", values=tuple(contract.values()))

        tree.pack(pady=10, fill="x")  
