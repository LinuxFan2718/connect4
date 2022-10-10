import pygame
HEIGHT = 600
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

  def move(self, move_column):
    
    return

  def winner(self):
    horizontals = [row[i:i+4] for row in self.board for i in range(self.width-4)]
    hwins = [subrow[0] and all(subrow[0] == subrow[i] for i in range(1, 4)) for subrow in horizontals]
    if any(hwins):
      return True

    verticals = [row[i] for i in range(self.height) for row in self.board]
    verticalfour = [vertical[i:i+4] for i in range(self.height - 4) for vertical in verticals]
    vwins = [subvert[0] and all(subvert[0] == subvert[i]) for i in range(1, 4) for subvert in verticalfour]
    if any(vwins):
      return True
    
    # down right
    downrights = []
    for i in range(self.height - 4):
      for j in range(self.width - 4):
        downright = [self.board[i][j], self.board[i+1][j+1], self.board[i+2][j+2], self.board[i+3][j+3]]
        downrights.append(downright)
    drwins = [subdr[0] and all(subdr[0] == subdr[i]) for i in range(1, 4) for subdr in downrights]
    if any(drwins):
      return True

    downlefts = []
    for i in range(self.height - 4):
      for j in range(4, self.width):
        downleft = [self.board[i][j], self.board[i+1][j-1], self.board[i+2][j-2], self.board[i+3][j-3]]
        downlefts.append(downleft)
    dlwins = [subdl[0] and all(subdl[0] == subdl[i]) for i in range(1, 4) for subdl in downlefts]
    if any(dlwins):
      return True
    return False

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

if __name__=="__main__":
    main()