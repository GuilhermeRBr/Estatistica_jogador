dados = {}
jogadores = []
gols = []
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
        opcao = str(input('Quer continuar? [S/N]: ')).lower()
        if opcao in 'sn':
            break
        print('Digite apenas S ou N.')
    print('-'*35)    
    if opcao == 'n':
        break   
print(f'{'Cod':^5} {'Nome':^10} {'Gols':^15} {'Total':^10}')
for pos, item in enumerate(jogadores):

    print(f'\n{pos:^5}   {jogadores[pos]['nome']:^5}   {jogadores[pos]['gols']}   {jogadores[pos]['total']:^}')

print('-'*35) 
while True: 
    jogador = int(input('Mostrar dados de qual jogador? [999 encerra]: '))
    if jogador == 999:
        print('ENCERRANDO...')
        break
    if jogador >= len(jogadores):
        print('NAO EXISTE ESSE JOGADOR')
    else:
        print(f'Levantamento do jogador: {jogadores[jogador]['nome']}')
        for pos, item in enumerate(jogadores[jogador]['gols']):
            print(f'    No jogo {pos+1} fez {item} gols')
        print('-'*35) 