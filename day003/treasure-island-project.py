#Write your code below this line 👇
print("Welcome to Treasure Island. Your mission is to find the hidden treasure, rumored to be buried deep within this enchanted forest. The path ahead forks into two directions.")
print(" ")

rightOrLeft = input("Turn left and venture deeper into the heart of the forest.\nor\nTurn right, where the path seems to lead downhill.\n")

if rightOrLeft == "left":
  swimOrWait = input("After venturing deeper into the forest, you find yourself on the edge of a serene and crystal-clear river. The path continues alongside the riverbank. You have two options:\nSwim across the river to the other side.\nor\nWait patiently by the riverbank.\n")
  if swimOrWait == "wait":
    door = input("After choosing to wait by the riverbank, you patiently watch the gentle flow of the river. Time passes, and just as you start to wonder if this was the right choice, something remarkable happens. You notice a peculiar pattern in the river's current, forming a message: 'Choose wisely and follow the path ahead.'\n \nFeeling that this is a clue leading you to the treasure, you continue down the path until you reach a chamber with three ornate doors: one red, one blue, and one yellow.\nPick a door.")
    if door == "red":
      print("You decide to open the red door with anticipation. As the door creaks open, you're met with a blast of scorching heat and a fiery abyss. It's a trap! You're consumed by flames, and your adventure comes to an unfortunate end.")
    elif door == "blue":
      print("Curiosity drives you to open the blue door. A freezing wind howls through the doorway, and you find yourself plummeting into a bottomless icy chasm. It's another trap! Your journey ends in a frigid abyss.")
    elif door == "yellow":
      print("With a sense of purpose, you choose the yellow door. It swings open to reveal a glittering chamber filled with piles of gleaming treasure! You've found it, the legendary treasure of Treasure Island. Congratulations! You've won the game and become the ultimate treasure hunter.\n")
      print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    else:
      print("Feeling cautious, you hesitate to open any of the doors, suspecting that they might all be traps. But as you stand there indecisively, the chamber begins to tremble, and the walls start closing in on you. It's a perilous trap triggered by your indecision! You're crushed as the walls converge, and your adventure comes to a tragic end.")
  else:
    print("As you decide to brave the river, you cautiously wade into the water. Suddenly, a school of aggressive trout emerges from the depths, their sharp teeth gleaming. They circle around you, and the situation looks dire.\nGAME OVER")
else:
  print("You choose the right path, which leads downhill through a rocky, treacherous terrain. It's a steep descent, and as you navigate the tricky path, you suddenly lose your footing. With a gasp, you tumble into a concealed pitfall. Darkness surrounds you as you fall, and you land with a thud at the bottom.\nGAME OVER")
