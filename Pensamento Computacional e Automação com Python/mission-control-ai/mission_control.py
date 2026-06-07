dadosMissao = [
    [10, 57, 22, 99, 70],
    [38, 33, 12, 78, 60],
    [31, 78, 30, 83, 71],
    [27, 60, 50, 88, 83],
    [21, 70, 80, 90, 90],
    [29, 89, 88, 95, 97]
]

dadosStatus = []

areasMonitoradas = [
    "Temperatura interna",
    "Sistema de rádio",
    "Células de energia",
    "Filtragem de oxigênio",
    "Estabilidade da estrutura"
]

recomendacoes = [
    "Verificar sistemas de resfriamento",
    "Verificar a antena de comunicação",
    "Trocar as células de energia",
    "Limpar os filtros de oxigênio",
    "Consertar qualquer dano na estrutura"
]

def VerificarTemperatura(temperatura):
    if temperatura < 20: #menor que 20 atenção
        return 1
    elif temperatura < 30: #entre 20 e 29 normal
        return 0
    elif temperatura < 35: #entre 30 e 34 atenção
        return 1
    else: #maior que 34 crítico
        return 2

def VerificarComunicacao(radio):
    if radio < 35: #menor que 35 crítico
        return 2
    elif radio < 65: #entre 35 e 64 atenção
        return 1
    else: #maior que 64 normal
        return 0

def VerificarEnergia(energia):
    if energia < 35: #menor que 35 crítico
        return 2
    elif energia < 50: #entre 35 e 49 atenção
        return 1
    else: #maior que 49 normal
        return 0

def VerificarOxigenio(oxigenio):
    if oxigenio < 80: #menor que 80 crítico
        return 2
    elif oxigenio < 90: #entre 80 e 89 atenção
        return 1
    else: #maior que 89 normal
        return 0

def VerificarEstrutura(estrutura):
    if estrutura < 70: #menor que 70 crítico
        return 2
    elif estrutura < 90: #entre 70 e 89 atenção
        return 1
    else: #maior que 89 normal
        return 0

def VerificarDados():
    for fase in dadosMissao:
        dadosStatusFase = []

        dadosStatusFase.append(VerificarTemperatura(fase[0]))
        dadosStatusFase.append(VerificarComunicacao(fase[1]))
        dadosStatusFase.append(VerificarEnergia(fase[2]))
        dadosStatusFase.append(VerificarOxigenio(fase[3]))
        dadosStatusFase.append(VerificarEstrutura(fase[4]))

        dadosStatus.append(dadosStatusFase)

def MediaDado(dado):
    soma = 0

    for fase in dadosMissao:
        soma += fase[dado]

    return soma / len(dadosMissao)

def TextoRisco(fase, area):
    if dadosStatus[fase][area] == 0:
        return "NORMAL"
    elif dadosStatus[fase][area] == 1:
        return "ATENÇÃO"
    else:
        return "CRÍTICO"

def ClassificarFase(fase):
        soma = 0

        for i in dadosStatus[fase]:
            soma += i

        if soma < 3: #entre 0 e 2
            return "ESTÁVEL", soma
        elif soma < 6: #entre 3 e 5
            return "EM ATENÇÃO", soma
        else: #entr 6 e 10
            return "CRÍTICA", soma

def TendenciaMissao():
    somaInicial = 0
    somaFinal = 0

    for status in dadosStatus[0]:
        somaInicial += status

    for status in dadosStatus[len(dadosStatus)-1]:
        somaFinal += status

    if somaFinal > somaInicial:
        return "Piorar"
    elif somaFinal < somaInicial:
        return "Melhorar"
    else:
        return "Estabilizar"

def SomarRisco(area):
    soma = 0

    for i in range(len(dadosStatus)):
        soma += dadosStatus[i][area]

    return soma

def AreaMaisAfetadaMissao():
    maiorRisco = 0
    maisAfetada = -1

    for i in range(len(areasMonitoradas)):
        if SomarRisco(i) > maiorRisco:
            maisAfetada = i
            maiorRisco = SomarRisco(i)

    match maisAfetada:
        case -1:
            return "Nenhuma"
        case 0:
            return areasMonitoradas[0]
        case 1:
            return areasMonitoradas[1]
        case 2:
            return areasMonitoradas[2]
        case 3:
            return areasMonitoradas[3]
        case 4:
            return areasMonitoradas[4]

def RecomendacoesFase(fase):
    problemaFase = 0
    recomendacoesString = ""

    if ClassificarFase(fase)[1] < 6:
        for i in range(len(areasMonitoradas)):
            if dadosStatus[fase][i] != 0:
                recomendacoesString += f"{recomendacoes[i]}, "
                problemaFase += 1
    else:
        return "Priorizar suporte à vida e preparar ejeção emergencial"

    if problemaFase == 0:
        return "Fase estável, manter monitoramento"
    else:
        recomendacoesString = recomendacoesString[:len(recomendacoesString) - 2]
        return recomendacoesString

VerificarDados()



print(f"""
============================================================================================
CONTROLE DE OPERAÇÕES
============================================================================================
Missão: Demo-2 Teste de Lançamento
Equipe: Alpha Team
Quantidade de fases analisadas: 6
============================================================================================

FASE 1
--------------------------------------------------------------------------------------------
Temperatura: {dadosMissao[0][0]}°C | {TextoRisco(0, 0)}
Comunicação: {dadosMissao[0][1]}% | {TextoRisco(0, 1)}
Energia: {dadosMissao[0][2]}% | {TextoRisco(0, 2)}
Oxigenio: {dadosMissao[0][3]}% | {TextoRisco(0, 3)}
Estabilidade: {dadosMissao[0][4]}% | {TextoRisco(0, 4)}

Pontuação de risco da fase: {ClassificarFase(0)[1]}
Classificação da fase: {ClassificarFase(0)[0]}
Recomendação: {RecomendacoesFase(0)}

FASE 2
--------------------------------------------------------------------------------------------
Temperatura: {dadosMissao[1][0]}°C | {TextoRisco(1, 0)}
Comunicação: {dadosMissao[1][1]}% | {TextoRisco(1, 1)}
Energia: {dadosMissao[1][2]}% | {TextoRisco(1, 2)}
Oxigenio: {dadosMissao[1][3]}% | {TextoRisco(1, 3)}
Estabilidade: {dadosMissao[1][4]}% | {TextoRisco(1, 4)}

Pontuação de risco da fase: {ClassificarFase(1)[1]}
Classificação da fase: {ClassificarFase(1)[0]}
Recomendação: {RecomendacoesFase(1)}

FASE 3
--------------------------------------------------------------------------------------------
Temperatura: {dadosMissao[2][0]}°C | {TextoRisco(2, 0)}
Comunicação: {dadosMissao[2][1]}% | {TextoRisco(2, 1)}
Energia: {dadosMissao[2][2]}% | {TextoRisco(2, 2)}
Oxigenio: {dadosMissao[2][3]}% | {TextoRisco(2, 3)}
Estabilidade: {dadosMissao[2][4]}% | {TextoRisco(2, 4)}

Pontuação de risco da fase: {ClassificarFase(2)[1]}
Classificação da fase: {ClassificarFase(2)[0]}
Recomendação: {RecomendacoesFase(2)}

FASE 4
--------------------------------------------------------------------------------------------
Temperatura: {dadosMissao[3][0]}°C | {TextoRisco(3, 0)}
Comunicação: {dadosMissao[3][1]}% | {TextoRisco(3, 1)}
Energia: {dadosMissao[3][2]}% | {TextoRisco(3, 2)}
Oxigenio: {dadosMissao[3][3]}% | {TextoRisco(3, 3)}
Estabilidade: {dadosMissao[3][4]}% | {TextoRisco(3, 4)}

Pontuação de risco da fase: {ClassificarFase(3)[1]}
Classificação da fase: {ClassificarFase(3)[0]}
Recomendação: {RecomendacoesFase(3)}

FASE 5
--------------------------------------------------------------------------------------------
Temperatura: {dadosMissao[4][0]}°C | {TextoRisco(4, 0)}
Comunicação: {dadosMissao[4][1]}% | {TextoRisco(4, 1)}
Energia: {dadosMissao[4][2]}% | {TextoRisco(4, 2)}
Oxigenio: {dadosMissao[4][3]}% | {TextoRisco(4, 3)}
Estabilidade: {dadosMissao[4][4]}% | {TextoRisco(4, 4)}

Pontuação de risco da fase: {ClassificarFase(4)[1]}
Classificação da fase: {ClassificarFase(4)[0]}
Recomendação: {RecomendacoesFase(4)}

FASE 6
--------------------------------------------------------------------------------------------
Temperatura: {dadosMissao[5][0]}°C | {TextoRisco(5, 0)}
Comunicação: {dadosMissao[5][1]}% | {TextoRisco(5, 1)}
Energia: {dadosMissao[5][2]}% | {TextoRisco(5, 2)}
Oxigenio: {dadosMissao[5][3]}% | {TextoRisco(5, 3)}
Estabilidade: {dadosMissao[5][4]}% | {TextoRisco(5, 4)}

Pontuação de risco da fase: {ClassificarFase(5)[1]}
Classificação da fase: {ClassificarFase(5)[0]}
Recomendação: {RecomendacoesFase(5)}

============================================================================================
RELATÓRIO FINAL DA MISSÃO
============================================================================================
Missão: Demo-2 Teste de Lançamento
Equipe: Alpha Team
Quantidade de fases analisadas: 6

Média de temperatura: {MediaDado(0):.2f}°C
Média de comunicação: {MediaDado(1):.2f}%
Média de energia: {MediaDado(2):.2f}%
Média de oxigênio: {MediaDado(3):.2f}%
Média de estabilidade: {MediaDado(4):.2f}%

Tendência da missão:
{TendenciaMissao()}

Pontuação acumulada por área:
{areasMonitoradas[0]}: {SomarRisco(0)} pontos
{areasMonitoradas[1]}: {SomarRisco(1)} pontos
{areasMonitoradas[2]}: {SomarRisco(2)} pontos
{areasMonitoradas[3]}: {SomarRisco(3)} pontos
{areasMonitoradas[4]}: {SomarRisco(4)} pontos

Área mais afetada:
{AreaMaisAfetadaMissao()}

Conclusão:
A missão começou em défict e na segunda fase, a operação
escalou rápido, além do permitido, colocando a vida dos
tripulantes em risco. Mas graças ao preparo da equipe
a situação se estabilizou e no final seguiu sem problemas.
""")