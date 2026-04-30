import random
import pygame

class Info:
  __init__(self):
    pass

  getRandom(self, f, t):
    return f + random.random() * (t - f)

DATA = {
  "blockWidth": 100,
  "blockSubPixels": 5,
  "widthScreen": 600,
  "heigthScreen": 400
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
  return [(x-camera[0])*DATA["blockWidth"]+subX*(DATA["blockWidth"]/DATA["blockSubPixels"]), 
          (y-camera[1])*DATA["blockWidth"]+subY*(DATA["blockWidth"]/DATA["blockSubPixels"])]

import json
with open("blocks.json") as file:
  blocks = json.parse(file.read())
print(blocks)
