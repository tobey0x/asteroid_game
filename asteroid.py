import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

    
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    random_angle = random.uniform(20, 50)
    
    vel1 = self.velocity.rotate(random_angle)
    vel2 = self.velocity.rotate(-random_angle)
    
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    
    roid_1 = Asteroid(self.position.x, self.position.y, new_radius)
    roid_2 = Asteroid(self.position.x, self.position.y, new_radius)
    roid_1.velocity = vel1 * 1.2
    roid_2.velocity = vel2
    self.kill()