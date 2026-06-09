# ==========================================================
# GLOBAL SOLUTION
# Sistema Inteligente de Monitoramento para Missão Espacial
#
# Integrantes:
# André Felix - 571691
# Gabriel Silveira - 568910
# Sala: 1CCPQ
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# 1. LEITURA DA BASE DE DADOS
# ==========================================================

arquivo = "base_dados.csv"

df = pd.read_csv(arquivo)

# Remove espaços extras dos nomes das colunas
df.columns = df.columns.str.strip()

# ==========================================================
# 2. TRATAMENTO DOS DADOS
# ==========================================================

# Remove registros inválidos (-99.9)
df = df[df["MEAN TEMP"] > -90]

# ==========================================================
# 3. CRIAÇÃO DA VARIÁVEL DISCRETA
# ==========================================================

# Sistema simples de alerta operacional
# 1 = Alerta
# 0 = Normal

df["ALERTA_OPERACIONAL"] = (df["MEAN TEMP"] > 80).astype(int)

# ==========================================================
# 4. TABELA DE FREQUÊNCIA
# VARIÁVEL QUANTITATIVA DISCRETA
# ==========================================================

print("\n" + "=" * 60)
print("TABELA DE FREQUÊNCIA - ALERTA OPERACIONAL")
print("=" * 60)

freq_discreta = (
    df["ALERTA_OPERACIONAL"]
    .value_counts()
    .sort_index()
)

freq_discreta_relativa = (
    df["ALERTA_OPERACIONAL"]
    .value_counts(normalize=True)
    .sort_index()
    * 100
)

tabela_discreta = pd.DataFrame({
    "Frequência": freq_discreta,
    "Percentual (%)": freq_discreta_relativa.round(2)
})

print(tabela_discreta)

# ==========================================================
# 5. TABELA DE FREQUÊNCIA
# VARIÁVEL QUANTITATIVA CONTÍNUA
# ==========================================================

print("\n" + "=" * 60)
print("TABELA DE FREQUÊNCIA - TEMPERATURA MÉDIA")
print("=" * 60)

classes = pd.cut(
    df["MEAN TEMP"],
    bins=6
)

freq_continua = classes.value_counts().sort_index()

freq_continua_relativa = (
    classes.value_counts(normalize=True)
    .sort_index()
    * 100
)

tabela_continua = pd.DataFrame({
    "Frequência": freq_continua,
    "Percentual (%)": freq_continua_relativa.round(2)
})

print(tabela_continua)

# ==========================================================
# 6. ESTATÍSTICA DESCRITIVA
# ==========================================================

print("\n" + "=" * 60)
print("ESTATÍSTICA DESCRITIVA - TEMPERATURA MÉDIA")
print("=" * 60)

media = df["MEAN TEMP"].mean()
mediana = df["MEAN TEMP"].median()
moda = df["MEAN TEMP"].mode()[0]

maximo = df["MEAN TEMP"].max()
minimo = df["MEAN TEMP"].min()

amplitude = maximo - minimo

variancia = df["MEAN TEMP"].var()

desvio_padrao = df["MEAN TEMP"].std()

coeficiente_variacao = (
    desvio_padrao / media
) * 100

quartis = df["MEAN TEMP"].quantile(
    [0.25, 0.50, 0.75]
)

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")

print(f"Máximo: {maximo:.2f}")
print(f"Mínimo: {minimo:.2f}")

print(f"Amplitude: {amplitude:.2f}")

print(f"Variância: {variancia:.2f}")

print(f"Desvio Padrão: {desvio_padrao:.2f}")

print(
    f"Coeficiente de Variação: "
    f"{coeficiente_variacao:.2f}%"
)

print("\nQuartis")

print(f"Q1: {quartis[0.25]:.2f}")
print(f"Q2: {quartis[0.50]:.2f}")
print(f"Q3: {quartis[0.75]:.2f}")

# ==========================================================
# 7. GRÁFICO 1
# HISTOGRAMA DA TEMPERATURA MÉDIA
# ==========================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["MEAN TEMP"],
    bins=10
)

plt.title(
    "Distribuição da Temperatura Média"
)

plt.xlabel(
    "Temperatura Média (°F)"
)

plt.ylabel(
    "Frequência"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "grafico_temperatura_media.png"
)

plt.show()

# ==========================================================
# 8. GRÁFICO 2
# ALERTAS OPERACIONAIS
# ==========================================================

plt.figure(figsize=(8, 5))

freq_discreta.plot(
    kind="bar"
)

plt.title(
    "Frequência de Alertas Operacionais"
)

plt.xlabel(
    "Situação"
)

plt.ylabel(
    "Quantidade de Dias"
)

plt.xticks(
    [0, 1],
    ["Normal", "Alerta"],
    rotation=0
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "grafico_alertas_operacionais.png"
)

plt.show()

# ==========================================================
# 9. RESUMO FINAL
# ==========================================================

print("\n" + "=" * 60)
print("ANÁLISE FINAL")
print("=" * 60)

print(
    "A região analisada apresentou comportamento "
    "climático relativamente estável ao longo "
    "do período estudado."
)

print(
    "O sistema de alertas permite identificar "
    "automaticamente dias com temperaturas "
    "mais elevadas, auxiliando o monitoramento "
    "operacional de uma missão espacial "
    "experimental."
)

print("\nINSIGHT 1")
print(
    "A baixa variabilidade observada na temperatura "
    "indica condições relativamente estáveis para "
    "operações monitoradas."
)

print("\nINSIGHT 2")
print(
    "O monitoramento automático de alertas permite "
    "identificar rapidamente condições que exigem "
    "atenção operacional."
)