import pygame
from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  running = True

  dt = 0

  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.fill("black")


    pygame.display.flip()

    dt = clock.tick(60) / 1000


if __name__ == "__main__":
  main()
