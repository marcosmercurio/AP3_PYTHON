import time

import pygame
import math
import words

count = 0
difficult = 10


def initial_game(penalty):
    global difficult, count
    count = 0
    difficult = penalty
    main()


def init():
    # setup display
    pygame.init()
    global WIDTH, HEIGHT, RADIUS, win, GAP, letters, startx, starty
    global LETTER_FONT, A, WORD_FONT, TITLE_FONT, guessed, WHITE, BLUE, BLACK
    global word, typeWord, finalized, points

    WIDTH, HEIGHT = 800, 500
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jogo das Palavras!")

    # button variables
    RADIUS = 20
    GAP = 15
    letters = []

    startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
    starty = 400
    A = 65

    # fonts
    LETTER_FONT = pygame.font.SysFont('comicsans', 40)
    WORD_FONT = pygame.font.SysFont('comicsans', 60)
    TITLE_FONT = pygame.font.SysFont('comicsans', 70)

    guessed = []

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (131, 196, 254)

    points = 200

    word = ""
    typeWord = ""


def startLetters():
    for i in range(26):
        x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])


def defineSortedWord():
    global sortedWord, word, typeWord
    sortedWord = words.sortWords()
    word = sortedWord[0]
    typeWord = sortedWord[1]


def draw():
    win.fill(WHITE)
    # draw title
    text = TITLE_FONT.render("JOGO DAS PALAVRAS", 1, BLACK)
    typeWordText = LETTER_FONT.render("TIPO: " + typeWord, 2, BLUE)

    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))
    win.blit(typeWordText, (WIDTH / 2 - typeWordText.get_width() / 2, 80))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    pointsText = TITLE_FONT.render(str(points), 2, BLACK)
    win.blit(pointsText, (80, 200))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() /
                    2, HEIGHT / 2 - text.get_height() / 2)
             )
    pygame.display.update()
    pygame.time.delay(100)


def main():
    global count, guessed, points
    if count == 0:
        init()
        count += 1

    startLetters()
    defineSortedWord()

    draw()

    fps = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.display.update()
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                points -= difficult
                                break
        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("Você Ganhou!")
            guessed = []
            points = 200
            main()
            break

        if points <= 150:
            display_message("Você Perdeu!")
            guessed = []
            points = 200
            main()
            break
