import customtkinter as ctk
from datetime import datetime, timedelta
from tkinter import ttk

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
        """Retorna contratos que vencem nos próximos 'days' dias."""
        filtered = []
        now = datetime.now()
        max_date = now + timedelta(days=days)

        for contract in contracts:
            end_date = datetime.strptime(contract["Data de Término"], "%Y-%m-%d")
            if now <= end_date <= max_date:
                filtered.append(contract)

        return filtered

    def display_table(self, contracts):
        """Exibe os contratos na tabela."""
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        headers = ["ID", "Cliente", "Data de Início", "Data de Término", "Status", "Valor"]

        tree = ttk.Treeview(self.table_frame, columns=headers, show="headings", height=10)
        for header in headers:
            tree.heading(header, text=header)
            tree.column(header, anchor="center", width=100)

        for contract in contracts:
            tree.insert("", "end", values=tuple(contract.values()))

        tree.pack(fill="both", expand=True)
