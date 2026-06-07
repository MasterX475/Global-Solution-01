# Sistema de Controle de Operações Espaciais

Projeto desenvolvido em Python para simular o monitoramento de uma missão espacial em múltiplas fases, avaliando riscos operacionais do foguete e gerando relatórios automáticos de análise da missão.

---

# Objetivo do Projeto

O sistema realiza a análise de dados críticos de um foguete durante diferentes fases de uma missão de teste.

A aplicação:

* Monitora áreas essenciais do foguete
* Classifica níveis de risco
* Calcula médias operacionais
* Detecta tendências da missão
* Identifica áreas mais afetadas
* Gera recomendações automáticas de segurança

---

# Áreas Monitoradas

Durante cada fase da missão, o sistema analisa cinco áreas principais:

| Área                      | Descrição                   |
|---------------------------|-----------------------------|
| Temperatura interna       | Controle térmico do foguete |
| Sistema de rádio          | Comunicação com a base      |
| Células de energia        | Alimentação elétrica        |
| Filtragem de oxigênio     | Qualidade do ar interno     |
| Estabilidade da estrutura | Integridade estrutural      |

---

# Estrutura dos Dados

Os dados da missão são armazenados na variável:

```text
dadosMissao[]
```

Cada linha representa uma fase da missão:

```text
[
    temperatura,
    comunicação,
    energia,
    oxigênio,
    estabilidade
]
```

Exemplo:

```text
[10, 57, 22, 99, 70]
```

Significa:

| Indicador   | Valor |
|-------------|-------|
| Temperatura | 10°C  |
| Comunicação | 57%   |
| Energia     | 22%   |
| Oxigênio    | 99%   |
| Estrutura   | 70%   |

---

# Sistema de Classificação de Risco

O sistema utiliza três níveis de risco:

| Valor Numérico | Classificação |
|----------------|---------------|
| 0              | NORMAL        |
| 1              | ATENÇÃO       |
| 2              | CRÍTICO       |

---

# Variáveis Globais

## `dadosMissao`

Matriz principal contendo os dados coletados em cada fase da missão.

---

## `dadosStatus`

Armazena os níveis de risco calculados para cada área monitorada.

Exemplo:

```text
[
    [1, 1, 2, 0, 1]
]
```

---

## `areasMonitoradas`

Lista textual com os nomes das áreas analisadas.

---

## `recomendacoes`

Lista de recomendações utilizadas para sugerir ações corretivas durante a missão.

---

# Funções do Sistema

## `VerificarTemperatura(temperatura)`

Analisa a temperatura interna do foguete.

| Faixa               | Resultado |
|---------------------|-----------|
| Menor que 20        | ATENÇÃO   |
| 20 a 29             | NORMAL    |
| 30 a 34             | ATENÇÃO   |
| Maior ou igual a 35 | CRÍTICO   |

---

## `VerificarComunicacao(radio)`

Avalia a qualidade da comunicação do sistema de rádio.

| Faixa               | Resultado |
|---------------------|-----------|
| Menor que 35        | CRÍTICO   |
| 35 a 64             | ATENÇÃO   |
| Maior ou igual a 65 | NORMAL    |

---

## `VerificarEnergia(energia)`

Verifica a condição das células de energia.

| Faixa               | Resultado |
|---------------------|-----------|
| Menor que 35        | CRÍTICO   |
| 35 a 49             | ATENÇÃO   |
| Maior ou igual a 50 | NORMAL    |

---

## `VerificarOxigenio(oxigenio)`

Avalia a eficiência da filtragem de oxigênio.

| Faixa               | Resultado |
|---------------------|-----------|
| Menor que 80        | CRÍTICO   |
| 80 a 89             | ATENÇÃO   |
| Maior ou igual a 90 | NORMAL    |

---

## `VerificarEstrutura(estrutura)`

Analisa a integridade estrutural do foguete.

| Faixa               | Resultado |
|---------------------|-----------|
| Menor que 70        | CRÍTICO   |
| 70 a 89             | ATENÇÃO   |
| Maior ou igual a 90 | NORMAL    |

---

## `VerificarDados()`

Percorre todas as fases da missão e aplica as funções de verificação para gerar a matriz de riscos:

```text
dadosStatus[]
```

---

## `MediaDado(dado)`

Calcula a média de uma área monitorada durante toda a missão.

### Exemplo

```text
MediaDado(0)
```

Retorna a média da temperatura durante a missão.

---

## `TextoRisco(fase, area)`

Converte o valor numérico do risco em texto legível.

### Conversões

| Número | Texto   |
|--------|---------|
| 0      | NORMAL  |
| 1      | ATENÇÃO |
| 2      | CRÍTICO |

---

## `ClassificarFase(fase)`

Calcula a pontuação total de risco da fase e define sua classificação.

| Soma dos Riscos | Resultado  |
|-----------------|------------|
| 0 a 2           | ESTÁVEL    |
| 3 a 5           | EM ATENÇÃO |
| 6 a 10          | CRÍTICA    |

### Retorno

A função retorna:

```text
(classificacao, pontuacao)
```

Exemplo:

```text
("EM ATENÇÃO", 4)
```

---

## `TendenciaMissao()`

Compara os riscos da primeira e da última fase da missão.

### Possíveis resultados

* `"Melhorar"`
* `"Piorar"`
* `"Estabilizar"`

---

## `SomarRisco(area)`

Calcula o risco acumulado de uma área durante toda a missão.

---

## `AreaMaisAfetadaMissao()`

Identifica qual área apresentou maior risco acumulado.

---

## `RecomendacoesFase(fase)`

Gera recomendações automáticas de acordo com os riscos detectados.

### Possíveis comportamentos

* Retorna ações corretivas específicas
* Retorna mensagem de estabilidade
* Retorna protocolo emergencial em casos críticos

Exemplo:

```text
"Verificar sistemas de resfriamento"
```

Ou:

```text
"Priorizar suporte à vida e preparar ejeção emergencial"
```

---

# Fluxo de Execução

```text
1. Carregamento dos dados da missão
2. Verificação dos riscos
3. Geração da matriz de status
4. Classificação de cada fase
5. Geração de recomendações
6. Cálculo de médias e tendências
7. Emissão do relatório final
```

---

# Relatório Gerado

O sistema imprime:

* Status detalhado de cada fase
* Pontuação de risco
* Classificação operacional
* Recomendações automáticas
* Médias da missão
* Tendência geral
* Área mais afetada
* Conclusão final

---

# Exemplo de Saída

```text
FASE 1
Temperatura: 10°C | ATENÇÃO
Comunicação: 57% | ATENÇÃO
Energia: 22% | CRÍTICO

Pontuação de risco da fase: 5
Classificação da fase: EM ATENÇÃO
```

