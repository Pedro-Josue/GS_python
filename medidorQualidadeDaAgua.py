#O programa consiste em um medidor de qualidade da água, ele funciona para medir a qualidade da água em ambientes marinhos utilizando os parametros do Índice de Qualidade Ambiental Marinha (IQAM) para o ambiente marinho.
def media(od, ph, sal, temp, turb, nutri, metais, fito, especies):
    #essa função usa uma média ponderada para calcular a qualidade da água cada elemento tem 0.1 de peso, só o od que n tem 0.2
    total = (od * 0.2) + (ph * 0.1) + (sal * 0.1) + (temp * 0.1) + (turb * 0.1) + (nutri * 0.1) + (metais * 0.1) + (fito * 0.1) + (especies * 0.1)
    return total


print('Bem-vindo ao medidor de IQAM!')
n = 0
#loop pra fazer o menu, se o usuario digitar 3, o programa para, declarei n = 0 no início pro programa rodar
while n != 3:
    print('='*30)
    print('1 - Para medir a qualidade da água\n2 - Para saber mais sobre o IQAM\n3 - Para sair do programa')
    print('='*30)
    n = int(input('Digite a opção desejada: '))
    #caso a opção do usuario seja 1 ele faz uma série de perguntas e depois chama a função média para calcular a média ponderada
    if n == 1:
        print('Todos os parametros devem ser informado entre 0 e 1.')
        od = float(input('Informe o oxigênio dissolvido: '))
        ph = float(input('Informe o ph: '))
        salinidade = float(input('Informe a salinidade: '))
        temp = float(input('Informe a temperatura da água: '))
        turbidez = float(input('Informe a turbidez da água: '))
        nutrientes = float(input('Informe os nutrientes: '))
        metais = float(input('Informe os metais pesados: '))
        fito = float(input('Informe a quantidade de biomassa de fitoplacton: '))
        especies = float(input('Informe a quantidade de especies indicadoras: '))
        resultado = media(od, ph, salinidade, temp, turbidez, nutrientes, metais, fito, especies)
        if  resultado < 0.2:
            print(f'O resultado do calculo IQAM foi igual a {resultado:.1f}, oque representa uma qualidade da água muito ruim, esse lugar deve ser tratado por autoridades competentes imediatamente.')
        elif resultado == 0.2 or resultado < 0.4:
            print(f'O resultado do calculo IQAM foi igual a {resultado:.1f}, oque representa uma qualidade da água ruim, esse lugar deve ser tratado por autoridades competentes imediatamente.')
        elif resultado == 0.4 or resultado < 0.6:
            print(f'O resultado do calculo IQAM foi igual a {resultado:.1f}, oque representa uma qualidade da água regular, não representa grandes riscos a fauna e flora do ambiente mas deve entrar em observação.')
        elif resultado == 0.6 or resultado < 0.8:
            print(f'O resultado do calculo IQAM foi igual a {resultado:.1f}, oque representa uma qualidade da água boa.')
        elif resultado >= 0.8:
            print(f'O resultado do calculo IQAM foi igual a {resultado:.1f}, oque representa uma qualidade da água muito boa.')
    #A opção 2 mostra um texto explicativo com cada parametro do calculo
    elif n == 2:
        print('Informações sobre os parametros utilizados no calculo:\nO calculo consiste em uma média ponderada entre 9 paramêtros, eles são:\n\nOxigênio Dissolvido: O oxigênio dissolvido é a quantidade de oxigênio disponível na água para respiração dos organismos aquáticos. É um indicador crucial da saúde do ecossistema aquático.\n\npH: O pH afeta os processos biológicos e químicos na água. Valores extremos podem ser prejudiciais para a vida aquática e indicar poluição\n\nSalinidade: É vital para a osmorregulação dos organismos marinhos.\n\nTemperatura da Água: A temperatura da água influencia o metabolismo dos organismos aquáticos e a solubilidade dos gases.\n\nTurbidez: Alta turbidez pode reduzir a penetração da luz, afetando a fotossíntese das plantas aquáticas e a visibilidade dos organismos.\n\nNutrientes (Nitratos, Fosfatos): Nutrientes como nitratos e fosfatos são essenciais para o crescimento das plantas aquáticas.\n\nMetais Pesados (Mercúrio, Chumbo, Cádmio): A presença de metais pesados pode ser indicativa de poluição industrial e representa um risco significativo para a saúde dos ecossistemas.\n\nBiomassa do Fitoplâncton e Zooplâncton: ndicadores da produtividade primária e secundária do ecossistema. Alterações na biomassa podem refletir mudanças na qualidade da água e na saúde do ecossistema​.\n\nPresença de Espécies Indicadoras: Espécies indicadoras são aquelas sensíveis ou tolerantes à poluição e mudanças ambientais.​')
    #opção 3 sai do programa
    elif n == 3:
        print('Saindo...')
    #Condicional para caso o usuário digite um número que não está no menu
    elif n > 3:
        print('Número digitado inválido, por favor, digite um dos números do menu.')

print('Obrigado por utilizar o programa!')