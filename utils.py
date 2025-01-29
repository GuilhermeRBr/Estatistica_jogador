jogadores = []

def jogador():
    gols = []   
    dados = {}
    try:
        while True:
            #Nome jogador
            while True:
                nome = str(input('Nome do jogador: ')).capitalize()
                if nome.isalpha():
                    dados['nome'] = nome
                    break
                else:
                    print('Digite um nome valido!')

            #Quantidade de partidas
            while True:
                partidas = input(f'Quantas partidas {dados['nome']} jogou? ')
                if partidas.isdigit():
                    partidas = int(partidas)
                    break 
                else:
                    print('Digite apenas números!')

            #Gols por partida
            for partida in range(0, partidas):
                while True:
                    score = input(f'Quantos gols na partida {partida+1}? ')
                    if score.isdigit():
                        gols.append(int(score))
                        break
                    else:
                        print('Digite apenas números!')
            if partidas == 0:
                gols.append(0)       

            dados['gols'] = gols[:]
            dados['total'] = sum(gols)
            jogadores.append(dados.copy())
            gols.clear()


            while True:
                opcao = str(input('Quer continuar? [S/N]: ')).strip().lower()
                if opcao in ['s','n']:
                    break
                elif not opcao:
                    print('Você não digitou nada! Por favor, digite S ou N.')
                else:
                    print('Digite apenas S ou N.')
            print('-'*35)    
            if opcao == 'n':
                break

    except Exception as e:
        print('Algo deu errado!')


def mostrar_dados():
    try:

        #Dados jogadores
        while True: 
            while True:
                jogador = input('Mostrar dados de qual jogador? [999 encerra]: ')
                if jogador.isdigit():
                    jogador = int(jogador)
                    break
                else:
                    print('Digite apenas números!')
            if jogador == 999:
                print('ENCERRADO...')
                break
            elif jogador >= len(jogadores):
                print('NÃO EXISTE ESSE JOGADOR NO NOSSO BANCO DE DADOS!')
            else:
                if jogadores[jogador]['gols'][0] > 0:
                    print(f'Levantamento do jogador: {jogadores[jogador]['nome']}')
                    for pos, item in enumerate(jogadores[jogador]['gols']):
                        print(f'    No jogo {pos+1} fez {item} gols')
                else:
                    print(f'O jogador {jogadores[jogador]['nome']} não fez nenhum gol.')
                print('-'*35) 
    except Exception as e:
        print('Algo deu errado.')

