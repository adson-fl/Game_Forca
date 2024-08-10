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
    palavra = random.choice(palavras)

    # List comprehension 
    letras_descobertas = ['-' for letras in palavra]

    # numero de chances
    chances = 6

    # Lista para letras erradas 
    letras_erradas = []