from random import randint
from tkinter import N

EASY_LEVEL_TURNS = 15
HARD_LEVEL_TURNS = 10

def resposta(guess, answer, turns):
  
    if guess > answer:
        print("Mais baixo")
        return turns - 1
  
    elif guess < answer:
        print("Mais alto")
        return turns - 1
  
    else:
        print(f"Voce acertou, a resposta era {answer}.")

def dificuldade():
  
    level = input("Escolha a dificuldade easy/hard : ")
  
    if level == "easy":
        return EASY_LEVEL_TURNS
  
    else:
        return HARD_LEVEL_TURNS

def game():
    
    print("Estou pensando em um numero de 1 a 100")
    
    answer = randint(1, 100)

    turns = dificuldade()
  
    guess = 0
    
    while guess != answer:
        print(f"Voce tem {turns} tentativas.")

        guess = int(input("De um palpite: "))

        turns = resposta(guess, answer, turns)
        if turns == 0:
            print("Voce perdeu")
            return
        elif guess != answer:
            print("Tente novamente")

game()
