# Detector de Fraude em Transações Bancárias

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.x-orange.svg)
![Pandas](https://img.shields.io/badge/pandas-2.x-yellow.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Descrição

Um projeto de Machine Learning que utiliza Regressão Logística para identificar a probabilidade de uma transação bancária ser fraudulenta. O modelo é treinado com dados sintéticos que simulam características realistas de transações.

---

## 🚀 Funcionalidades

-   **Geração de Dados Sintéticos**: Cria um dataset (`transacoes.csv`) com características realistas para simular um ambiente de transações bancárias.
-   **Treinamento de Modelo**: Treina um modelo de Regressão Logística e salva o modelo treinado (`modelo.pkl`) e o escalador (`scaler.pkl`) para uso posterior.
-   **Previsão via CLI**: Permite fazer previsões em tempo real através de uma interface de linha de comando, informando os dados da transação.

---

## 🛠️ Tecnologias Utilizadas

-   **Python 3.x**
-   **Pandas**: Para manipulação e análise de dados.
-   **Scikit-learn**: Para a criação e treinamento do modelo de Regressão Logística.
-   **Joblib**: Para salvar e carregar o modelo treinado.

---

## 📁 Estrutura do Projeto

```
fraude-bancaria-ml/
│
├── data/
│   └── transacoes.csv      # Dataset simulado
│
├── src/
│   ├── generate_data.py    # Script para gerar dados simulados
│   ├── train_model.py      # Script para treinar o modelo
│   └── predict.py          # Script para realizar previsões via terminal
│
├── modelo.pkl              # Modelo treinado e salvo
├── scaler.pkl              # Escalador de dados salvo
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

---

## ⚙️ Instalação e Uso

### Pré-requisitos

-   Python 3.8 ou superior
-   `pip` (gerenciador de pacotes do Python)

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/fraude-bancaria-ml.git
    cd fraude-bancaria-ml
    ```
    *(Substitua `seu-usuario` pelo seu nome de usuário no GitHub se for um fork)*

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Gere os dados simulados:**
    O script `generate_data.py` criará o arquivo `data/transacoes.csv`.
    ```bash
    python src/generate_data.py
    ```

5.  **Treine o modelo:**
    O script `train_model.py` usará os dados gerados para treinar o modelo e salvar os artefatos `modelo.pkl` e `scaler.pkl`.
    ```bash
    python src/train_model.py
    ```

6.  **Faça uma previsão:**
    Use o script `predict.py` com os parâmetros da transação para obter a probabilidade de fraude.

    **Exemplo:**
    ```bash
    python src/predict.py --valor 3500 --tipo "PIX" --hora "03:00" --local "Miami" --dispositivo "Android"
    ```

    **Saída esperada:**
    ```
    Chance de fraude: 87.23%
    Recomendação: Bloquear transação.
    ```

---

## 📊 Sobre os Dados

Os dados são gerados de forma sintética pelo script `src/generate_data.py`, buscando simular distribuições realistas para:

-   **Valor da Transação**: Valores baixos e altos.
-   **Horário**: Manhã, tarde, noite e madrugada.
-   **Tipo de Transação**: PIX, débito, crédito, boleto, transferência.
-   **Dispositivo**: Android, iPhone, PC, Caixa Eletrônico.
-   **Localização**: Cidades variadas como São Paulo, Rio de Janeiro, Miami, etc.

A variável alvo (`fraude`) é determinada por um conjunto de regras heurísticas para refletir cenários onde a probabilidade de fraude é maior (ex: valores altos de madrugada em locais incomuns).

---

## ✍️ Autor

**Rodrigo Bolgheroni**

---

## 📄 Licença

Este projeto está sob a licença MIT.
