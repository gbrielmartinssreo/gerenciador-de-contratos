import customtkinter as ctk
from tkinter import ttk

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
        headers = ["ID", "Cliente", "Data de Início", "Data de Término", "Status", "Valor"]
        contracts = self.controller.contract_controller.load_contracts()

        tree = ttk.Treeview(self, columns=headers, show="headings", height=10)
        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, anchor="center", width=100)

        for contract in contracts:
            tree.insert("", "end", values=tuple(contract.values()))

        tree.pack(pady=10)
