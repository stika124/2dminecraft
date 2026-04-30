import random
import pygame
import json

class Info:
  def __init__(self):
    pass

  def getRandom(self, f, t):
    return f + random.random() * (t - f)

DATA = {
  "blockWidth": 100,
  "blockSubPixels": 5,
  "widthScreen": 600,
  "heightScreen": 400
}

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("2d mc")
camera = [0, 0]
world = [
  {
    "block": "grass_block",
    "coor": [0, 0]
  }
]
def getBlockPixels(x, y, subX=0, subY=0):
  return [(x-camera[0])*DATA["blockWidth"]+subX*(DATA["blockWidth"]/DATA["blockSubPixels"])+DATA["widthScreen"]/2, 
          (y-camera[1])*DATA["blockWidth"]+subY*(DATA["blockWidth"]/DATA["blockSubPixels"])+DATA["heightScreen"]/2]


with open("blocks.json") as file:
  blocks = json.load(file)

clock = pygame.time.Clock()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((255, 255, 255))
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
