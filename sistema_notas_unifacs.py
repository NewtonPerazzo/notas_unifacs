"""
Código que criei com a intenção de automatizar o cálculo da média das notas da UNIFACS, que houve alteração e
se tornou bastante trabalhoso de se fazer à mão.

Por via de Regra:
N1 = primeira unidade
N2 = segunda unidade
A1 = primeira avaliação da N1
A2 = segunda avaliação da N1
A3 = terceira avaliação da N1
A4 ou APS = primeira avaliação da N2
A5 = segunda avaliação da N2

"""
from time import sleep


def n1():
    """
    Esta função tem como objetivo calcular a média da primeira unidade (N1).

    :return: O cálculo é a SOMA das 3 avaliações dividio por 3;

    """
    a1 = float(input('Informe a nota da A1: '))
    a2 = float(input('Informe a nota da A2: '))
    a3 = float(input('Informe a nota da A3: '))
    nota1 = float((a1 + a2 + a3)/3)
    print(f'Nota da N1: {nota1:.1f}' )
    return nota1


def n2():
    """
    Esta função tem como objetivo calcular a média da segunda unidade (N2).

    :return: O cálculo é a primeira avaliação da N2 (A4 ou APS) MULTIPLICADO por 0.1 e somado com a
    segunda avaliação da N2 (A5) MULTIPLICADO por 0.9.

    """
    a4 = float(input('Informe a nota da A4: '))
    a5 = float(input('Informe a nota da A5: '))
    nota2 = float((a4 * 0.1) + (a5 * 0.9))
    print(f'Nota da N2: {nota2:.1f}')
    return nota2


def media():
    """

    Esta função tem como objetivo calcular a média final da disciplina.

    Para calcular a média final, pegamos a média da primeira unidade e MULTIPLICAMOS por 0.4;
    MULTIPLICAMOS a média da segunda unidade por 0.6;
    SOMAMOS o resultado final das duas operações, resultando em sua média.

    """
    media_final = (n1() * 0.4) + (n2() * 0.6)
    if media_final >= 6.0:
        print(f'Sua média foi {media_final:.1f}. Você foi Aprovado! Parabéns!')
    else:
        print(f'Sua média foi {media_final:.1f}. Você foi Reprovado!')
    return media_final


def falta():
    """
    Esta função tem como objetivo verificar quanto preciso tirar na N2, visto que tenho as notas da N1.

    Veritifico quais as notas da N1, isolo a variável "qt_falta", que representa a N2, atribuo 6 à média (que é
    a nota mínima) e realizo o cálculo utilizando conceitos básicos de matemática.

    """
    qt_falta = (6 - 0.4 * n1()) / 0.6
    print(f"Para ser aprovado, você precisa tirar {qt_falta:.1f} na N2 ")
    return qt_falta


def quanto_preciso():
    """
    Esta função calcula quanto preciso tirar na última avaliação, considerando que tenho as outras 4 notas.
    OBS.: seguindo as regras da UNIFACS, caso o aluno seja reprovado, terá direito de fazer uma sexta avaliação (A6). A
    nota desta A6 substituirá a nota da A5 nos cálculos. Desta forma, posso aproveitar esta função para verificar tanto
    quanto preciso na A5, quanto na A6 para ser aprovado na disciplina.

    Realiza o cálculo para saber a nota mínima necessária para que a média final seja 6;
    Utilizando a fórmula de média media = (n1() * 0.4) + (n2() * 0.6), substituo a variável "média" pelo valor
    mínimo (6), para que só tenhamos como variável a var "A5" e a isolamos, respeitando e aplicando os conceitos de
    matemática básica;
    Ao final, tenho a fórmula  A5 = (6 - ((N1 * 0.4) + (0.06 * A4)))/0.54 e retorno o valor de A5, que é seria o
    valor que preciso tirar na A5.

    """
    A4 = float(input('Informe a nota da APS: '))
    qt_falta = (6 - ((n1() * 0.4) + (0.06 * A4)))/0.54
    print(f'Para ser aprovado, precisa tirar {qt_falta:.1f} na última prova.')


def simular_todas_as_notas():
    """
    Função que simula as notas gerais da disciplina de forma hipotética.

    """
    media()

    op = str(input('Deseja continuar no simulador? [S/N] ')).upper()

    if op == 'S':
        simular_todas_as_notas()
    elif op == 'N':
        menu()
    else:
        print('Por favor, insira apenas S ou N.')


def sair():
    print('Volte sempre!')
    exit()


def menu_sleep():
    """
    Função apenas para interação e para reiniciar o menu.

    """
    sleep(1)
    print('Carregando...')
    sleep(1)
    menu()


def menu():
    """
    Esta função é responsável somente para exibição de menu e que recebe os comandos passados pelo usuário, dependendo
    do que o mesmo deseja fazer.

    Utilizei o dicionário "opcoes" com as chaves para as respectivas opções de escolha do usuário. Para exibir no menu,
    criei um for que percorre as chaves desse dicionário e exibe seus valores, evitando assim a repetição de prints.
    """
    opcoes = {
        1: 'para calcular sua N1;',
        2: 'para calcular sua N2;',
        3: 'para calcular sua média final;',
        4: 'para calcular quanto precisa tirar na N2;',
        5: 'para saber quanto precisa tirar na A5;',
        6: 'para saber quanto precisa tirar na A6;',
        7: 'para simular notas;',
        8: 'para sair.'
    }

    print('\n******************************')
    print('-------------MENU-------------')
    for n in opcoes:
        print('Digite', n, opcoes[n])
    print('******************************\n')

    op = int(input('O que deseja? '))

    if op == 1:
        n1()
        menu_sleep()

    elif op == 2:
        n2()
        menu_sleep()

    elif op == 3:
        media()
        menu_sleep()

    elif op == 4:
        falta()
        menu_sleep()

    elif op == 5:
        quanto_preciso()
        menu_sleep()

    elif op == 6:
        quanto_preciso()
        menu_sleep()

    elif op == 7:
        simular_todas_as_notas()

    elif op == 8:
        sair()

    else:
        print('Por favor, insira um valor válido')
        menu_sleep()

menu()