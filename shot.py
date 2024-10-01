import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)