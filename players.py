import pygame, os
from pygame.locals import *

class Ghosts(pygame.sprite.Sprite):
    """Create and manage the 4 Ghosts"""
    def __init__(self, name):
        """Constructor for ghosts"""
        """Call the constructor of Sprite class"""
        pygame.sprite.Sprite.__init__(self)
        image_to_load = os.path.join('Data', 'Images', name)
        self.image = pygame.image.load(image_to_load).convert()
        self.rect = self.image.get_rect()

        self.walls = None
    """make 3 update fns (1 named update which then calls the rest so tht v can do self.all_sprites_list.update()
        - 1 for AI i.e. they keep roaming, second to go behind PacMan,
        3rd when Pacdies or they die and hv to go back inside box"""

class PacMan(pygame.sprite.Sprite):
    """Create and manage PacMan"""
    def __init__(self, name):
        """Constructor for PacMan"""
        """Call the constructor of Sprite class"""
        pygame.sprite.Sprite.__init__(self)
        image_to_load = os.path.join('Data', 'Images', name)
        self.image = pygame.image.load(image_to_load).convert()
        self.rect = self.image.get_rect()

        """Current Direction of PacMan based on keyboard input"""
        self.direction = None
        self.walls = None

    def update(self):
        """Update PacMan's location based on Gamer Input"""
        #remember to change pacman's image on each turn direction
        frame = 0
        if self.direction == 'right':
            image_to_load = os.path.join('Data', 'Images', 'pacmanright.png')
            self.image = pygame.image.load(image_to_load).convert()
            self.rect.x += 5
            if self.rect.right >= 780:
                self.rect.right = 780

        elif self.direction == 'left':
            image_to_load = os.path.join('Data', 'Images', 'pacmanleft.png')
            self.image = pygame.image.load(image_to_load).convert()
            self.rect.x -= 5
            if self.rect.left <= 0:
                self.rect.left = 0

        elif self.direction == 'down':
            image_to_load = os.path.join('Data', 'Images', 'pacmandown.png')
            self.image = pygame.image.load(image_to_load).convert()
            self.rect.y += 5
            if self.rect.bottom >= 700:
                self.rect.bottom = 700

        elif self.direction == 'up':
            image_to_load = os.path.join('Data', 'Images', 'pacmanup.png')
            self.image = pygame.image.load(image_to_load).convert()
            self.rect.y -= 5
            if self.rect.top <= 0:
                self.rect.top = 0

        """Did this update cause us to hit a wall"""
        """make a list of all collissions between PacMan and the walls"""
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.direction == 'right':
                self.rect.right = block.rect.left
            elif self.direction == 'left':
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
            # Reset our position based on the top/bottom of the object.
            elif self.direction == 'down':
                self.rect.bottom = block.rect.top
            elif self.direction == 'up':
                self.rect.top = block.rect.bottom

