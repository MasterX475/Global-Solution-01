# EcoSpace Monitor

## Descrição

O EcoSpace Monitor é um sistema inteligente de monitoramento desenvolvido para uma missão espacial experimental. O projeto foi criado com o objetivo de acompanhar condições operacionais simuladas, permitindo a identificação automática de situações críticas e auxiliando na tomada de decisões durante a missão.

O sistema monitora indicadores essenciais para o funcionamento da operação espacial, incluindo temperatura, energia disponível, comunicação e status dos módulos da missão. Com base nesses dados, são gerados alertas automáticos e recomendações de ações corretivas quando necessário.

## Objetivo

Desenvolver uma solução capaz de receber, interpretar e exibir informações operacionais de uma missão espacial experimental, utilizando conceitos de programação, lógica computacional e automação para auxiliar o monitoramento das condições da missão.

## Funcionalidades

* Monitoramento da temperatura da missão.
* Monitoramento do nível de energia disponível.
* Verificação do status da comunicação.
* Acompanhamento dos módulos operacionais.
* Geração automática de alertas.
* Tomada de decisão automatizada para situações críticas.
* Avaliação simplificada de sustentabilidade energética.
* Exibição organizada das informações operacionais.

## Estrutura Monitorada

O sistema realiza o acompanhamento dos seguintes elementos:

* Temperatura da missão.
* Energia disponível.
* Comunicação.
* Módulo Científico.
* Módulo de Navegação.
* Módulo de Suporte à Vida.

## Sistema de Alertas

O EcoSpace Monitor identifica automaticamente condições que possam comprometer a operação da missão.

Entre os eventos monitorados estão:

* Temperatura acima do limite seguro.
* Baixo nível de energia.
* Falhas de comunicação.
* Alterações no status dos módulos.

Quando uma situação crítica é detectada, o sistema apresenta um alerta e sugere uma ação corretiva apropriada.

## Sustentabilidade

Além do monitoramento operacional, o projeto realiza uma avaliação simplificada da sustentabilidade energética da missão por meio de um indicador calculado a partir dos níveis de energia e temperatura observados.

Esse indicador auxilia na análise da eficiência operacional e na identificação de possíveis riscos relacionados ao consumo energético.

## Tecnologias Utilizadas

* Python 3
* Biblioteca datetime

## Como Executar

1. Faça o download do arquivo `main.py`.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python main.py
```

## Cenários Disponíveis

O sistema possui três cenários de simulação:

### Cenário 1 – Operação Normal

Todos os sistemas operam dentro dos parâmetros esperados.

### Cenário 2 – Temperatura Elevada e Energia Reduzida

O sistema identifica condições críticas relacionadas à temperatura e ao fornecimento de energia.

### Cenário 3 – Falha de Comunicação

O sistema detecta falhas de comunicação e executa procedimentos automáticos de contingência.

Para alterar o cenário, basta modificar o valor da variável:

```python
cenario = 1
```

ou

```python
cenario = 2
```

ou

```python
cenario = 3
```

## Resultados Esperados

Durante a execução, o sistema apresenta:

* Dados da missão.
* Índice de sustentabilidade.
* Alertas operacionais.
* Ações automáticas recomendadas.
* Status geral da missão.
* Resumo operacional.

## Integrantes

André Felix – 571691

Gabriel Silveira – 568910

## Considerações Finais

O projeto demonstra a aplicação de conceitos de monitoramento inteligente em um contexto de missão espacial experimental. A utilização de alertas automáticos e respostas básicas permite transformar informações operacionais em suporte à tomada de decisão, contribuindo para a segurança e eficiência da missão.
