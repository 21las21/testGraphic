import pygame

def render():

    screen.fill((0, 0, 0))

    pygame.draw.line(screen,(255, 255, 255), (10,10), (630,10))

    pygame.draw.line(screen,(0, 0, 255), (10,10), (10,630))

    pygame.draw.line(screen,(0,255,0), (10,630), (630,630))

    pygame.draw.line(screen,(255,0,0), (630,630), (630,10))

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
