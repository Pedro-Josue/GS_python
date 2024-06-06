# Medidor de IQAM (Índice de Qualidade Ambiental Marinha)

## Descrição

O Medidor de IQAM é um programa em Python que calcula e monitora a qualidade da água em ambientes marinhos com base nos parâmetros do Índice de Qualidade Ambiental Marinha (IQAM). Este índice utiliza uma média ponderada de cinco parâmetros principais para avaliar a saúde do ecossistema marinho: turbidez, pH, salinidade, temperatura da água e oxigênio dissolvido.

## Funcionalidades

1. **Medir a Qualidade da Água**: Coleta valores dos cinco parâmetros principais e calcula o IQAM.
2. **Informações sobre o IQAM**: Exibe informações detalhadas sobre cada parâmetro utilizado no cálculo.
3. **Histórico de Medições**: Armazena e exibe o histórico das medições realizadas, permitindo ao usuário acessar detalhes específicos de cada resultado.
4. **Sair do Programa**: Encerra a execução do programa.

## Parâmetros Utilizados no Cálculo

- **Turbidez**: Medida em NTU (Unidades de Turbidez Nefelométricas).
- **pH**: Escala de 1 a 8.2.
- **Salinidade**: Medida em PSU (Practical Salinity Units).
- **Temperatura da Água**: Medida em °C (graus Celsius).
- **Oxigênio Dissolvido**: Medido em mg/L (miligramas por litro).

## Como Usar

1. Execute o programa.
2. Selecione uma das opções do menu:
   - `1` - Para medir a qualidade da água.
   - `2` - Para saber mais sobre o IQAM.
   - `3` - Para acessar o seu histórico.
   - `4` - Para sair do programa.
3. Para medir a qualidade da água, insira os valores solicitados para cada parâmetro.
4. O programa calculará o IQAM e exibirá uma mensagem sobre a qualidade da água.
5. O histórico das medições pode ser acessado e detalhado conforme necessário.

## Estrutura do Código

### Funções

- **`verifica_resultado(r)`**: Verifica a qualidade da água com base no valor do IQAM e retorna uma mensagem apropriada.
- **`media(turb, ph, sal, temp, od)`**: Calcula a média ponderada dos parâmetros e retorna o valor normalizado para a escala de 1 a 5.

### Menu

- **Opção 1**: Coleta os valores dos parâmetros e calcula o IQAM.
- **Opção 2**: Exibe informações detalhadas sobre os parâmetros.
- **Opção 3**: Exibe o histórico das medições realizadas e permite acessar detalhes específicos.
- **Opção 4**: Encerra o programa.

## Exemplo de Uso

```python
# Exemplo de execução do programa
Bem-vindo ao medidor de IQAM!
==============================
1 - Para medir a qualidade da água
2 - Para saber mais sobre o IQAM
3 - Para acessar o seu histórico
4 - Para sair
==============================
Digite a opção desejada: 1
Informe a turbidez da água [entre 1 e 100]: 15
Informe o ph [entre 1 a 8.2]: 7.5
Informe a salinidade [entre 1 a 45 ou mais]: 35
Informe a temperatura da água [entre 1ºC a 35ºC ou mais]: 25
Informe o oxigênio dissolvido: [entre 1 mg/L a 7 mg/L]: 5
O resultado do cálculo IQAM foi igual a 1.9, o que representa uma qualidade da água ruim. Esse lugar deve ser tratado por autoridades competentes imediatamente.
```
## Tecnologias utilizadas
- Python
- IDE utilizada: Visual Studio Code
## Requisitos para construir o projeto
- Computador
- IDE
- Biblioteca Python
## Instruções de Uso
- Baixar ou clonar esse repositório
- Cole em uma IDE
- E rode o programa utilizando uma biblioteca Python
