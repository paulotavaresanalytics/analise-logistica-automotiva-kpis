import pandas as pd

def carregar_dados():
    return pd.read_csv('../data/dados_frota.csv')

def custo_por_km(df):
    df['custo_total'] = df['custo_manutencao']
    df['custo_km'] = df['custo_total'] / df['km_rodado']
    return df

def consumo_combustivel(df):
    df['consumo_km_l'] = df['km_rodado'] / df['combustivel_litros']
    return df

def tempo_medio_entrega(df):
    return df['tempo_entrega_horas'].mean()

if __name__ == "__main__":
    df = carregar_dados()
    df = custo_por_km(df)
    df = consumo_combustivel(df)

    print(df)
    print("Tempo médio de entrega:", tempo_medio_entrega(df))
