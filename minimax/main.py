from ui import TicTacToeUI
from game import TicTacToe
from minimax import AI
import pygame, sys


game_ui = TicTacToeUI()
game = TicTacToe('X', 'O')

player_num = game_ui.text_input()


if player_num == 1:
    ai = AI('X')

if game.current_player == 'X' and player_num == 1:
    game_ui.show_text("Ai Thinking...")
else:
    game_ui.draw_grid()

while True:
    if player_num == 1 and game.current_player == 'X':
        row, col = ai.make_move(game.board)
        game.game_move(row, col)
        game_ui.draw_grid()
        game_ui.draw_board(game.board)
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[0]//80, pos[1]//80
                game.game_move(row, col)
                game_ui.draw_board(game.board)
    
    pygame.display.flip()

    if game.is_game_over():
        pygame.time.wait(300)
        if game.is_winner('X'): 
            game_ui.draw_end('X')
        elif game.is_winner('O'): 
            game_ui.draw_end('O')
        else: 
            print("It is a tie!")
            game_ui.draw_end('No One')
        break