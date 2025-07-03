import argparse
import pandas as pd
import joblib

# Carregando modelo, scaler e colunas salvos no treino
modelo = joblib.load("../modelo.pkl")
scaler = joblib.load("../scaler.pkl")
colunas = joblib.load("../colunas.pkl")  # lista com os nomes das colunas no treino

# Configura os argumentos do terminal
parser = argparse.ArgumentParser()
parser.add_argument("--valor", type=float, required=True)
parser.add_argument("--tipo", type=str, required=True)
parser.add_argument("--hora", type=str, required=True)
parser.add_argument("--local", type=str, required=True)
parser.add_argument("--dispositivo", type=str, required=True)
args = parser.parse_args()

# Converte a hora "HH:MM" para período do dia
hora_str = args.hora
h = int(hora_str.split(":")[0])
if 6 <= h < 12:
    hora_do_dia = "Manhã"
elif 12 <= h < 18:
    hora_do_dia = "Tarde"
elif 18 <= h < 24:
    hora_do_dia = "Noite"
else:
    hora_do_dia = "Madrugada"

# Monta um dicionário com os dados da transação
entrada = {
    "Valor": args.valor,
    "Hora do Dia": hora_do_dia,
    "Tipo de Transferência": args.tipo,
    "Dispositivo": args.dispositivo,
    "Localização": args.local
}

# Cria DataFrame para entrada
df_input = pd.DataFrame([entrada])

# Aplica one-hot encoding para variáveis categóricas
df_input = pd.get_dummies(df_input)

# Reindexa para alinhar com as colunas do modelo (preenche com zeros se faltar)
df_input = df_input.reindex(columns=colunas, fill_value=0)

# Garante a ordem exata das colunas (normalmente já está ok, mas reforça)
df_input = df_input[colunas]

# Normaliza os dados usando scaler já treinado
df_input_scaled = pd.DataFrame(scaler.transform(df_input), columns=colunas)

# Faz a previsão da probabilidade de fraude
proba = modelo.predict_proba(df_input_scaled)[0][1]

print(f"Chance de fraude: {proba * 100:.2f}%")

if proba >= 0.5:
    print("Recomendação: bloquear transação.")
else:
    print("Recomendação: transação segura.")
