jogadores = []


def jogador():
    gols = []   
    dados = {}
    try:
        while True:
            dados['nome'] = str(input('Nome do jogador: ')).capitalize()
            partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
            for partida in range(0, partidas):
                gols.append(int(input(f'Quantos gols na partida {partida+1}? ')))
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
    while True: 
        jogador = int(input('Mostrar dados de qual jogador? [999 encerra]: '))
        if jogador == 999:
            print('ENCERRADO...')
            break
        if jogador >= len(jogadores):
            print('NAO EXISTE ESSE JOGADOR')
        else:
            print(f'Levantamento do jogador: {jogadores[jogador]['nome']}')
            for pos, item in enumerate(jogadores[jogador]['gols']):
                print(f'    No jogo {pos+1} fez {item} gols')
            print('-'*35) 

