# ==========================================================
# GLOBAL SOLUTION 2026.1
# EcoSpace Monitor
#
# André Felix - 571691
# Gabriel Silveira - 568910
# ==========================================================

from datetime import datetime

# ==========================================================
# CONFIGURAÇÃO DO CENÁRIO
# ==========================================================
# 1 = Operação normal
# 2 = Temperatura alta e energia baixa
# 3 = Falha de comunicação

cenario = 2

# ==========================================================
# DADOS DA MISSÃO
# ==========================================================

if cenario == 1:

    temperatura = 45
    energia = 85
    comunicacao = True

    modulo_cientifico = "Operacional"
    modulo_navegacao = "Operacional"
    modulo_suporte_vida = "Operacional"

elif cenario == 2:

    temperatura = 87
    energia = 28
    comunicacao = True

    modulo_cientifico = "Operacional"
    modulo_navegacao = "Atenção"
    modulo_suporte_vida = "Operacional"

else:

    temperatura = 58
    energia = 70
    comunicacao = False

    modulo_cientifico = "Operacional"
    modulo_navegacao = "Operacional"
    modulo_suporte_vida = "Manutenção"

# ==========================================================
# CABEÇALHO
# ==========================================================

print("=" * 60)
print("ECOSPACE MONITOR")
print("=" * 60)

print("Sistema inteligente de monitoramento")
print("para missão espacial experimental.")

print(
    "\nData/Hora da análise:",
    datetime.now().strftime("%d/%m/%Y %H:%M:%S")
)

# ==========================================================
# EXIBIÇÃO DOS DADOS
# ==========================================================

print("\nDADOS DA MISSÃO")
print("-" * 60)

print(f"Temperatura: {temperatura}°C")
print(f"Energia disponível: {energia}%")

if comunicacao:
    print("Comunicação: OK")
else:
    print("Comunicação: FALHA")

print(f"Módulo Científico: {modulo_cientifico}")
print(f"Módulo de Navegação: {modulo_navegacao}")
print(f"Módulo de Suporte à Vida: {modulo_suporte_vida}")

# ==========================================================
# INDICADOR DE SUSTENTABILIDADE
# ==========================================================

indice_sustentabilidade = energia / temperatura

print(
    f"\nÍndice de Sustentabilidade: "
    f"{indice_sustentabilidade:.2f}"
)

# ==========================================================
# VERIFICAÇÃO DE ALERTAS
# ==========================================================

print("\n" + "=" * 60)
print("VERIFICAÇÃO DE ALERTAS")
print("=" * 60)

alerta = False

if temperatura > 80:

    alerta = True

    print("\nALERTA CRÍTICO DE TEMPERATURA")
    print("Temperatura acima do limite seguro.")

    print("AÇÃO AUTOMÁTICA:")
    print("Ativando sistema de resfriamento.")

if energia < 30:

    alerta = True

    print("\nALERTA DE ENERGIA")
    print("Nível de energia abaixo do ideal.")

    print("AÇÃO AUTOMÁTICA:")
    print("Reduzindo consumo dos módulos secundários.")

if not comunicacao:

    alerta = True

    print("\nALERTA DE COMUNICAÇÃO")
    print("Falha de comunicação detectada.")

    print("AÇÃO AUTOMÁTICA:")
    print("Ativando canal de comunicação reserva.")

if modulo_cientifico != "Operacional":

    alerta = True

    print("\nALERTA NO MÓDULO CIENTÍFICO")

    print("AÇÃO AUTOMÁTICA:")
    print("Executando diagnóstico do módulo.")

if modulo_navegacao != "Operacional":

    alerta = True

    print("\nALERTA NO MÓDULO DE NAVEGAÇÃO")

    print("AÇÃO AUTOMÁTICA:")
    print("Verificando sensores e rota.")

if modulo_suporte_vida != "Operacional":

    alerta = True

    print("\nALERTA NO MÓDULO DE SUPORTE À VIDA")

    print("AÇÃO AUTOMÁTICA:")
    print("Ativando protocolo de segurança.")

if not alerta:

    print("\nNenhum alerta detectado.")
    print("Todos os sistemas operam normalmente.")

# ==========================================================
# STATUS DA MISSÃO
# ==========================================================

print("\n" + "=" * 60)
print("STATUS DA MISSÃO")
print("=" * 60)

if (
    temperatura <= 80
    and energia >= 30
    and comunicacao
    and modulo_cientifico == "Operacional"
    and modulo_navegacao == "Operacional"
    and modulo_suporte_vida == "Operacional"
):
    print("MISSÃO OPERANDO NORMALMENTE")
else:
    print("MISSÃO OPERANDO COM RESTRIÇÕES")
    print("Monitoramento intensificado recomendado.")

# ==========================================================
# AVALIAÇÃO DE SUSTENTABILIDADE
# ==========================================================

print("\n" + "=" * 60)
print("AVALIAÇÃO DE SUSTENTABILIDADE")
print("=" * 60)

if indice_sustentabilidade >= 1:
    print("Situação energética favorável.")
elif indice_sustentabilidade >= 0.5:
    print("Situação energética aceitável.")
else:
    print("Situação energética crítica.")

# ==========================================================
# RESUMO OPERACIONAL
# ==========================================================

print("\n" + "=" * 60)
print("RESUMO OPERACIONAL")
print("=" * 60)

print("A missão foi monitorada continuamente pelo sistema.")
print("As condições térmicas, energéticas e operacionais foram avaliadas.")
print("Alertas automáticos foram emitidos para situações críticas.")
print("O sistema recomendou ações corretivas para manter a segurança da missão.")
print("Processo de monitoramento finalizado.")