This is example of block with full tree and thsi sis used as a default for **?** attributes

```

{
  "example": {
    "face": [
      [
        {"color": "#123456, "animation?": 1000}x5
      ]x5
    ],
    "other":{
      "breakTime?": 1000
      "drops?": {
         "beforeCode?": "rarity = random.random()",
         "conditions": [
           {
             "condition": "rarity > 0.5",
             "drops": [
               {
                 item: "example_item"
               }
             ]
           }
         ]
      }
    }
  }
}

```
