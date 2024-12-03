import tkinter as tk
import customtkinter as ctk
from controllers.app_controller import AppController

if __name__ == "__main__":
    # Configurações iniciais do customtkinter
    ctk.set_appearance_mode("System")  # Pode ser "Light" ou "Dark"
    ctk.set_default_color_theme("blue")  # Escolha o tema desejado

    # Inicializa a janela principal
    root = ctk.CTk()
    root.title("Gerenciador de Contratos")
    root.geometry("800x600")  # Largura e altura da janela

    # Inicializa o controlador da aplicação
    app_controller = AppController()
    app_controller.set_root(root)

    root.mainloop()
