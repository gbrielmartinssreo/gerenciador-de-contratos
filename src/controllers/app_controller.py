from controllers.contract_controller import ContractController
from views.home_view import HomeView
from views.contract_view import ContractView
from views.add_contract_view import AddContractView

class AppController:
    def __init__(self):
        self.root = None
        self.current_view = None
        self.contract_controller = ContractController()

    def set_root(self, root):
        """Define a raiz da interface e inicializa a tela inicial."""
        self.root = root
        self.show_home_view()

    def show_home_view(self):
        """Mostra a tela inicial."""
        if self.current_view:
            self.current_view.destroy()  # Remove a visualização atual
        self.current_view = HomeView(self.root, self)

    def show_contract_view(self):
        """Mostra a visualização de contratos."""
        if self.current_view:
            self.current_view.destroy()  # Remove a visualização atual
        self.current_view = ContractView(self.root, self)

    def show_add_contract_view(self):
        """Mostra a tela de adicionar contrato."""
        if self.current_view:
            self.current_view.destroy()  # Remove a visualização atual
        self.current_view = AddContractView(self.root, self)
