# Mission Control AI
## Sistema Inteligente de Monitoramento para Missão Espacial Experimental

### Disciplina
Ciências da Computação

### Professor
Lucas Moreira

---

# 1. Objetivo do Projeto

O projeto **Mission Control AI** tem como objetivo simular um sistema de monitoramento utilizado em missões espaciais, capaz de identificar condições de risco através de sensores e lógica digital.

O sistema monitora continuamente:

- Temperatura interna da cápsula;
- Luminosidade interna;
- Estabilidade da nave;
- Energia produzida pelas placas solares;
- Estado das baterias auxiliares.

Quando uma ou mais condições críticas são detectadas, o sistema gera alertas visuais através de LEDs e aciona um alerta principal utilizando portas lógicas digitais.

---

# 2. Contexto da Missão

A missão simulada representa uma cápsula espacial experimental denominada **Cápsula 02**.

Durante a operação, diversos fatores podem comprometer o sucesso da missão:

- Superaquecimento dos sistemas;
- Falta de iluminação;
- Vibrações excessivas;
- Baixa geração de energia;
- Falha nas baterias auxiliares.

Para evitar danos à nave, o sistema realiza monitoramento contínuo e fornece alertas automáticos.

---

# 3. Variáveis de Entrada

Conforme solicitado no desafio, foram definidas cinco variáveis de entrada.

| Variável | Sensor | Condição Normal |
|----------|-----------|-----------|
| Temp     | Temperatura | Entre 5°C e 30°C |
| Lum      | Luminosidade | Igual ou superior a 35% |
| Est      | Vibração/Estabilidade | Sem vibração excessiva |
| Ener     | Energia | Igual ou superior a 3V |
| Bat      | Baterias | Ativas |

Representação binária:

| Valor | Significado |
|---------|---------|
| 0 | Normal |
| 1 | Alerta/Risco |

---

# 4. Condições Operacionais

O sistema considera como situação normal:

- Temperatura entre 5°C e 30°C;
- Luminosidade acima de 35%;
- Ausência de vibrações excessivas;
- Energia acima de 3V;
- Baterias ativas.

Qualquer condição fora desses limites gera um alerta local.

---

# 5. Componentes Utilizados

## Hardware

- 1 Arduino Uno R3
- 3 Protoboards
- 1 Sensor de temperatura
- 1 Fotorresistor (LDR)
- 1 Sensor de inclinação
- 1 Painel solar
- 1 Interruptor deslizante
- 6 LEDs
- 8 Resistores
- 1 CI AND
- 2 CIs OR
- 1 CI NOT

## Software

- Tinkercad
- Linguagem C++
- Logism

---

# 6. Sensores e Entradas

## Temperatura

Responsável por monitorar a temperatura interna da cápsula.

Faixa considerada segura:

- Temperatura ≥ 5°C
- Temperatura ≤ 30°C

Caso a temperatura fique fora desse intervalo, é gerado um alerta.

---

## Luminosidade

Utiliza um LDR para medir a quantidade de luz recebida pelo painel solar.

Faixa considerada segura:

- Luminosidade ≥ 35%

Valores inferiores indicam baixa incidência solar.

---

## Estabilidade

O sensor de inclinação monitora mudanças bruscas de posição.

Quando ocorrem diversas alterações em curto intervalo de tempo, o sistema interpreta como vibração excessiva.

---

## Energia

O painel solar fornece um valor analógico convertido para tensão.

Faixa considerada segura:

- Energia ≥ 3V

Valores inferiores podem comprometer os sistemas da nave.

---

## Baterias

Um interruptor representa o estado das baterias auxiliares.

Estados possíveis:

- Ativas
- Inativas

---

# 7. Funcionamento do Programa

Durante cada ciclo de execução, o Arduino realiza:

```cpp
ConverterTemp();
ConverterLum();
ConverterInclinacao();
VerificarInclinacao();
VerificarVibracao();
ConverterEnergia();
AtivarBaterias();
MostrarRelatorio();
LigarAlertas();
```

Fluxo de processamento:

1. Leitura dos sensores.
2. Conversão dos valores.
3. Verificação das condições operacionais.
4. Atualização dos LEDs de alerta.
5. Geração de relatório.
6. Envio dos sinais ao circuito lógico.

---

# 8. Funções Implementadas

## ConverterTemp()

Converte a leitura analógica em temperatura e verifica se está dentro da faixa operacional.

## ConverterLum()

Converte a leitura do LDR em porcentagem de luminosidade.

## ConverterInclinacao()

Transforma o valor analógico do sensor de inclinação em estado lógico.

## VerificarInclinacao()

Detecta mudanças de posição e contabiliza eventos de inclinação.

## VerificarVibracao()

Determina se houve vibração excessiva durante um intervalo de tempo.

## ConverterEnergia()

Converte a leitura do painel solar para tensão elétrica.

## AtivarBaterias()

Verifica o estado das baterias auxiliares.

## MostrarRelatorio()

Exibe todos os dados da missão no Monitor Serial.

Exemplo:
```text
===========================================
Relatorio do monitoramento da 'Capsula 02'
===========================================

Temperatura: 24 C
Luminosidade: 78%
Vibracao: NORMAL
Energia: 4.2V
Baterias: Ativas
```

## LigarAlertas()

Controla os LEDs indicadores de falha.

---

# 9. Expressão Lógica do Sistema

As condições de risco utilizadas pelo circuito lógico são:

| Variável | Significado |
|-----------|-----------|
| Temp | Temperatura fora da faixa |
| Lum | Luminosidade insuficiente |
| Est | Perda de estabilidade |
| Ener | Baixa energia |
| Bat | Baterias inativas |

Expressão booleana implementada:

```text
X = ((Temp * Lum) + Est) + (!Lum * Ener) + (Ener * Bat)
```

Onde:

- Sinal " + " representa OR
- Sinal " * " representa AND
- Sinal " ! " representa NOT

---

# 10. Interpretação da Expressão

O alerta principal será ativado quando:

### Situação 1

Ocorrer problema de temperatura e luminosidade ou perda de estabilidade.

```text
(Temp * Lum) + Est
```

### Situação 2

A luminosidade estiver alta e houver baixa energia.

```text
!Lum * Ener
```

### Situação 3

Houver baixa energia e as baterias estiverem inativas.

```text
Ener * Bat
```

---

# 11. Circuito Lógico

O circuito foi desenvolvido utilizando:

- CI OR;
- CI NOT;
- CI AND;
- LEDs indicadores;
- Resistores;
- Protoboards.

A lógica recebe os sinais provenientes do Arduino e realiza a tomada de decisão final.

O LED vermelho representa a saída principal:

```text
X = 1
```

Quando aceso, indica situação crítica na missão.

---

# 12. Indicadores Visuais

| LED | Função |
|------|------|
| Laranja | Temperatura |
| Branco | Luminosidade |
| Verde | Estabilidade |
| Amarelo | Energia |
| Azul | Baterias |
| Vermelho | Alerta Principal |

Funcionamento:

- LED apagado → condição normal.
- LED aceso → condição crítica.

---

# 13. Resultados Obtidos

O sistema foi capaz de:

- Monitorar cinco variáveis críticas da missão;
- Detectar condições de risco em tempo real;
- Acionar alertas visuais individuais;
- Executar tomada de decisão utilizando lógica digital;
- Integrar programação com eletrônica digital;
- Simular um sistema de monitoramento espacial.

---

# 14. Conclusão

O projeto permitiu aplicar conceitos de:

- Pensamento Computacional;
- Programação em Arduino;
- Lógica Booleana;
- Portas Lógicas;
- Automação e Monitoramento.

A integração entre sensores, software e circuitos digitais possibilitou a criação de um sistema capaz de identificar falhas operacionais e emitir alertas automáticos, simulando o funcionamento de um centro de controle de missão espacial.