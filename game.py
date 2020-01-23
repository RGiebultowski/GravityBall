import pygame
import sys
from Bird import Bird


class Game(object):
    def __init__(self):
        #config
        self.tps_max = 65.0

        #inicialization
        pygame.init()
        self.height = 720
        self.width = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.tps_clock = pygame.time.Clock()
        self.tps_timer = 0.0

        self.bird = Bird(self)

        # Game loop
        while True:
            # Handle events of the screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            #Ticking
            self.tps_timer += self.tps_clock.tick() / 1000.0
            while self.tps_timer > 1 / self.tps_max:
                self.tick()
                self.tps_timer -= 1 / self.tps_max
            #Render
            self.screen.fill((0,0,0))
            self.draw()
            pygame.display.flip()
    def tick(self):
        self.bird.tick()

    def draw(self):
        self.bird.draw()

if __name__ == "__main__":
    Game()