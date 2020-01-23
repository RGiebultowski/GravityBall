import pygame



class Bird(object):
    #Setting the main physics of the Bird
    def __init__(self, game):
        self.game = game
        self.x = 50
        self.y = 300
        self.gravity = 1  #must be an integer
        self.velocity = 0
        self.up = 2  #must be an integer

    def tick(self):
        #Create the graviti for ball to fall down
        self.velocity += self.gravity
        self.y += self.velocity

        #Stopping the bird at the bottom of the screen and the top of it
        if self.y > self.game.height:
            self.y = self.game.height
            self.velocity = 0
        elif self.y < 0:  #can't be an self.game.height beacuse its going to be allways on top.
            self.y = 0
            self.velocity = 0

        #Flying function
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.velocity -= self.up

    #Draw of the Bird and setting the main position of bird
    def draw(self):
        color = (255,255,255)
        #positions must be an integer
        pygame.draw.circle(self.game.screen, color, (self.x, self.y),20)
