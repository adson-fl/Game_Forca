import random
from os import system, name

# metodo para limpar tela 
def limpa_tela():
    if name == 'nt':
        _= system('cls')
    else:
        _= system('clear')

board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:

    # construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letra_erradas = []
        self.letras_escolhidas = []

    # metodo para adivinha letra 
    def guess (self, letra):
        
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)

        elif letra not in self.palavra and letra not in self.letra_erradas:
            self.letra_erradas.append(letra)

        else:
            return False
        
        return True
    
    # metodo  para verificar de o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letra_erradas) == 6)
    
    # metodo para verificar se o jogador venceu
    def hangman_won(self):
         
        if '_' not in self.hide_palavra():
            return True
        return False
    
    # metodo para não mostra letras no board
    def hide_palavra(self):

        rnt = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rnt += '_'
            else:
                rnt += letra
        return rnt
        
    
    def print_game_status(self):
        print(board[len(self.letra_erradas)])

        print('\nPalavras: ' + self.hide_palavra())
        print('\nLetras erradas: ', ', '.join(self.letra_erradas))
        print('Letras corretas: ', ', '.join(self.letras_escolhidas))
        print()
        


    # metodo para ler uma palavra de forma aleatoria
def rand_palavra():
# doc de palavras para jogo 
    with open("palavras/palavras_200.txt","r") as file:
            palavras = file.read().split(", ")
            palavra = random.choice(palavras).lower()
            return palavra
        
# metodo Main - Execução do Programa 
def main():

    limpa_tela()

    # Crinado um obj que seleciona uma palavra de forma randomica
    game = Hangman(rand_palavra())

    # Enquanto o jogo não tiver termiando print o statis e selecione uma palavra
    while not game.hangman_over():

        # Status do Game
        game.print_game_status()

        # receba input do terminal
        user_input = input('\nDigite uma letra: ').lower() # corrigido

        # verifica se a letra digitada faz parte da palavra
        game.guess(user_input)

    game.print_game_status()

        # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu.')

    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.palavra)
        
    print('\nFoi bom jogar com você! Agora vá estudar\n')

        # Executar programa
if __name__ == "__main__":
        main() 
