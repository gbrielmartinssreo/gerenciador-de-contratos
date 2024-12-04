import customtkinter as ctk

class HomeView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        
        self.place(relx=0.5, rely=0.5, anchor="center")
        self.configure(width=400, height=300)

        self.create_widgets()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text="Gerenciador de Contratos", font=("Arial", 24))
        title_label.pack(pady=20)

        view_contracts_button = ctk.CTkButton(self, text="Visualizar Contratos", command=self.controller.show_contract_view)
        view_contracts_button.pack(pady=10)

        add_contract_button = ctk.CTkButton(self, text="Adicionar Novo Contrato", command=self.controller.show_add_contract_view)
        add_contract_button.pack(pady=10)

        exit_button = ctk.CTkButton(self, text="Sair", command=self.controller.root.quit)
        exit_button.pack(pady=10)
