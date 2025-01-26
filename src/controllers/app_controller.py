from controllers.contract_controller import ContractController
from views.home_view import HomeView
from views.contract_view import ContractView
from views.add_contract_view import AddContractView
from views.filter_by_days_view import FilterByDaysView
from views.cotacao_view import CotacaoView
import requests


class AppController:
    def __init__(self):
        self.root = None
        self.current_view = None
        self.contract_controller = ContractController()
    
    def get_cotacoes(self):
        try:
                requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
                requisicao.raise_for_status()
                requisicao_dic = requisicao.json()
                cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
                cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
                cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])
                return cotacao_dolar, cotacao_euro, cotacao_btc
        except requests.exceptions.RequestException as e:
            return None, None, None

    def set_root(self, root):
        """Define a raiz da interface e inicializa a tela inicial."""
        self.root = root
        self.show_home_view()

    def show_home_view(self):
        """Mostra a tela inicial."""
        if self.current_view:
            self.current_view.destroy()  
        self.current_view = HomeView(self.root, self)

    def show_contract_view(self):
        """Mostra a visualização de contratos."""
        if self.current_view:
            self.current_view.destroy()  
        self.current_view = ContractView(self.root, self)

    def show_add_contract_view(self):
        """Mostra a tela de adicionar contrato."""
        if self.current_view:
            self.current_view.destroy()  
        self.current_view = AddContractView(self.root, self)

    def show_filter_by_days_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = FilterByDaysView(self.root, self)

    def show_cotacao_view(self):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = CotacaoView(self.root, self)
