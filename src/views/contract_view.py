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
        headers = ["Descrição do Contrato", "Categoria", "Data de Vencimento", "Fornecedor", "Valor do Contrato", "Moeda", "Valor em Reais"]
        contracts = self.controller.contract_controller.load_contracts()
        cotacao_dolar, cotacao_euro, cotacao_btc = self.controller.get_cotacoes()

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
            "Valor do Contrato": 150,
            "Moeda": 80,
            "Valor em Reais": 150
        }

        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, anchor="center", width=column_widths.get(header, 150))

        for contract in contracts:
            valor_contrato = float(contract["Valor do Contrato"])
            moeda = contract["Moeda"]
            
            valor_em_reais = self.converter_para_reais(valor_contrato, moeda, cotacao_dolar, cotacao_euro, cotacao_btc)
            
            tree.insert("", "end", values=(*contract.values(), f"R$ {valor_em_reais:.2f}"))
        tree.pack(pady=10, fill="x")
    
    def converter_para_reais(self, valor_contrato, moeda, cotacao_dolar, cotacao_euro, cotacao_btc):
        if cotacao_dolar is None or cotacao_euro is None or cotacao_btc is None:
            return valor_contrato
        if moeda == "USD":
             return valor_contrato * cotacao_dolar
        elif moeda == "EUR":
            return valor_contrato * cotacao_euro
        elif moeda == "BTC":
            return valor_contrato * cotacao_btc
        else:
            return valor_contrato
