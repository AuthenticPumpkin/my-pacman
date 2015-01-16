import pygame, os, sys
from pygame.locals import *

from players import Ghosts, PacMan
from wallsntokens import Walls

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
        """This is a list of all the walls"""
        self.wall_list = pygame.sprite.Group()
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
            #self.all_sprites_list.add(self.ghosts[color])
            x+=40
        """PacMan Sprite"""
        self.pacman = PacMan("pacmanleft.png")
        """Assigning start position to PacMan"""
        self.pacman.rect.x = 390
        self.pacman.rect.y = 475
        self.all_sprites_list.add(self.pacman)
        """Wall Sprites"""
        """List of all the top, left, width and height of all the walls to be created"""
        wall_xywh = [(37, 36, 228, 1), (266, 37, 1, 95), (265, 131, 12, 1), (276, 37, 1, 95), (277, 36, 228, 1), (36, 37, 1, 205), (506, 37, 1, 205), (37, 243, 95, 1), (409, 243, 95, 1), (131, 242, 1, 83), (410, 242, 1, 80), (27, 324, 105, 1), (409, 321, 105, 1), (27, 363, 105, 1), (409, 366, 105, 1), (131, 362, 1, 83), (410, 366, 1, 83), (37, 445, 95, 1), (409, 445, 95, 1), (36, 446, 1, 83), (506, 446, 1, 83), (37, 530, 47, 1), (457, 530, 47, 1), (83, 529, 1, 37), (458, 529, 1, 37), (37, 565, 47, 1), (457, 565, 47, 1), (36, 566, 1, 84), (506, 566, 1, 84), (37, 651, 468, 1)]
        for xywh in wall_xywh:
            wall = Walls(xywh[0], xywh[1], xywh[2], xywh[3])
            self.wall_list.add(wall)
            self.all_sprites_list.add(wall)
        self.pacman.walls = self.wall_list

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
        
    def displayFrame(self, DISPSURFACE, background):
        "Renders the changes to the main display"""
        """Clear the screen and render background"""
        DISPSURFACE.blit(background, (20, 20))

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

    """Creating the background image"""
    background_to_load = os.path.join('Data', 'Images', 'pacback.jpg')
    background = pygame.image.load(background_to_load).convert()
    """Rendering the background to the display"""
    DISPSURFACE.blit(background, (20, 20))

    #test pixels for wall pixels
    pixObj = pygame.PixelArray(DISPSURFACE)
    pixObj[20][20] = WHITE #Start pt. of image
    pixObj[37][37] = WHITE #top left  1
    pixObj[265][37] = WHITE #top center left   2
    pixObj[277][37] = WHITE #top center right   3
    pixObj[265][132] = WHITE #top center down left    27
    pixObj[277][132] = WHITE #top center down right   28
    pixObj[505][37] = WHITE #top right   4
    pixObj[37][242] = WHITE #mid left top    5
    pixObj[505][242] = WHITE #mid right top   6
    pixObj[132][242] = WHITE #mid left top right    11
    pixObj[409][242] = WHITE #mid right top left    12
    pixObj[132][325] = WHITE #mid left mid top right    13
    pixObj[409][325] = WHITE #mid right mid top left    14
    pixObj[37][446] = WHITE #mid left bottom    7
    pixObj[505][446] = WHITE #mid right bottom    8
    pixObj[132][446] = WHITE #mid left bottom right    17
    pixObj[409][446] = WHITE #mid right bottom left     18
    pixObj[132][362] = WHITE #mid left mid bottom right    15
    pixObj[409][362] = WHITE #mid right mid bottom left    16
    pixObj[37][529] = WHITE #down left top   23
    pixObj[505][529] = WHITE #down right top   24
    pixObj[84][529] = WHITE #down left top right    19   
    pixObj[457][529] = WHITE #down right top left   20
    pixObj[37][566] = WHITE #down left bottom   25
    pixObj[505][566] = WHITE #down right bottom   26
    pixObj[84][566] = WHITE #down left bottom right    21
    pixObj[457][566] = WHITE #down right bottom left   22
    pixObj[37][650] = WHITE #bottom left    9
    pixObj[505][650] = WHITE #bottom right   10
    del pixObj
    #

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
        game.displayFrame(DISPSURFACE, background)

        """Limit to 60 frames per second"""
        fps_clock.tick(30)

if __name__ == '__main__':
    main()
