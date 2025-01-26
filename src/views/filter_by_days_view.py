import customtkinter as ctk
from datetime import datetime, timedelta
from tkinter import ttk
#from controllers.app_controller import AppController


class FilterByDaysView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.pack(fill="both", expand=True)

        title_label = ctk.CTkLabel(self, text="Filtrar Contratos por Dias Restantes", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        self.days_entry = ctk.CTkEntry(self, placeholder_text="Digite a quantidade de dias")
        self.days_entry.pack(pady=10)

        filter_button = ctk.CTkButton(self, text="Filtrar", command=self.filter_contracts)
        filter_button.pack(pady=10)

        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(pady=10, fill="both", expand=True)

        back_button = ctk.CTkButton(self, text="Voltar", command=self.controller.show_home_view)
        back_button.pack(pady=10)

    def filter_contracts(self):
        """Filtra contratos com base na quantidade de dias restantes."""
        try:
            days = int(self.days_entry.get())
        except ValueError:
            ctk.CTkLabel(self, text="Por favor, insira um número válido.", text_color="red").pack()
            return

        contracts = self.controller.contract_controller.load_contracts()
        filtered_contracts = self.get_contracts_due_in_days(contracts, days)

        self.display_table(filtered_contracts)

    def get_contracts_due_in_days(self, contracts, days):
        filtered = []
        now = datetime.now()
        max_date = now + timedelta(days=days)

        for contract in contracts:
            try:
                end_date = datetime.strptime(contract["Data de Vencimento"], "%d/%m/%Y")
                if now <= end_date <= max_date:
                    filtered.append(contract)
            except ValueError:
                continue  

        return filtered

    def display_table(self, contracts):
        """Exibe os contratos na tabela."""
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        headers = ["Descrição do Contrato", "Categoria", "Data de Vencimento", "Fornecedor", "Valor do Contrato", "Moeda", "Valor em Reais"]
        cotacao_dolar, cotacao_euro, cotacao_btc = self.controller.get_cotacoes()

        tree = ttk.Treeview(self.table_frame, columns=headers, show="headings", height=10)
        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, anchor="center", width=100)
        
        for contract in contracts:
            valor_contrato = float(contract["Valor do Contrato"])
            moeda = contract["Moeda"]
            
            valor_em_reais = self.converter_para_reais(valor_contrato, moeda, cotacao_dolar, cotacao_euro, cotacao_btc)
            
            tree.insert("", "end", values=(*contract.values(), f"R$ {valor_em_reais:.2f}"))

        tree.pack(fill="both", expand=True)
    
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
