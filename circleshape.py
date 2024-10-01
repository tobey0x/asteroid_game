import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
  def __init__(self, x, y, radius):
    if hasattr(self, "containers"):
      super().__init__(self.containers)
    else:
      super().__init__()
      
    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 0)
    self.radius = radius
  
  def draw(self, screen):
    pass
  
  def update(self, dt):
    pass 

  def collision(self, circle_shape):
    r1 = self.radius
    r2 = circle_shape.radius
    sum_of_r = r1 + r2 
    distance = pygame.math.Vector2.distance_to(self.position, circle_shape.position)
    if distance < sum_of_r:
      return True
    return False