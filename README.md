# Gerenciador de Contratos 
![Status do Projeto](https://img.shields.io/badge/Status-Finalizado-darkgreen)

## 📖 Descrição
Um aplicativo simples para gerenciar contratos, permitindo visualizar, adicionar e organizar contratos por data de vencimento, incluindo a funcionalidade de conversão de moedas (BRL, USD, EUR e BTC).

Este projeto foi desenvolvido utilizando **Python** com as bibliotecas **CustomTkinter**, **tkcalendar**, **Pillow** e **requests**.

---

## 📋 Índice
1.  [Instalação e execução](#-instalação)
2.  [Funcionalidades](#-funcionalidades)
3.  [Estrutura do Projeto](#-estrutura-do-projeto)

---

## 🛠 Instalação e execução

1.  Clone o repositório:
    ```bash
    git clone https://github.com/gbrielmartinssreo/gerenciador-de-contratos.git
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd gerenciador-de-contratos
    ```
3.  Certifique-se de ter o python instalado:
    ```python
    python --version
    ```
4.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5.  Navegue até o diretório `src`:
    ```bash
    cd src
    ```
6.  Rode o programa:
    ```python
    python main.py
    ```

---

## ⚙️ Funcionalidades

-   **Visualização de contratos**: Exibe uma tabela com os contratos cadastrados, ordenados por data de término em ordem crescente. A tabela inclui a descrição, categoria, data de vencimento, fornecedor, valor do contrato na moeda original, a moeda e o valor convertido para Reais (BRL).
-   **Cadastro de contratos**: Interface amigável para adicionar novos contratos, incluindo a opção de selecionar a moeda do contrato (BRL, USD, EUR ou BTC).
-   **Filtro por dias restantes**: Permite filtrar contratos com vencimento dentro de um número específico de dias, exibindo as informações do contrato e a conversão para reais.
-   **Cotação de Moedas**: Exibe as cotações atuais do Dólar, Euro e Bitcoin em relação ao Real.
-   **Navegação intuitiva**: Transição fácil e intuitiva entre as telas do sistema.
---
## 🗂️ Estrutura do Projeto

```
gerenciador-de-contratos/
├── README.md
├── requirements.txt
└── src/
  ├── controllers/
  │ ├── app_controller.py
  │ └── contract_controller.py
  ├── data/
  │ └── contratos.csv
  ├── main.py
  └── views/
    ├── add_contract_view.py
    ├── contract_view.py
    ├── cotacao_view.py
    ├── filter_by_days_view.py
    └── home_view.py
```
      
-   **`README.md`**: Documentação do projeto.
-   **`requirements.txt`**: Lista das dependências do projeto.
-   **`src/`**:
    -   **`controllers/`**: Lógica da aplicação.
        -   `app_controller.py`: Controla o fluxo principal do aplicativo e lida com as cotações.
        -   `contract_controller.py`: Gerencia as operações com os contratos (carregar, salvar, adicionar).
    -   **`data/`**: Armazena dados.
        -   `contratos.csv`: Arquivo CSV com os dados dos contratos.
    -   **`main.py`**: Ponto de entrada da aplicação.
    -   **`views/`**: Interface gráfica do usuário.
        -   `add_contract_view.py`: Tela para adicionar novos contratos.
        -   `contract_view.py`: Tela para visualizar os contratos.
        -   `cotacao_view.py`: Tela para visualizar as cotações de moedas.
        -  `filter_by_days_view.py`: Tela para filtrar os contratos por dias restantes.
        -   `home_view.py`: Tela inicial do aplicativo.

    

