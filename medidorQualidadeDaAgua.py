#O programa consiste em um medidor de qualidade da água, ele funciona para medir a qualidade da água em ambientes marinhos utilizando os parametros do Índice de Qualidade Ambiental Marinha (IQAM) para o ambiente marinho.
def verifica_resultado(r):
    if r < 1.5:
        return f'O resultado do cálculo IQAM foi igual a {r:.1f}, o que representa uma qualidade da água muito ruim. Esse lugar deve ser tratado por autoridades competentes imediatamente.'
    elif r < 2.5:
        return f'O resultado do cálculo IQAM foi igual a {r:.1f}, o que representa uma qualidade da água ruim. Esse lugar deve ser tratado por autoridades competentes imediatamente.'
    elif r < 3.5:
        return f'O resultado do cálculo IQAM foi igual a {r:.1f}, o que representa uma qualidade da água regular. Não representa grandes riscos à fauna e flora do ambiente, mas deve entrar em observação.'
    elif r < 4.5:
        return f'O resultado do cálculo IQAM foi igual a {r:.1f}, o que representa uma qualidade da água boa.'

def media(turb, ph, sal, temp, od):
    # Cálculo da média ponderada
    total = (turb * 0.05) + (ph * 0.1) + (sal * 0.2) + (temp * 0.3) + (od * 0.35)
    # Normalizando o valor para uma escala de 1 a 5
    total_real = total / 5 # Dividido por 5, pois a soma dos pesos é 1
    return total_real

n = 0
historico = []

print('Bem-vindo ao medidor de IQAM!')

#loop pra fazer o menu, se o usuario digitar 3, o programa para, declarei n = 0 no início pro programa rodar
while n != 4:
    print('='*30)
    print('1 - Para medir a qualidade da água\n2 - Para saber mais sobre o IQAM\n3 - Para acessar o seu histórico\n4 - Para sair')
    print('='*30)
    n = int(input('Digite a opção desejada: '))
    #caso a opção do usuario seja 1 ele faz uma série de perguntas e depois chama a função média para calcular a média ponderada
    if n == 1:
        turbidez = float(input('Informe a turbidez da água [entre 1 e 100]: '))
        ph = float(input('Informe o ph [entre 1 a 8.2]: '))
        salinidade = float(input('Informe a salinidade [entre 1 a 45 ou mais]: '))
        temperatura = float(input('Informe a temperatura da água [entre 1ºC a 35ºC ou mais]: '))
        oxigenio = float(input('Informe o oxigênio dissolvido: [entre 1 mg/L a 7 mg/L]: '))
        resultado = media(turbidez, ph, salinidade, temperatura, oxigenio)
        historico.append(resultado)
        print(verifica_resultado(resultado))
    #A opção 2 mostra um texto explicativo com cada parametro do calculo
    elif n == 2:
        print('Informações sobre os parametros utilizados no calculo:\nO calculo consiste em uma média ponderada entre 5 paramêtros, eles são:\n\nOxigênio Dissolvido: O oxigênio dissolvido é a quantidade de oxigênio disponível na água para respiração dos organismos aquáticos. É um indicador crucial da saúde do ecossistema aquático A unidade de \nmedida mais comum para o oxigênio dissolvido é o "mg/L".\n\npH: O pH afeta os processos biológicos e químicos na água. Valores extremos podem ser prejudiciais para a vida aquática e indicar poluição. Ele é medido através da concentração de íons de hidrogênio \n(H+) presentes na solução.\n\nSalinidade: É vital para a osmorregulação dos organismos marinhos. É medida em PSU que é um sistema pratico para medir a salinidade da água.\n\nTemperatura da Água: A temperatura da água influencia o metabolismo dos organismos aquáticos e a solubilidade dos gases.\n\nTurbidez: Alta turbidez pode reduzir a penetração da luz, afetando a fotossíntese das plantas aquáticas e a visibilidade dos organismos.Os níveis de turbidez são medidos em unidades de turbidez \nnefelométricas (NTU)​')
    #opção 3 para acessar o historico do usuario, que consiste em uma lista que dei append la na opção 1, fazemos um loop for que mostra o que mostra o index da variavel de controle 'i' que percorre a lista e o valor dentro dela, depois outro loop for onde a variavel verificador pergunta para o usuario se ele quer ou não acessar mais detalhes sobre aquele determinado resultado, se ele digitar 999 o loop é quebrado e volta para o menu inicial, se ele digitar o codigo que é o index da lista, é printado com a função verifica resultado esse resultado, informando a qualidade da agua, quando o usuario percorrer todos os valores do usuario o loop também termina e volta para o menu inicial.
    elif n == 3:
        for i in historico:
            print(f'Código: {historico.index(i)} Resultado: {i:.1f}')
        for k in historico:
            verificador = int(input('Deseja acessar mais detalhes sobre algum desses resultados?\nSe sim digite o código, se não digite 999: '))
            if verificador != 999:
                print(f'Nesse calculo o resultado obtido foi: {verifica_resultado(historico[verificador])}')
            else:
                break

    #opção 4 sai do programa
    elif n == 4:
        print('Saindo...')
    #Condicional para caso o usuário digite um número que não está no menu
    elif n > 4:
        print('Número digitado inválido, por favor, digite um dos números do menu.')
print('Obrigado por utilizar o programa!')