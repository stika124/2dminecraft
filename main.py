import json
with open("blocks.json") as file:
  blocks = json.parse(file.read())
print(blocks)
