import sys, pygame
def crash_ball(screen, ball, speed):
    ballrect = ball.get_rect()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
        screen.blit(ball, ballrect)
pygame.init()
size = width, height = 600, 500
speed = [1, 1]
black = 249, 130, 57

screen = pygame.display.set_mode(size)
background = pygame.image.load('2.jpg')
ball = pygame.image.load('1.jpg')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    screen.blit(background, (0, 0))
    crash_ball(screen, ball, speed)
    pygame.display.flip()
