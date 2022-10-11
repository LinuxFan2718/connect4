import pygame
import random
HEIGHT = 400
WIDTH = int(HEIGHT * 4/3)
YELLOW = (0xff, 0xff, 0x00)
RED = (0xff, 0x00, 0x00)
BLACK = (0x00, 0x00, 0x00)
BLUE = (0x00, 0x00, 0xff)
PIECESIZE = 50
PIECECOLORS = {
  None: 'black',
  0: 'red',
  1: 'yellow'
}
PLAYER1 = 0
PLAYER2 = 1

class ConnectFour():
  def __init__(self) -> None:
    self.width = 7
    self.height = 6
    self.board = [[None]*self.width for _ in range(self.height)]
    self.turn = PLAYER1
    self.gameover = False

  def print_ascii_board(self):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board]))
    print('-' * 30)
    print()

  def winner(self):
    horizontals = [row[i:i+4] for row in self.board for i in range(self.width-3)]
    if self.check_fours(horizontals):
      print("horizontal win")
      return True

    verticals = [[self.board[x][i] for x in range(self.height)] for i in range(self.width)]
    verticalfour = [vertical[i:i+4] for i in range(self.height - 3) for vertical in verticals]
    if self.check_fours(verticalfour):
      print("vertical win")
      return True
    
    # down right
    downrights = []
    for i in range(self.height - 3):
      for j in range(self.width - 3):
        downright = [self.board[i][j], self.board[i+1][j+1], self.board[i+2][j+2], self.board[i+3][j+3]]
        downrights.append(downright)
    if self.check_fours(downrights):
      print("down right win")
      return True

    downlefts = []
    for i in range(self.height - 3):
      for j in range(3, self.width):
        downleft = [self.board[i][j], self.board[i+1][j-1], self.board[i+2][j-2], self.board[i+3][j-3]]
        downlefts.append(downleft)
    if self.check_fours(downlefts):
      print("down left win")
      return True
    return False

  def draw(self) -> bool:
    for row in self.board:
      if None in row:
        return False
    return True
  
  def move(self, move_column) -> bool:
    current_column = [self.board[x][move_column] for x in range(self.height)]
    if current_column[0] is not None:
      return False
    i = 0
    while i < len(current_column) and current_column[i] is None:
      i += 1
    self.board[i-1][move_column] = self.turn
    if self.winner():
      win_message = PIECECOLORS[self.turn]
      self.print_ascii_board()
      print(f"{win_message} pieces won. Last move: {move_column}.")
      self.gameover = True
    if self.draw():
      self.print_ascii_board()
      print(f"Draw. Last move: {move_column}.")
      self.gameover = True
    
    self.turn = PLAYER2 if self.turn == PLAYER1 else PLAYER1
    return True
  
  def check_fours(self, lists) -> bool:
    for sublist in lists:
      if sublist[0] is not None and all([sublist[0] == sublist[1], sublist[0] == sublist[2], sublist[0] == sublist[3]]):
        return True

def main():
    connectfour = ConnectFour()
    pygame.init()
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    black_square = pygame.image.load("black50x50.png")
    red_square = pygame.image.load("red50x50.png")
    yellow_square = pygame.image.load("yellow50x50.png")
    pygame.display.set_caption("Connect Four")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BLUE)

    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        else:
          if connectfour.gameover:
            print("game over!")
            running = False
          else:
            if random.randrange(10) < 8:
              moved = False
              while not moved:
                move_idea = random.randrange(7)
                moved = connectfour.move(move_idea)
          screen.fill(BLUE)
          x = 0
          y = 0
          board = connectfour.board
          for row in board:
            x = 0
            y += PIECESIZE
            for square in row:
              x += PIECESIZE
              color = PIECECOLORS[square]
              if color == 'black':
                screen.blit(black_square, (x, y))
              elif color == 'red':
                screen.blit(red_square, (x, y))
              elif color == 'yellow':
                screen.blit(yellow_square, (x, y))
          pygame.display.flip()
    waitingToExit = True
    while waitingToExit:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          waitingToExit = False


if __name__=="__main__":
    main()