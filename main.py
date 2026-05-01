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
  "heightScreen": 400,
}

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("2d mc")
pygame.mouse.set_visible(False)
camera = [0, 0]
world = {
  "block": [
    {
      "block": "grass_block",
      "coor": [0, 0]
    }
  ]
}
def getBlockPixels(x, y, subX=0, subY=0):
  return [(x-camera[0])*DATA["blockWidth"]+subX*(DATA["blockWidth"]/DATA["blockSubPixels"])+DATA["widthScreen"]/2, 
          (y-camera[1])*DATA["blockWidth"]+subY*(DATA["blockWidth"]/DATA["blockSubPixels"])+DATA["heightScreen"]/2]

def htr(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c*2 for c in h)
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

with open("blocks.json") as file:
  blocks = json.load(file)

clock = pygame.time.Clock()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  screen.fill((255, 255, 255))

  # world blocks
  for block in world["block"]:
    face = blocks[block["block"]]["face"]
    for ifL, faceLine in enumerate(face):
      for ifP, facePiece in enumerate(faceLine):
        i = pygame.time.get_ticks() / facePiece.get("animation", 1000)
        T = htr(facePiece["color"][int(i // 1 % facePiece["color"].__len__())])
        TT = htr(facePiece["color"][int(( i // 1 + 1 ) % facePiece["color"].__len__())])
        color = [ T[K] + (TT[K] - T[K]) * (i % 1) for K in range(3) ]
        pygame.draw.rect(screen, color, tuple(getBlockPixels(block["coor"][0], block["coor"][1], ifP, ifL)+[DATA["blockWidth"]/DATA["blockSubPixels"], DATA["blockWidth"]/DATA["blockSubPixels"]]))

  # player cursor
  player_mouseX, player_mouseY = pygame.mouse.get_pos()
  pygame.draw.rect(screen, ( 200, 200, 200 ), map(lambda x: x - DATA["blockWidth"]/DATA["blockSubPixels"]/6, pygame.mouse.get_pos())+(DATA["blockWidth"]/DATA["blockSubPixels"]/3)*2)
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
