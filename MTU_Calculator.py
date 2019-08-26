import os

mtu_base = 1000
mtu = mtu_base
mtu_anterior = 0
escala = 100
cout = 1
url = 'www.google.com.br'

def mtu_test():
    global mtu
    global url
    # Get the results of the command ping to know what is happening with MTU
    result = list(os.popen(f'ping {url} -f -l {mtu}'))
    #for i in result:
    #    print(i)
    result = result[8].split(',')
    enviados, recebidos, perdidos = result[0], result[1], result[2]
    avalia_mtu(get_numResults(enviados), get_numResults(recebidos), get_numResults(perdidos))


def get_numResults(string):
    return int(string[string.find('=')+2])


def avalia_mtu(enviados, recebidos, perdidos):
    global mtu
    global mtu_anterior
    global escala
    global cout
    global mtu_base

    print(f'Teste {cout}\nMTU: {mtu} \n- Foram enviados {enviados} pacotes\n- {recebidos} Recebidos com sucesso\n- {perdidos} Pacotes perdidos\n')
    cout += 1
    if perdidos >= 1:
        mtu_anterior = mtu
        mtu -= escala
        mtu_test()

    else:
        if escala == 1:
            print(f'\nProcesso concluido!!\n'
                  f'Seu MTU exato é: {mtu}')

        else:
            if mtu >= mtu_base:
                mtu_base += 1000
                mtu += mtu
                mtu_test()

            else:
                mtu = mtu_anterior
                escala /= 10
                mtu -= escala
                mtu_test()


def __main__():
    print(5*'=', ' MTU FINDER ', 5*'=')

    op = input('\nTestes serão feitos com URL: www.google.com.br\n'
          'Deseja alterar (S | N): ').upper()

    while 1:
        if op == 'S':
            url = input("Digite URL: ")
            print('Realizando testes com {}\n'.format(url))
            break
        elif op == 'N':
            print('Realizando testes com www.google.com.br\n')
            break
        else:
            print('Opção invalida!')

    mtu_test()

__main__()






