import pygame


PUCK_RADIUS = 10
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
ISLAND_WIDTH, ISLAND_HEIGHT = 400, 400

# Defines a class for the pucks
class Puck(pygame.sprite.Sprite):
    def __init__(self, position, velocity, color):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.color = color
        self.radius = PUCK_RADIUS
        self.onIsland = True
        self.isClicked = False
        self.hasLine = False
        self.velocity = velocity
        self.mass = 10

    def set_pos(self, x, y):
        ''' Set the x,y position of the puck '''
        self.position = (x,y)

    def set_color(self, color):
        ''' Set the color of the puck '''
        self.color = color

    def move(self):
        ''' Calculate the velocities and stuff '''
        # vel = distance*0.1
        # acc = -5
        x,y = self.position
        vx,vy = self.velocity
        x += vx
        y += vy
        self.position = (x,y)

        if x >= (SCREEN_WIDTH / 2) + (ISLAND_WIDTH / 2) - self.radius or x <  (SCREEN_WIDTH / 2) - (ISLAND_WIDTH / 2) + self.radius:
            self.velocity = (-self.velocity[0], self.velocity[1])
        if y >= (SCREEN_HEIGHT / 2) + (ISLAND_HEIGHT / 2) - self.radius or y <  (SCREEN_HEIGHT / 2) - (ISLAND_HEIGHT/ 2) + self.radius:
            self.velocity = (self.velocity[0], -self.velocity[1])

    def click(self):
        ''' User clicked the puck '''
        self.isClicked = not self.isClicked

    def draw(self, surface):
        ''' Draw puck to the surface '''
        if self.isClicked:
            pygame.draw.circle(surface, (0,0,0), (self.position[0], self.position[1]), PUCK_RADIUS)
        else:
            pygame.draw.circle(surface, self.color, (self.position[0], self.position[1]), PUCK_RADIUS)

    def get_pos(self):
        '''Get puck position'''
        return (self.position[0],self.position[1])

    def col_circle(self, circlepos):
        '''Checking for collision with another puck'''
        x1, y1 = self.position
        x2, y2 = circlepos

        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        if distance <= PUCK_RADIUS:
            return True
        return False

    def col(self, pucks):
        '''Checking for collision'''
        return (self, pygame.sprite.spritecollideany(self, pucks, collided = None))