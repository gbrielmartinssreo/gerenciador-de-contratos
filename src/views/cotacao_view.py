import customtkinter as ctk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import os


class CotacaoView(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
         
        title_label = ctk.CTkLabel(self, text="Cotações de Moedas", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)
        
        self.loading_label = ctk.CTkLabel(self, text="Carregando cotações...", font=("Arial", 14))
        self.loading_label.pack(pady=10)
               
        self.dolar_label = ctk.CTkLabel(self, text="", font=("Arial", 14), compound="left")
        self.dolar_label.pack(pady=5)

        self.euro_label = ctk.CTkLabel(self, text="", font=("Arial", 14), compound="left")
        self.euro_label.pack(pady=5)
        
        self.btc_label = ctk.CTkLabel(self, text="", font=("Arial", 14), compound="left")
        self.btc_label.pack(pady=5)
        
        back_button = ctk.CTkButton(self, text="Voltar", command=self.controller.show_home_view)
        back_button.pack(pady=20)
        
        self.load_cotacoes()

    def load_image(self, path, size):
        try:
            image = Image.open(path)
            image = image.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print(f"Erro: Imagem não encontrada em {path}")
            return None

    def load_cotacoes(self):
        try:
                requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
                requisicao.raise_for_status()
                requisicao_dic = requisicao.json()

                cotacao_dolar = float(requisicao_dic['USDBRL']['bid'])
                cotacao_euro = float(requisicao_dic['EURBRL']['bid'])
                cotacao_btc = float(requisicao_dic['BTCBRL']['bid'])

                self.dolar_label.configure(text=f"Dólar: R$ {cotacao_dolar:.2f}")
                self.euro_label.configure(text=f"Euro: R$ {cotacao_euro:.2f}")
                self.btc_label.configure(text=f"BTC: R$ {cotacao_btc:.2f}")
                self.loading_label.destroy()
        except requests.exceptions.RequestException as e:
               self.loading_label.configure(text=f"Erro ao obter cotações: {e}", text_color="red")
               self.dolar_label.configure(text="")
               self.euro_label.configure(text="")
               self.btc_label.configure(text="")
