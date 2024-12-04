import tkinter as tk
import customtkinter as ctk
from controllers.app_controller import AppController

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  
    ctk.set_default_color_theme("blue")  

    root = ctk.CTk()
    root.title("Gerenciador de Contratos")
    root.geometry("800x600")  

    app_controller = AppController()
    app_controller.set_root(root)

    root.mainloop()
