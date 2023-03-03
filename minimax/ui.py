import pygame

class TicTacToeUI:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 243, 243
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(color=(255, 200, 255))
    
    def show_text(self, text):
        font = pygame.font.Font(None, 36)
        text = font.render(text, True, (0, 0, 0))
        self.screen.fill(color=(255, 200, 255))
        self.screen.blit(text, (40, 100))
        pygame.display.flip()

    def text_input(self):
        font = pygame.font.Font(None, 36)
        self.screen.fill(color=(255, 200, 255))
        text1 = font.render("Press 1 for AI", True, (0, 0, 0))
        text2 = font.render("Press 2 for Co-Op", True, (0, 0, 0))
        self.screen.blit(text1, (0, 80))
        self.screen.blit(text2, (0, 110))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 1
                    elif event.key == pygame.K_2:
                        return 2   
    
    def draw_grid(self):
        self.screen.fill(color=(255, 200, 255))
        for i in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), (i*80, 0), (i*80, 243), 4)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i*80), (243, i*80), 4)
        pygame.display.flip()
    
    def draw_cross(self, x, y):
        x = x//80 * 80
        y = y//80 * 80
        pygame.draw.line(self.screen, (0, 0, 0), (x+10, y+10), (x + 70, y + 70), 4)
        pygame.draw.line(self.screen, (0, 0, 0), (x+10, y + 70), (x + 70, y+10), 4)

    def draw_circle(self, x, y):
        x = x//80 * 80
        y = y//80 * 80
        pygame.draw.circle(self.screen, (0, 0, 0), (x+40, y+40), 35, 4)
    
    def draw_board(self, board):
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    self.draw_cross((row+1)*70, (col+1)*70)
                elif board[row][col] == 'O':
                    self.draw_circle((row+1)*70, (col+1)*70)

    def draw_end(self, winner):
        font = pygame.font.Font(None, 36)
        self.screen.fill(color=(255, 200, 255))
        text = font.render(f"{winner} wins!", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=self.screen.get_width()/2, 
                                centery=self.screen.get_height()/2,)
        self.screen.blit(text, textpos)
        pygame.display.flip()
        pygame.time.wait(3000)
