import pygame, os, sys
from pygame.locals import *

from players import Ghosts, PacMan

"""Global constants"""
"""Creating Basic colors"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    """This class performs all the main initializations and manages everything that is to take place in the main game loop"""
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """

    """Class attributes- In this case, all the data we need to run our game"""
    
    def __init__(self):
        self.game_over = False
        self.score = 0

        """Create all the sprite lists"""
        """This is a list of all the token sprites"""
        self.token_list = pygame.sprite.Group()
        """This is a list of all the ghost sprites"""
        self.ghost_list = pygame.sprite.Group()
        """This is a list of all the sprites created in the entire game"""
        self.all_sprites_list = pygame.sprite.Group()

        """Create all the required sprites"""
        """Ghost Sprites"""
        self.ghosts = {"red":None, "blue":None, "white":None, "orange":None}
        x = 0
        for color in self.ghosts.keys():
            """Creating the Ghost Sprite"""
            self.ghosts[color] = Ghosts(color + ".png")
            """Assigning starting positions to the Ghost"""
            self.ghosts[color].rect.x = 300 + x
            self.ghosts[color].rect.y = 350
            """Adding Ghost to the required sprite groups"""
            self.ghost_list.add(self.ghosts[color])
            self.all_sprites_list.add(self.ghosts[color])
            x+=40
        """PacMan Sprite"""
        self.pacman = PacMan("pacman.png")
        """Assigning start position to PacMan"""
        self.pacman.rect.x = 390
        self.pacman.rect.y = 475
        self.all_sprites_list.add(self.pacman)    

    def manageEvents(self):
        """Checking all the events occured in this frame"""
        for event in pygame.event.get():
            """Checking for game quit event"""
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.pacman.direction = 'down'
                elif event.key == pygame.K_RIGHT:
                    self.pacman.direction = 'right'
                elif event.key == pygame.K_UP:
                    self.pacman.direction = 'up'
                elif event.key == pygame.K_LEFT:
                    self.pacman.direction = 'left'

    def runLogic(self):
        "Processes and updates objects based on events"""
        if not self.game_over:
            self.all_sprites_list.update()
        
    def displayFrame(self, DISPSURFACE):
        "Renders the changes to the main display"""
        """Clear the screen"""
        DISPSURFACE.fill(WHITE)

        """if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])"""

        if not self.game_over:
            """Drawing all the sprites to the display surface"""
            self.all_sprites_list.draw(DISPSURFACE)

        """Updating the display with all the drawn changes"""
        pygame.display.update()


def main():
    """Performing the main initializations"""
    pygame.init()
    """Creating the Main display surface"""
    DISPSURFACE = pygame.display.set_mode((780, 700),0, 32)
    pygame.display.set_caption('PacMan')
  
    """Creating a Game Instance"""
    game = Game()
    """Creating the FPS Clock"""
    fps_clock = pygame.time.Clock()

    while True:
        """calling event manager"""
        game.manageEvents()
        """calling processing function to process the events and update objects"""
        game.runLogic()
        """Calling render function to render all the drawn changes to the display"""
        game.displayFrame(DISPSURFACE)

        """Limit to 60 frames per second"""
        fps_clock.tick(60)

if __name__ == '__main__':
    main()
