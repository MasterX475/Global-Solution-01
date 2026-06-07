
## Variáveis Globais
### (Uso de Lower CamelCase para declaração)

- **dadosMissão** - Guarda a matriz de dados de cada área monitorada.
- **dadosStatus** - Declarada como array vazia para posteriormente encadear os pontos de risco de cada dado  
com a matriz de *dadosMissão*.
- **areasMonitoradas** - Representa o que está sendo monitorado.
- **recomendacoes** - Um array de textos para recomendar possíveis ações após a análise de riscos.

## Funções
### (Uso de Upper CamelCase para declaração)

- **VerificarTemperatura** - Verifica se a temperatura interna se encontra em padrões aceitáveis.

|     Valor      |  Risco   |
|:--------------:|:--------:|
|  Menor que 20  | ATENÇÃO  |
| Entre 20 e 29  |  NORMAL  |
| Entre 30 e 34  | ATENÇÃO  |
|  Maior que 34  | CRÍTICO  |

- **VerificarComunicacao** - Verifica se o sistema de rádio está em boa operação.

|     Valor      |  Risco   |
|:--------------:|:--------:|
|  Menor que 35  | CRÍTICO  |
| Entre 35 e 64  | ATENÇÃO  |
|  Maior que 64  |  NORMAL  |

- **VerificarEnergia** - Verifica as células de energia (baterias).

|     Valor      |  Risco   |
|:--------------:|:--------:|
|  Menor que 35  | CRÍTICO  |
| Entre 35 e 49  | ATENÇÃO  |
|  Maior que 49  |  NORMAL  |

- **VerificarOxigênio** - Verifica a respirabilidade do ar após a filtragem.

|     Valor      |  Risco   |
|:--------------:|:--------:|
|  Menor que 80  | CRÍTICO  |
| Entre 80 e 89  | ATENÇÃO  |
|  Maior que 89  |  NORMAL  |

- **VerificarEstrutura** - Verifica a integridade das estruturas físicas do foguete.

|     Valor      |  Risco   |
|:--------------:|:--------:|
|  Menor que 70  | CRÍTICO  |
| Entre 70 e 89  | ATENÇÃO  |
|  Maior que 89  |  NORMAL  |

- **VerificarDados** - Usa as funções de verificação criadas anteriormente para fazer uma nova matriz  
que será armazenada na variável *dadosStatus*.
- **MediaDados** - Faz a media final de risco para a área colocada no parâmetro.
- **TextoRisco** - Transforma o dado de risco numérico em uma frase correspondente.
- **ClassificarFase** - Soma o risco da fase indicada e a classifica de acordo.

| Valor  |  Resultado  |
|:------:|:-----------:|
| 0 a 2  |   ESTÁVEL   |
| 3 a 5  | EM ATENÇÃO  |
| 6 a 10 |   CRÍTICA   |

- **TendênciaMissão** - Soma os riscos da fase inicial e final para ver a tendência da missão.
- **SomarRisco** - Soma os riscos de uma área durante toda a missão.
- **AreaMaisAfetadaMissao** - Usa a função *SomarRisco* para descobrir qual a área  
com mais pontos de riscos até o final da missão.
- **RecomendacoesFase** - De acordo com a pontuação das áreas, concatena strings  
da variável *recomendacoes* em uma grande variável para exibição.
