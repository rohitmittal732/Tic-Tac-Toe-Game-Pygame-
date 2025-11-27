import pygame
import time

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("X/O Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = 200

board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

player = "X"
font = pygame.font.Font(None, 100)
winner_font = pygame.font.Font(None, 60)
run = True
winner = None
game_over = False

def reset_game():
    global board, player, winner, game_over
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    player = "X"
    winner = None
    game_over = False

while run:
    screen.fill(WHITE)

    # grid lines
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 5)

    # draw X and O
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * SIZE + 70, row * SIZE + 50))

    # check winner
    if not winner:
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] != "":
                winner = board[row][0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                winner = board[0][col]

        if board[0][0] == board[1][1] == board[2][2] != "":
            winner = board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            winner = board[0][2]

    # check draw
    if not winner:
        filled = True
        for row in board:
            if "" in row:
                filled = False
        if filled:
            winner = "Draw"

    # show winner or draw
    if winner and not game_over:
        if winner == "Draw":
            msg = winner_font.render("It's a Draw!", True, (255, 0, 0))
        else:
            msg = winner_font.render(winner + " Wins!", True, (255, 0, 0))

        screen.blit(msg, (180, 260))
        pygame.display.update()
        game_over = True
        time.sleep(2)
        reset_game()

    # user click
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // SIZE
            col = mouse_x // SIZE
            if board[row][col] == "":
                board[row][col] = player
                player = "O" if player == "X" else "X"

    pygame.display.update()

pygame.quit()
