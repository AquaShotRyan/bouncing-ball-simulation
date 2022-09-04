import random, pygame,math
#Ball object
class Ball:
    def __init__(self):
        self.x = 350
        self.y = 350
        speed = 0.5
        angle = random.randint(1,360)
        self.speedx = speed * math.cos(angle)
        self.speedy = speed * math.sin(angle)
        self.colour = (random.randint(0,250), random.randint(0,250), random.randint(0,250))

    #updates drawing
    def draw(self,screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), 15)

    #makes ball move
    def move(self):

        #handle movement
        self.x+=self.speedx
        self.y+=self.speedy

        #handle bouncing
        if self.x >= 700 or self.x <= 0:
            self.speedx *= -1
        if self.y >= 700 or self.y <= 0:
            self.speedy *= -1

def main():
    screen = pygame.display.set_mode((700,700))
    exit_flag = False
    ball_amount = 5

    #create multple balls
    balls = []
    for i in range(ball_amount):
        balls.append(Ball())

    #main loop
    while exit_flag == False:
        screen.fill((0,0,0))

        for b in balls:
            b.move()
            b.draw(screen)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit_flag = True

main()

