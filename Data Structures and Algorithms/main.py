import random
import time

# ==========================
# CORES DO TERMINAL
# ==========================

VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"

# ==========================
# ESTRUTURAS DE DADOS
# ==========================

historico = []
ultima_leitura = None

# ==========================
# FUNÇÕES AUXILIARES
# ==========================

def exibir_cabecalho():
    print(AZUL + "=" * 50)
    print("     MONITORAMENTO DE MISSÃO ESPACIAL")
    print("=" * 50 + RESET)


def animacao_analise():
    etapas = [
        "Coletando dados dos sensores",
        "Verificando temperatura",
        "Verificando energia",
        "Verificando comunicação",
        "Calculando status operacional",
        "Finalizando análise"
    ]

    print()

    for etapa in etapas:
        print(etapa, end="", flush=True)

        for _ in range(3):
            time.sleep(0.25)
            print(".", end="", flush=True)

        print()

    print()


def calcular_status(leitura):

    alertas = 0

    if leitura["temperatura"] > 80:
        alertas += 1

    if leitura["energia"] < 20:
        alertas += 1

    if leitura["comunicacao"] == 0:
        alertas += 1

    if alertas == 0:
        return "OPERACIONAL"

    elif alertas == 1:
        return "ATENÇÃO"

    else:
        return "CRÍTICO"


# ==========================
# INSERÇÃO MANUAL
# ==========================

def inserir_dados():

    global ultima_leitura

    try:

        temperatura = float(
            input("Temperatura da nave (°C): ")
        )

        energia = float(
            input("Nível de energia (%): ")
        )

        comunicacao = int(
            input("Comunicação (1 = Ativa | 0 = Falha): ")
        )

        while comunicacao not in [0, 1]:
            comunicacao = int(
                input("Digite apenas 0 ou 1: ")
            )

        leitura = {
            "temperatura": temperatura,
            "energia": energia,
            "comunicacao": comunicacao
        }

        leitura["status"] = calcular_status(leitura)

        historico.append(leitura)

        ultima_leitura = leitura

        print(
            VERDE +
            "\nLeitura cadastrada com sucesso!\n" +
            RESET
        )

    except ValueError:

        print(
            VERMELHO +
            "\nValor inválido.\n" +
            RESET
        )


# ==========================
# SIMULAÇÃO AUTOMÁTICA
# ==========================

def simular_sensores():

    global ultima_leitura

    temperatura = random.randint(40, 100)
    energia = random.randint(0, 100)
    comunicacao = random.randint(0, 1)

    leitura = {
        "temperatura": temperatura,
        "energia": energia,
        "comunicacao": comunicacao
    }

    leitura["status"] = calcular_status(leitura)

    historico.append(leitura)
    ultima_leitura = leitura

    print(AZUL + "\nSIMULAÇÃO AUTOMÁTICA\n" + RESET)

    print(f"Temperatura: {temperatura} °C")
    print(f"Energia: {energia}%")

    if comunicacao == 1:
        print("Comunicação: ATIVA")
    else:
        print("Comunicação: FALHA")

    print(f"Status: {leitura['status']}")

    executar_analise()


# ==========================
# MONITORAMENTO CONTÍNUO
# ==========================

def monitoramento_continuo():

    global ultima_leitura

    quantidade = 5

    print(
        AZUL +
        "\nINICIANDO MONITORAMENTO CONTÍNUO\n" +
        RESET
    )

    for ciclo in range(quantidade):

        temperatura = random.randint(40, 100)
        energia = random.randint(0, 100)
        comunicacao = random.randint(0, 1)

        leitura = {
            "temperatura": temperatura,
            "energia": energia,
            "comunicacao": comunicacao
        }

        leitura["status"] = calcular_status(leitura)

        historico.append(leitura)

        ultima_leitura = leitura

        print("=" * 35)
        print(f"LEITURA {ciclo + 1}")
        print("=" * 35)

        print(f"Temperatura: {temperatura} °C")
        print(f"Energia: {energia}%")

        if comunicacao == 1:
            print("Comunicação: ATIVA")
        else:
            print("Comunicação: FALHA")

        print(f"Status: {leitura['status']}")

        time.sleep(2)

    print(
        VERDE +
        "\nMonitoramento finalizado.\n" +
        RESET
    )


# ==========================
# VISUALIZAR STATUS
# ==========================

def visualizar_status():

    if ultima_leitura is None:

        print(
            AMARELO +
            "\nNenhuma leitura cadastrada.\n" +
            RESET
        )

        return

    print("\n===== STATUS ATUAL =====")

    print(
        f"Temperatura: "
        f"{ultima_leitura['temperatura']} °C"
    )

    print(
        f"Energia: "
        f"{ultima_leitura['energia']}%"
    )

    if ultima_leitura["comunicacao"] == 1:
        print("Comunicação: ATIVA")
    else:
        print("Comunicação: FALHA")

    status = ultima_leitura["status"]

    if status == "OPERACIONAL":

        print(
            VERDE +
            f"Status da Missão: {status}" +
            RESET
        )

    elif status == "ATENÇÃO":

        print(
            AMARELO +
            f"Status da Missão: {status}" +
            RESET
        )

    else:

        print(
            VERMELHO +
            f"Status da Missão: {status}" +
            RESET
        )

    print()


# ==========================
# ANÁLISE
# ==========================

def executar_analise():

    if ultima_leitura is None:

        print(
            AMARELO +
            "\nNenhuma leitura cadastrada.\n" +
            RESET
        )

        return

    animacao_analise()

    print("===== RESULTADO DA ANÁLISE =====")

    problemas = False

    if ultima_leitura["temperatura"] > 80:

        print(
            VERMELHO +
            "ALERTA: Superaquecimento detectado." +
            RESET
        )

        problemas = True

    if ultima_leitura["energia"] < 20:

        print(
            AMARELO +
            "ALERTA: Ativar economia de energia." +
            RESET
        )

        problemas = True

    if ultima_leitura["comunicacao"] == 0:

        print(
            VERMELHO +
            "ALERTA: Falha de comunicação." +
            RESET
        )

        problemas = True

    if not problemas:

        print(
            VERDE +
            "Missão operando normalmente." +
            RESET
        )

    print()


# ==========================
# HISTÓRICO
# ==========================

def mostrar_historico():

    if len(historico) == 0:

        print(
            AMARELO +
            "\nNenhum registro encontrado.\n" +
            RESET
        )

        return

    print("\n===== HISTÓRICO DE LEITURAS =====")

    for indice in range(len(historico)):

        leitura = historico[indice]

        print("\n-----------------------------")
        print(f"Leitura #{indice + 1}")

        print(
            f"Temperatura: "
            f"{leitura['temperatura']} °C"
        )

        print(
            f"Energia: "
            f"{leitura['energia']}%"
        )

        if leitura["comunicacao"] == 1:
            print("Comunicação: ATIVA")
        else:
            print("Comunicação: FALHA")

        print(f"Status: {leitura['status']}")

    print()


# ==========================
# ESTATÍSTICAS
# ==========================

def mostrar_estatisticas():

    if len(historico) == 0:

        print(
            AMARELO +
            "\nNenhum dado disponível.\n" +
            RESET
        )

        return

    maior_temperatura = historico[0]["temperatura"]
    menor_energia = historico[0]["energia"]
    falhas = 0

    for leitura in historico:

        if leitura["temperatura"] > maior_temperatura:
            maior_temperatura = leitura["temperatura"]

        if leitura["energia"] < menor_energia:
            menor_energia = leitura["energia"]

        if leitura["comunicacao"] == 0:
            falhas += 1

    print("\n===== ESTATÍSTICAS DA MISSÃO =====")

    print(f"Total de leituras: {len(historico)}")

    print(
        f"Maior temperatura registrada: "
        f"{maior_temperatura} °C"
    )

    print(
        f"Menor nível de energia registrado: "
        f"{menor_energia}%"
    )

    print(
        f"Falhas de comunicação registradas: "
        f"{falhas}"
    )

    print()


# ==========================
# MENU PRINCIPAL
# ==========================

while True:

    exibir_cabecalho()

    print("1 - Inserir dados manualmente")
    print("2 - Visualizar status atual")
    print("3 - Executar análise")
    print("4 - Histórico das leituras")
    print("5 - Estatísticas da missão")
    print("6 - Simulação automática")
    print("7 - Monitoramento contínuo")
    print("8 - Encerrar sistema")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        inserir_dados()

    elif opcao == "2":
        visualizar_status()

    elif opcao == "3":
        executar_analise()

    elif opcao == "4":
        mostrar_historico()

    elif opcao == "5":
        mostrar_estatisticas()

    elif opcao == "6":
        simular_sensores()

    elif opcao == "7":
        monitoramento_continuo()

    elif opcao == "8":

        print(
            VERDE +
            "\nSistema encerrado com sucesso." +
            RESET
        )

        break

    else:

        print(
            VERMELHO +
            "\nOpção inválida.\n" +
            RESET
        )