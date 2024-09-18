import pygame
from constants import *
from player import Player


def main():
    
    pygame.init()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # print(
        # f"""
        # Starting asteroids!
        # Screen width: {SCREEN_WIDTH}
        # Screen height: {SCREEN_HEIGHT}
        #   """)
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)   
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
