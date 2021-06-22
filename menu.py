import pygame
import pygame_menu

import main

pygame.init()
surface = pygame.display.set_mode((800, 500))

penalty_for_question = 10


def set_difficulty(value, difficulty):
    global penalty_for_question
    penalty_for_question = difficulty


def start_the_game():
    main.initial_game(penalty_for_question)


menu = pygame_menu.Menu('Bem Vindo ao Jogo de Palavras', width=600, height=400,
                        theme=pygame_menu.themes.THEME_BLUE
                        )
menu.add.text_input('Seu Nome :', default='Vinicius')
menu.add.selector('Dificuldade :', [('Fácil', 10), ('Difícil', 30)], onchange=set_difficulty)
menu.add.button('Jogar', start_the_game)
menu.add.button('Sair', pygame_menu.events.EXIT)

menu.mainloop(surface)
