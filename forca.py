# imports

import random
from os import system, name

# Função para limpara tela a cada execução 

def linpar_tela():

    # Windows
    if name == 'nt':
        _ = system('cls')
    
    # Mec/Linux
    else:
        _ = system('clear')

# Função que desenha a forca na tela
def forc(chances):
    # Lista de estagios da forca
    stages = [ # estagio 6(Final)
            '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
            ''',
            # Estagio 5
            '''
                 --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
            ''',
            # Estagio 4
               '''
                  --------
                |      |
                |      O
                |     \\|/
                |      |
                |     
                -
            ''',
            # Estagio 3
               '''
                  --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
            ''',
            # Estagio 2
               '''
                 --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
            ''',
            # Estagio 1
               '''
                ------
                |    |
                |    O
                |  
                |    
                |   
                |
                -
            ''',
            # Estagio 0
               '''
                ------
                |    |
                |    
                |  
                |    
                |   
                |
                -
            '''

    ]
    return stages[chances]

def game():

    linpar_tela()

    print("\nBem vindo (a) jogo da forca")
    print("Adivinhe a palavra abaixo\n")

    # lista de palavras do jogo
    palavras = ["Abacate", "Abacaxi", "Acerola", "Açaí", "Ameixa", "Amora", "Araçá", "Banana",
    "Bergamota", "Buriti", "Cacau", "Caju", "Cambuci", "Caqui", "Carambola", "Cereja",
    "Coco", "Cupuaçu", "Damasco", "Figo", "Framboesa", "Goiaba", "Graviola", "Groselha",
    "Jabuticaba", "Jaca", "Jambo", "Jatobá", "Jenipapo", "Kiwi", "Laranja", "Limão",
    "Lichia", "Maçã", "Mamão", "Manga", "Mangaba", "Maracujá", "Melancia", "Melão",
    "Mirtilo", "Morango", "Nectarina", "Noni", "Pequi", "Pera", "Pêssego", "Pitanga",
    "Pitaia", "Romã", "Sapoti", "Siriguela", "Tamarindo", "Tangerina", "Tomate",
    "Uva", "Umbu", "Veludo", "Zabumba", "Zimbro"]

    # Escolhe uma palavra da lista de forma aleatoria
    palavra = random.choice(palavras).lower()

    # List comprehension 
    letras_descobertas = ['_' for letras in palavra]

    # numero de chances
    chances = 6

    # Lista para letras erradas 
    letras_erradas = []

    # Loop em quanto o numero de chances for maior que zero
    while chances > 0:
        print(forc(chances))
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #tentativas 
        tentativa = input("\nDigite uma letra: ").lower()

        #condição 
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            # Decremento
            chances -= 1
            letras_erradas.append(tentativa)

        # Condição final
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
        
    # Condição final "DERROTA"
    if "_" in letras_descobertas:
        print("\nVoce perdeu, a palavra era: ", palavra)

# Bloco main 
if __name__ == "__main__":
    game()
    print("\nFIM\n")