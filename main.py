from utils import jogadores, jogador, mostrar_dados


jogador()

print(f'{'Cod':^5} {'Nome':^10} {'Gols':^15} {'Total':^10}')
for pos in range(len(jogadores)):

    print(f'\n{pos:^5}   {jogadores[pos]['nome']:^5}   {jogadores[pos]['gols']}   {jogadores[pos]['total']:^}')

print('-'*35) 

mostrar_dados()