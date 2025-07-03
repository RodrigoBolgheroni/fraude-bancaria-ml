import random
import pandas as pd
import os

def gerar_dados(t):
    valores_baixos = [random.randint(10, 3000) for _ in range(int(t * 0.85))]
    valores_altos = [random.randint(3001, 15000) for _ in range(t - int(t * 0.85))]
    valor_transferencia = valores_baixos + valores_altos
    random.shuffle(valor_transferencia) 

    # Hora do dia
    horarios = ["Manhã", "Tarde", "Noite", "Madrugada"]
    hora_do_dia = random.choices(horarios, weights=[0.3, 0.3, 0.25, 0.15], k=t)

    # Tipo de transação
    tipos = ["PIX", "Débito", "Crédito", "Boleto", "Transferência"]
    tipo_de_transferencia = random.choices(tipos, weights=[0.4, 0.25, 0.15, 0.1, 0.1], k=t)

    # Dispositivo do usuário
    dispositivos = ["Android", "iPhone", "PC", "Caixa Eletrônico"]
    dispositivo_do_usuario = random.choices(dispositivos, weights=[0.4, 0.3, 0.2, 0.1], k=t)

    # Localização
    locais = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Miami", "Nova York", "Lisboa", "?"]
    localizacao_transacao = random.choices(locais, weights=[0.5, 0.2, 0.1, 0.08, 0.05, 0.04, 0.02], k=t)

    fraude = []

    for i in range(t):
        chance_fraude = 0
        if valor_transferencia[i] > 3000:
            chance_fraude += 15
        if hora_do_dia[i] in ['Madrugada']:
            chance_fraude += 20
        if tipo_de_transferencia[i] in ['PIX','Débito','Boleto']:
            chance_fraude += 5
        if dispositivo_do_usuario[i] in ['Caixa Eletrônico','PC']:
            chance_fraude += 10
        if localizacao_transacao[i] in ['?']:
            chance_fraude += 45
        elif localizacao_transacao[i] in ['Lisboa','Nova York','Miami']:
            chance_fraude += 35

        if chance_fraude >= 70:
            fraude.append(1)
        else:
            fraude.append(0)
    dados = {
        "Valor": valor_transferencia,
        "Hora do Dia": hora_do_dia,
        "Tipo de Transferência": tipo_de_transferencia,
        "Dispositivo": dispositivo_do_usuario,
        "Localização": localizacao_transacao,
        "Fraude": fraude
    }
    return dados


def transformar_em_csv(caminho, t):
    pasta = os.path.dirname(caminho)
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    dados = gerar_dados(t)
    df = pd.DataFrame(dados)
    df.to_csv(caminho, index=False)





