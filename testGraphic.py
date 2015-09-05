import pygame

def render():

    screen.fill((0, 255, 0))

    pygame.draw.line(screen,(255, 255, 255), (10,600), (300,600), (5))

    pygame.draw.line(screen,(255, 255, 255), (300,600), (300,350), (5))

    pygame.draw.line(screen,(255,255,255), (300,350), (10,350), (5))

    pygame.draw.line(screen,(255,255,255), (10,350), (10,600), (5))

    pygame.draw.line(screen,(255,255,255), (10,350), (155,300), (5))

    pygame.draw.line(screen,(255,255,255), (155,300), (300,350), (5))

    pygame.draw.circle(screen,(255,255,0), (100,100), 50)

    pygame.draw.rect(screen,(0,0,255), ((305,450), (340,150)))

    x = 325

    while x < 640:
        pygame.draw.line(screen,(0,0,0), (x,450), (x,600), 2)

        x = x + 20

screen = pygame.display.set_mode((640, 640))

loop = True
while loop:
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      loop = False
    elif e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        loop = False

  render()

  pygame.display.flip()
