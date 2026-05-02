import random
import pygame
import json

with open("blocks.json") as file:
  blocks = json.load(file)
with open(input("")) as f:
  world = json.load(f)  
with open("player.json) as file:
  playerjson = json.load(file)

class Info:
  @staticmethod
  class random:
    def float(f, t):
      retun f + random.random() * (t - f)

    def int(f, t):
      return int( f + random.random() * (t - f) )

    def bool():
      return True if random.random() > 0.5 else False

  class getBlock:
    @staticmethod
    def fromCoor(x, y):
      for C in world:
        if (C["coor"] == [x, y]):
          return C
      return None

DATA = {
  "blockWidth": 100,
  "blockSubPixels": 5,
  "widthScreen": 600,
  "heightScreen": 400,
}

player = {
  "walkSpeed": 100,
  "jumpHeight: 100,
}

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("2d mc")
pygame.mouse.set_visible(False)
camera = world["player"]["position"]
def getBlockPixels(x, y, subX=0, subY=0):
  return [(x-camera[0])*DATA["blockWidth"]+subX*(DATA["blockWidth"]/DATA["blockSubPixels"])+DATA["widthScreen"]/2, 
          ((-y)-camera[1])*DATA["blockWidth"]+subY*(DATA["blockWidth"]/DATA["blockSubPixels"])+DATA["heightScreen"]/2]

def htr(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c*2 for c in h)
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

class Engine:
  pressed_keys_last = {
    w: 0
  }
  @staticmethod
  def renderWorldBlocks():
    for coor in world["blocks"].keys():
      block = world["blocks"][coor]
      face = blocks[block["block"]]["face"]
      for ifL, faceLine in enumerate(face):
        for ifP, facePiece in enumerate(faceLine):
          i = pygame.time.get_ticks() / facePiece.get("animation", 1000)
          T = htr(facePiece["color"][int(i // 1 % facePiece["color"].__len__())])
          TT = htr(facePiece["color"][int(( i // 1 + 1 ) % facePiece["color"].__len__())])
          color = [ T[K] + (TT[K] - T[K]) * (i % 1) for K in range(3) ]
          pygame.draw.rect(screen, color, tuple(getBlockPixels(block["coor"][0], block["coor"][1], ifP, ifL)+[DATA["blockWidth"]/DATA["blockSubPixels"], DATA["blockWidth"]/DATA["blockSubPixels"]]))
  def renderWorldPlayer():
    face = playerjson["player"]
    for ifL, faceLine in enumerate(face):
        for ifP, facePiece in enumerate(faceLine):
          i = pygame.time.get_ticks() / facePiece.get("animation", 1000)
          T = htr(facePiece["color"][int(i // 1 % facePiece["color"].__len__())])
          TT = htr(facePiece["color"][int(( i // 1 + 1 ) % facePiece["color"].__len__())])
          color = [ T[K] + (TT[K] - T[K]) * (i % 1) for K in range(3) ]
          pygame.draw.rect(screen, color, tuple(getBlockPixels(block["coor"][0], block["coor"][1], ifP, ifL)+[DATA["blockWidth"]/DATA["blockSubPixels"], DATA["blockWidth"]/DATA["blockSubPixels"]]))
  
  @staticmethod
  def controlMove():
    global camera
    camera_last = camera[:]
    if pygame.key.get_pressed()[pygame.K_w] == 1:
      camera[1] -= (pygame.time.get_ticks() - pressed_keys_last["w"]) / 1000 * player["walkSpeed"] / DATA["blockWidth"]
    pressed_keys_last["w"] = pygame.time.get_ticks()

    for l in [[int(camera[0])+k, int(camera[1])+kk] for k, kk in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
      if camera[0]+1 > l[0] and camera[0] < l[0]+1 and camera[1]+1 > l[1] and camera[1] < l[1]+1 and world["blocks"]["".join(l)]:
        camera[:] = camera_last
    
clock = pygame.time.Clock()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  screen.fill((255, 255, 255))
  Engine.renderWorldBlocks()
  Engine.controlMove()
  
  # player cursor
  player_mouseX, player_mouseY = pygame.mouse.get_pos()
  pygame.draw.rect(screen, ( 200, 200, 200 ), tuple(map(lambda x: x - DATA["blockWidth"]/DATA["blockSubPixels"]/6, pygame.mouse.get_pos()))+(DATA["blockWidth"]/DATA["blockSubPixels"]/3,)*2)
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
