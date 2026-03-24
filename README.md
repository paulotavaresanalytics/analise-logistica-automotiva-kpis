# 🚗 Projeto de Análise de Dados — Logística Automotiva

Projeto de portfólio para GitHub com dados fictícios de uma operação logística de uma indústria automotiva de médio porte (~200 funcionários), responsável pela distribuição de peças e produtos em nível regional.

O objetivo é analisar indicadores estratégicos que auxiliam a área de logística, operações e supply chain na tomada de decisão.

---

## 🎯 Objetivos do projeto

Neste projeto, foram desenvolvidas e calculadas as seguintes métricas:

- Custo por KM (R$/km)
- Consumo de combustível (km/L)
- Análise de manutenção preventiva
- Tempo médio de entrega
- Eficiência logística (roteirização básica)

---

## 🏭 Contexto do negócio

A empresa fictícia realiza transporte de mercadorias entre centros de distribuição e clientes finais, operando com uma frota própria de veículos.

Características da empresa:

- Setor: Logística automotiva  
- Porte: Médio  
- Funcionários: Aproximadamente 200  
- Período analisado: Janeiro a Dezembro de 2025  
- Frota analisada: 15 veículos  

---

## 📁 Estrutura do projeto

analise-logistica-automotiva-kpis/
├── data/
│   └── dados_frota.csv
├── notebooks/
│   └── analise.ipynb
├── src/
│   └── kpis.py
├── reports/
│   └── insights.md
├── docs/
│   └── dicionario_dados.md
├── requirements.txt
├── .gitignore
└── README.md

---

## 📊 Dicionário dos dados

dados_frota.csv

| Coluna | Descrição |
|--------|----------|
| veiculo | Identificador do veículo |
| km_rodado | Quilometragem percorrida |
| combustivel_litros | Consumo total de combustível |
| custo_manutencao | Custo de manutenção no período |
| tempo_entrega_horas | Tempo total de entrega |

---

## 📐 Regras de negócio e fórmulas

Custo por KM  
custo por km = custo de manutenção / km rodado  

Consumo de combustível  
consumo (km/L) = km rodado / combustível utilizado  

Tempo médio de entrega  
tempo médio = média do tempo de entrega dos veículos  

Análise de manutenção  
Identificação de veículos com maior custo operacional, indicando necessidade de manutenção preventiva.

Eficiência logística  
Avaliação baseada no tempo de entrega e consumo de combustível.

---

## 📈 Principais insights

- Veículos com alto custo por km apresentam baixa eficiência operacional  
- Diferença significativa no consumo de combustível entre veículos  
- O tempo médio de entrega pode ser reduzido com melhor roteirização  
- Manutenção preventiva impacta diretamente no custo logístico  

---

## 📊 Visualizações

- Custo por KM por veículo  
- Consumo de combustível  
- Tempo de entrega  
- Ranking de eficiência da frota  

---

## 🛠️ Tecnologias utilizadas

- Python  
- Pandas  
- Matplotlib  

---

## 🚀 Como executar o projeto

git clone <SEU_LINK_DO_REPOSITORIO>  
cd analise-logistica-automotiva-kpis  

python -m venv .venv  
source .venv/bin/activate  

pip install -r requirements.txt  

python src/kpis.py  

---

## 💡 Ideias para evolução do projeto

- Criar dashboard em Power BI  
- Construir aplicação em Streamlit  
- Implementar previsão de demanda logística  
- Adicionar análise de rotas com otimização  
- Criar ranking de veículos mais eficientes  
- Implementar alertas de manutenção preventiva  
- Incluir análise de custo total logístico  
- Integrar com dados reais (API ou ERP)
