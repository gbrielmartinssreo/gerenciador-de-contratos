import customtkinter as ctk
from tkinter import ttk
from controllers.contract_controller import ContractController

class ContractView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        # Cabeçalhos da tabela
        headers = ["ID", "Cliente", "Data de Início", "Data de Término", "Status", "Valor"]

        # Carrega os contratos
        contract_controller = ContractController()
        contracts = contract_controller.load_contracts()

        # Criação do Treeview
        tree = ttk.Treeview(self, columns=headers, show="headings")
        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, anchor="center", width=150)

        # Adiciona os contratos à tabela
        for contract in contracts:
            tree.insert("", "end", values=[contract.get(header, "") for header in headers])

        # Exibe o Treeview na interface
        tree.pack(pady=20, fill="both", expand=True)
