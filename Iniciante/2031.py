N = int(input(''))

for i in range(0,N):
  player1 = str(input(''))
  player2 = str(input(''))


  if player1.upper() == 'ATAQUE' and player2.upper() == 'PEDRA':
    print('Jogador 1 venceu')
  if player2.upper() == 'ATAQUE' and player1.upper() == 'PEDRA':
    print('Jogador 2 venceu')
  #ataque vs. Pedra: Ataque Aéreo vence
  
  if player1.upper() == 'PEDRA' and player2.upper() == 'PAPEL':
    print('Jogador 1 venceu')
  if player2.upper() == 'PEDRA' and player1.upper() == 'PAPEL':
    print('Jogador 2 venceu')
  #Pedra vs. Papel: Pedra ganha
  
  if player1.upper() == 'PAPEL' and player2.upper() == 'ATAQUE':
    print('Jogador 2 venceu')
  if player2.upper() == 'PAPEL' and player1.upper() == 'ATAQUE':
    print('Jogador 1 venceu')
  #Papel vs. Ataque Aéreo: Ataque Aéreo ganha
  
  if player1.upper() == 'PAPEL' and player2.upper() == 'PAPEL':
    print('Ambos venceram')
  #Papel vs. Papel: ambos os jogadores ganha
  
  if player1.upper() == 'PEDRA' and player2.upper() == 'PEDRA':
    print('Sem ganhador')
  #Pedra vs. Pedra: não há ganhador
  
  if player1.upper() == 'ATAQUE' and player2.upper() == 'ATAQUE':
    print('Aniquilacao mutua')
  #Ataque Aéreo vs. Ataque Aéreo Aniquilação Mútua.