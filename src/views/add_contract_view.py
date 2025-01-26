import customtkinter as ctk
from tkcalendar import Calendar
import tkinter as tk
from controllers.contract_controller import ContractController
from datetime import datetime
from tkinter import messagebox

class DatePickerDialog(ctk.CTkToplevel):
    def __init__(self, parent, on_select=None, initial_date=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.title("Selecione a Data")
        self.resizable(False, False)
        self.geometry("300x250")
        self.transient(parent)  # Torna esta janela dependente da janela principal

        if initial_date:
            try:
                initial_date = datetime.strptime(initial_date, '%d/%m/%Y').date()
            except ValueError:
                 initial_date = None
        
        self.cal = Calendar(self, firstweekday='sunday', showweeknumbers=False, 
                             selectmode='day', date_pattern="dd/mm/yyyy", 
                             initialdate=initial_date)
        self.cal.pack(pady=10)
        
        self.on_select = on_select

        ok_button = ctk.CTkButton(self, text="OK", command=self.select_date)
        ok_button.pack(pady=10)
        
    def select_date(self):
        if self.on_select:
            selected_date = self.cal.selection_get()
            self.on_select(selected_date)

        self.destroy()
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

        categories = ["Fornecimento", "Locação", "Consultoria", "Software", "Seguro", "Manutenção"]
        self.category_combobox = ctk.CTkComboBox(self, values=categories)
        self.category_combobox.pack(pady=5, padx=20, fill="x")
        self.category_combobox.set("Selecione uma categoria")

        
        date_label = ctk.CTkLabel(self, text="Data de Vencimento")
        date_label.pack(pady=0)

        self.due_date_entry_button = ctk.CTkButton(self, text="Selecionar Data", command=self.show_date_picker)
        self.due_date_entry_button.pack(pady=5, padx=20, fill="x")

        self.selected_date = ctk.StringVar()
        self.date_label = ctk.CTkLabel(self, textvariable=self.selected_date)
        self.date_label.pack(pady=5)

        self.supplier_entry = ctk.CTkEntry(self, placeholder_text="Fornecedor")
        self.supplier_entry.pack(pady=5, padx=20, fill="x")

        self.value_entry = ctk.CTkEntry(self, placeholder_text="Valor do Contrato")
        self.value_entry.pack(pady=5, padx=20, fill="x")
    
        currencies = ["BRL", "USD", "EUR", "BTC"]
        self.currency_combobox = ctk.CTkComboBox(self, values=currencies)
        self.currency_combobox.pack(pady=5, padx=20, fill="x")
        self.currency_combobox.set("BRL")

        save_button = ctk.CTkButton(self, text="Salvar Contrato", command=self.save_contract)
        save_button.pack(pady=10)

        back_button = ctk.CTkButton(self, text="Voltar", command=self.controller.show_home_view)
        back_button.pack(pady=10)

    def show_date_picker(self):
        initial_date = None
        try:
            initial_date = self.selected_date.get()
        except Exception:
             pass
        dialog = DatePickerDialog(self, on_select=self.set_date, initial_date=initial_date)
        dialog.grab_set()

    def set_date(self, date):
        if date:
            self.selected_date.set(date.strftime("%d/%m/%Y"))
    
    def save_contract(self):
        description = self.description_entry.get()
        category = self.category_combobox.get()
        due_date = self.selected_date.get()
        supplier = self.supplier_entry.get()
        value = self.value_entry.get()
        currency = self.currency_combobox.get()

        if not all([description, category, due_date, supplier, value, currency, category != "Selecione uma categoria"]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return
        try:
            float(value)
        except ValueError:
            messagebox.showerror("Erro", "Valor do contrato precisa ser numérico")
            return
        
        contract = {
            "Descrição do Contrato": description,
            "Categoria": category,
            "Data de Vencimento": due_date,
            "Fornecedor": supplier,
            "Valor do Contrato": value,
            "Moeda": currency
        }
        contract_controller = ContractController()
        contract_controller.add_contract(contract)
        self.controller.show_contract_view()
