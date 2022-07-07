"""
main.py
"""
import pygame
import os
import random
from modules.vector2D import Vector2
from modules.drawable import Drawable
from modules.player import Player
from modules.cpu import CPU
from modules.button import Button
from modules.statusBar import StatusBar
from modules.textBox import TextBox
from modules.peterBox import PeterBox

SCREEN_SIZE = Vector2(1200, 750)
SCALE = 1
UPSCALED_SCREEN_SIZE = SCREEN_SIZE * SCALE

PETERS = ["peterBalboa.png", "easterPeter.png",
          "indianaGriffin.png", "longJohnPeter.png", "millenialPeter.png",
          "peterBay.png", "peterVice.png", "peterMcdonald.png",
          "peterGriffin.png",
          "peterSoprano.png", "pimpGriffin.png", 
          "peterSnow.png", "heisenpeter.png", "handsomePeter.png",
          "professorGriffin.png", "tweakingPeter.png", "peteFighter.png"]

#menu building functions
def startMenu(buttons, drawSurface):
   buttons.append(Button("Start", (0, 600, 600, 150), "start"))
   buttons.append(Button("Exit", (600, 600, 600, 150), "start"))

   return buttons

def selectMenu(buttons, drawSurface):
   buttons.append(Button("Confirm", (0, 600, 600, 150), "select"))
   buttons.append(Button("Back", (600, 600, 600, 150), "select"))

   return buttons

def mainMenu(buttons, drawSurface):
   buttons.append(Button("Attack", (0, 600, 400, 150), "main"))
   buttons.append(Button("Switch", (400, 600, 400, 150), "main"))
   buttons.append(Button("Exit", (800, 600, 400, 150), "main"))

   return buttons

def battleMenu(buttons, drawSurface, player):
   buttons.append(Button(player._moveset[0],
                         (0, 600, 240, 150),
                         "battle",
                         player.performMove(player._moveset[0])["Type"]))
   buttons.append(Button(player._moveset[1],
                         (240, 600, 240, 150),
                         "battle",
                         player.performMove(player._moveset[1])["Type"]))
   buttons.append(Button(player._moveset[2],
                         (480, 600, 240, 150),
                         "battle",
                         player.performMove(player._moveset[2])["Type"]))
   buttons.append(Button(player._moveset[3],
                         (720, 600, 240, 150),
                         "battle",
                         player.performMove(player._moveset[3])["Type"]))
   buttons.append(Button("Exit", (960, 600, 240, 150), "battle"))

   return buttons

def switchMenu(buttons, drawSurface, party):
   buttons.append(Button(party[0]._name, (0, 600, 300, 150), "switch"))
   buttons.append(Button(party[1]._name, (300, 600, 300, 150), "switch"))
   buttons.append(Button(party[2]._name, (600, 600, 300, 150), "switch"))
   buttons.append(Button("Exit", (900, 600, 300, 150), "switch"))

   return buttons

def selectMove(peter, moveset):
   # Gives each move a likelihood factor for cpu to choose,
   # with damage-dealing moves getting a factor of 3 and other
   # moves getting a factor of 1
   moveOdds = [0, 0, 0, 0]
   
   for i in range(len(moveset)):
      if peter.performMove(moveset[i])["Category"] == "Damage":
         moveOdds[i] = 3
      else:
         moveOdds[i] = 1
   num = random.randint(1, sum(moveOdds))
   total = 0

   for i in range(len(moveset)):
      if num > total and num <= total + moveOdds[i]:
         return i
      else:
         total += moveOdds[i]

#party building functions
def createCpuParty():
   indexes = [-1, -1, -1]
   i = 0
   while i < 3:
      num = random.randint(0, len(PETERS) - 1)
      if num not in indexes:
         indexes[i] = num
         i += 1
   return [CPU(PETERS[indexes[0]], Vector2(725, 250)),
           CPU(PETERS[indexes[1]], Vector2(725, 250)),
           CPU(PETERS[indexes[2]], Vector2(725, 250))]
         
def createPlayerParty(peterBoxes):
   party = []
   for row in peterBoxes:
      for peterBox in row: 
         if peterBox._selected == True:
            party.append(Player(peterBox._imageName, Vector2(300, 250)))
   return party
   
def main():
   
   # initialize the pygame module
   pygame.init()
   pygame.font.init()
   
   # load and set the logo
   pygame.display.set_caption("Pocket Peters")

   # load sounds
   selectSound = pygame.mixer.Sound("sounds\select.wav")
   exitSound = pygame.mixer.Sound("sounds\exit.wav")
   deniedSound = pygame.mixer.Sound("sounds\denied.wav")
   damageSound = pygame.mixer.Sound("sounds\damage.wav")
   posStatSound = pygame.mixer.Sound("sounds\stat_positive.wav")
   negStatSound = pygame.mixer.Sound("sounds\stat_negative.wav")
   pygame.mixer.music.load('sounds\start.mp3')
   pygame.mixer.music.play(-1)

   #load screen and backgrounds
   
   screen = pygame.display.set_mode(list(UPSCALED_SCREEN_SIZE))
   drawSurface = pygame.Surface(list(SCREEN_SIZE))
   
   startBackground = Drawable("startScreen.png", Vector2(0,0))
   selectBackground = Drawable("selectScreen.png", Vector2(0,0))
   battleBackground = Drawable("background.png", Vector2(0,0))

   #initialize status bars with dummy data
   playParty = [Player("professorGriffin.png", Vector2(300, 250)),
                Player("peterBalboa.png", Vector2(300, 250)),
                Player("peterMcdonald.png", Vector2(300, 250))]
   playerSB = StatusBar(playParty[0]._name,
                        playParty[0]._type,
                        playParty[0]._baseStats["HP"],
                        playParty[0]._stats["HP"],
                        (255, 255, 0))
   cpuParty = createCpuParty()
   cpuSB = StatusBar(cpuParty[0]._name,
                     cpuParty[0]._type,
                     cpuParty[0]._baseStats["HP"],
                     cpuParty[0]._stats["HP"],
                     (255, 255, 255))

   #initialize UI variables
   buttons = []
   buttons = startMenu(buttons, drawSurface)
   menu = "start"
   gamePhase = "start"
   turn = ""
   hasGone = [0, 0]
   isOpaque = True
   tBox = TextBox()
   peterBoxes = [[None],
                 [None, None, None],
                 [None, None, None],
                 [None, None, None],
                 [None, None, None],
                 [None, None, None],
                 [None]]
   k = 0
   for i in range(len(peterBoxes)):
      for j in range(len(peterBoxes[i])):
         if i == 0 or i == 6:
            peterBoxes[i][j] = PeterBox((75 + i * 150, 200, 150, 200), PETERS[k])
         else:
            peterBoxes[i][j] = PeterBox((75 + i * 150, j * 200, 150, 200), PETERS[k])
         k += 1
   numSelected = 0
            
   
   #Initialize moveEffect
   moveEffect = {"Category" : "Opening",
                 "Type" : "None",
                 "Target" : "None",
                 "Stat" : "None",
                 "Effect" : 0}
   
   # Make a game clock for nice, smooth animations
   gameClock = pygame.time.Clock()
   
   
   # define a variable to control the main loop
   RUNNING = True
   
   # main loop
   while RUNNING:
      
      # Draw everything
      if gamePhase == "start":
         startBackground.draw(drawSurface)
         for button in buttons:
            button.draw(drawSurface)
            
      elif gamePhase == "select":
         selectBackground.draw(drawSurface)
         for row in peterBoxes:
            for peterBox in row: 
               peterBox.draw(drawSurface)
         for button in buttons:
            button.draw(drawSurface)
            
      elif gamePhase == "battle":
         battleBackground.draw(drawSurface)
         playParty[0].draw(drawSurface)
         playerSB.draw(drawSurface, "left")
         cpuParty[0].draw(drawSurface)
         cpuSB.draw(drawSurface, "right")
         for button in buttons:
            button.draw(drawSurface)
         tBox.draw(drawSurface, isOpaque)

      
      pygame.transform.scale(drawSurface, list(UPSCALED_SCREEN_SIZE), screen)
      
      
      # Flip the display to the monitor
      pygame.display.flip()
      
      # event handling, gets all event from the eventqueue
      for event in pygame.event.get():
         # only do something if the event is of type QUIT or ESCAPE is pressed
         if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # change the value to False, to exit the main loop
            RUNNING = False
         if event.type == pygame.MOUSEBUTTONDOWN:

            if gamePhase == "start":
               for button in buttons:
                  
                  if button._buttonName == "Start":
                     l_coords = (button._coords[0], button._coords[1])
                     r_coords = (l_coords[0] + 600, l_coords[1] + 150)
                     if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                        event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:
                        
                        gamePhase = "select"
                        menu = "select"
                        pygame.mixer.Sound.play(selectSound)
                     
                  elif button._buttonName == "Exit":
                     l_coords = (button._coords[0], button._coords[1])
                     r_coords = (l_coords[0] + 600, l_coords[1] + 150)
                     if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                        event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:
                        
                        pygame.mixer.Sound.play(exitSound)
                        pygame.quit()
                        
            elif gamePhase == "select":
               for row in peterBoxes:
                  for peterBox in row:
                     l_coords = (peterBox._coords[0], peterBox._coords[1])
                     r_coords = (l_coords[0] + 150, l_coords[1] + 200)
                     if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                        event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:

                        
                        if peterBox._selected == True:
                           numSelected -= 1
                           peterBox._selected = False
                           pygame.mixer.Sound.play(selectSound)
                        elif peterBox._selected == False and numSelected < 3:
                           numSelected += 1
                           peterBox._selected = True
                           pygame.mixer.Sound.play(selectSound)
                        else:
                           pygame.mixer.Sound.play(deniedSound)
                        
                              
                     
               for button in buttons:
                  
                  if button._buttonName == "Confirm":
                     l_coords = (button._coords[0], button._coords[1])
                     r_coords = (l_coords[0] + 600, l_coords[1] + 150)
                     if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                        event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:
                        if numSelected != 3:
                           pygame.mixer.Sound.play(deniedSound)
                        else:
                           gamePhase = "battle"
                           menu = "main"
                           isOpaque = True
                           hasGone = [0, 0]

                           playParty = createPlayerParty(peterBoxes)
                           playerSB = StatusBar(playParty[0]._name,
                                                playParty[0]._type,
                                                playParty[0]._baseStats["HP"],
                                                playParty[0]._stats["HP"],
                                                (255, 255, 0))
                           cpuParty = createCpuParty()
                           cpuSB = StatusBar(cpuParty[0]._name,
                                             cpuParty[0]._type,
                                             cpuParty[0]._baseStats["HP"],
                                             cpuParty[0]._stats["HP"],
                                             (255, 255, 255))
                           
                           if cpuParty[0]._stats["Speed"] > playParty[0]._stats["Speed"]:
                              effect = str(cpuParty[0]._name) + " attacks first!"
                              turn = "cpu"
                              tBox.update("effect", effect)
                           else:
                              effect = str(playParty[0]._name) + " attacks first!"
                              turn = "player"
                              tBox.update("effect", effect)
                           pygame.mixer.music.load('sounds\music.mp3')
                           pygame.mixer.music.play(-1)
                           pygame.mixer.Sound.play(selectSound)
                     
                  elif button._buttonName == "Back":
                     l_coords = (button._coords[0], button._coords[1])
                     r_coords = (l_coords[0] + 600, l_coords[1] + 150)
                     if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                        event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:
                        
                        pygame.mixer.Sound.play(exitSound)
                        menu = "start"
                        gamePhase = "start"

         
            elif gamePhase == "battle":
                  
               #Checks to see if the text box is opaque(present)
               if isOpaque:
                  l_coords = (0, 600)
                  r_coords = (l_coords[0] + 1200, l_coords[1] + 150)
                  if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                     event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:

                     # display effect of player move   
                     if tBox._state == "action" and turn == "player":

                        #update stats
                        if moveEffect["Target"] == "Self":
                           playParty[0].update(moveEffect)
                        else:
                           cpuParty[0].update(moveEffect, playParty[0]._stats, playParty[0]._type)

                        #display sound
                        if moveEffect["Category"] == "Damage":
                           pygame.mixer.Sound.play(damageSound)
                        elif moveEffect["Category"] == "Stat" and moveEffect["Target"] == "Self":
                           pygame.mixer.Sound.play(posStatSound)
                        elif moveEffect["Category"] == "Stat" and moveEffect["Target"] == "Other":
                           pygame.mixer.Sound.play(negStatSound)
                        else:
                           pygame.mixer.Sound.play(selectSound)
                           
                        if cpuParty[0].isDead():
                           tBox.update("dead", str(cpuParty[0]._name + " has been brutally murdered!"))
                        else: 
                           tBox.update("effect", effect)
                           effect = ""
                        hasGone[0] = 1
                        turn = "cpu"

                     # display text if enemy dies
                     elif tBox._state == "dead" and turn == "cpu":
                        deadCpu = cpuParty[0]
                        numDead = 0
                        for i in range(3):
                           if cpuParty[i].isDead() == False:
                              cpuParty[0] = cpuParty[i]
                              cpuParty[i] = deadCpu
                              break
                           else:
                              numDead += 1
                        pygame.mixer.Sound.play(selectSound)

                        if numDead == 3:
                           tBox.update("end", "You win!")
                        else:
                           numDead = 0
                           tBox.update("effect", "Go, " + cpuParty[0]._name + "!")
                        
                     # display enemy attack info
                     elif tBox._state == "effect" and turn == "cpu" and hasGone[1] == 0:

                        move = selectMove(cpuParty[0], cpuParty[0]._moveset)
                        moveEffect = cpuParty[0].performMove(cpuParty[0]._moveset[move])
                        
                        tBox.update("action", str(cpuParty[0]._name + " used " + cpuParty[0]._moveset[move] + "!"))

                        if moveEffect["Category"] == "Damage":
                           if moveEffect["Type"] == "Intelligence":
                              if playParty[0]._type == "Dexterity":
                                 effect = "It's super effective!"
                              elif playParty[0]._type == "Strength":
                                 effect = "It's not very effective..."
                              else:
                                 effect = "It has standard effectiveness."
                           elif moveEffect["Type"] == "Dexterity":
                              if playParty[0]._type == "Charisma":
                                 effect = "It's super effective!"
                              elif playParty[0]._type == "Intelligence":
                                 effect = "It's not very effective..."
                              else:
                                 effect = "It has standard effectiveness."
                           elif moveEffect["Type"] == "Charisma":
                              if playParty[0]._type == "Strength":
                                 effect = "It's super effective!"
                              elif playParty[0]._type == "Dexterity":
                                 effect = "It's not very effective..."
                              else:
                                 effect = "It has standard effectiveness."
                           elif moveEffect["Type"] == "Strength":
                              if playParty[0]._type == "Intelligence":
                                 effect = "It's super effective!"
                              elif playParty[0]._type == "Charisma":
                                 effect = "It's not very effective..."
                              else:
                                 effect = "It has standard effectiveness."
                        elif moveEffect["Category"] == "Stat":
                           if moveEffect["Target"] == "Self":
                              effect = cpuParty[0]._name + "'s " + moveEffect["Stat"] + " has risen!"
                           else:
                              effect = playParty[0]._name + "'s " + moveEffect["Stat"] + " has diminished!"
                        pygame.mixer.Sound.play(selectSound)

                     # display effect of enemy move
                     elif tBox._state == "action" and turn == "cpu":
                        #update stats
                        if moveEffect["Target"] == "Self":
                           cpuParty[0].update(moveEffect)
                        else:
                           playParty[0].update(moveEffect, cpuParty[0]._stats, cpuParty[0]._type)

                        #display sound
                        if moveEffect["Category"] == "Damage":
                           pygame.mixer.Sound.play(damageSound)
                        elif moveEffect["Category"] == "Stat" and moveEffect["Target"] == "Self":
                           pygame.mixer.Sound.play(posStatSound)
                        elif moveEffect["Category"] == "Stat" and moveEffect["Target"] == "Other":
                           pygame.mixer.Sound.play(negStatSound)
                        elif moveEffect["Category"] == "Opening":
                           pygame.mixer.Sound.play(selectStatSound)
                           
                          # Check if opposite dies 
                        if playParty[0].isDead():
                           tBox.update("dead", str(playParty[0]._name + " has been brutally murdered!"))
                        else:
                           tBox.update("effect", effect)
                           effect = ""
                           
                        hasGone[1] = 1
                        turn = "player"
                        
                     # display text if player dies
                     elif tBox._state == "dead" and turn == "player":
                        deadPlayer = playParty[0]
                        numDead = 0
                        for i in range(3):
                           if playParty[i].isDead() == False:
                              playParty[0] = playParty[i]
                              playParty[i] = deadPlayer
                              break
                           else:
                              numDead += 1
                        pygame.mixer.Sound.play(selectSound)
                        if numDead == 3:
                           tBox.update("end", "The CPU wins!")
                        else:
                           numDead = 0
                           tBox.update("effect", "Go, " + playParty[0]._name + "!")
                        
                     # transition back to menu
                     elif tBox._state == "effect" and turn == "player" and hasGone[0] == 0:
                        tBox.update("none", "")
                        isOpaque = False
                        pygame.mixer.Sound.play(selectSound)
                        
                     # transition back to start screen if battle is over
                     elif tBox._state == "end":
                        pygame.mixer.Sound.play(selectSound)
                        gamePhase = "start"
                        menu = "start"
                        pygame.mixer.music.load('sounds\start.mp3')
                        pygame.mixer.music.play(-1)

                     # display menu descriptions
                     elif tBox._state == "describe":
                        pygame.mixer.Sound.play(selectSound)
                        isOpaque = False
                        
                     
               # If text box isn't opaque, then a menu is active
               else:
                  if menu == "main":
                     for button in buttons:
                        
                        if button._buttonName == "Attack":
                           l_coords = (button._coords[0], button._coords[1])
                           r_coords = (l_coords[0] + 400, l_coords[1] + 150)
                           if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                              event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:
                              menu = "battle"
                              pygame.mixer.Sound.play(selectSound)
                              
                        elif button._buttonName == "Switch":
                           l_coords = (button._coords[0], button._coords[1])
                           r_coords = (l_coords[0] + 400, l_coords[1] + 150)
                           if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                              event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:
                              menu = "switch"
                              pygame.mixer.Sound.play(selectSound)
                           
                        elif button._buttonName == "Exit":
                           l_coords = (button._coords[0], button._coords[1])
                           r_coords = (l_coords[0] + 400, l_coords[1] + 150)
                           if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                              event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:
                              pygame.mixer.Sound.play(exitSound)
                              menu = "start"
                              gamePhase = "start"
                              pygame.mixer.music.load('sounds\start.mp3')
                              pygame.mixer.music.play(-1)
                              
                              
                  elif menu == "battle":
                     for button in buttons:

                        if button._buttonName in (playParty[0]._moveset):
                           # If Player performs a move
                           l_coords = (button._coords[0], button._coords[1])
                           r_coords = (l_coords[0] + 240, l_coords[1] + 150)

                           # Check which button has been pressed
                           if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                              event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:

                              moveEffect = playParty[0].performMove(button._buttonName)

                              #left click
                              if pygame.mouse.get_pressed()[0] == 1:
                                 

                                 tBox.update("action", str(playParty[0]._name + " used " + button._buttonName + "!"))

                                 if moveEffect["Category"] == "Damage":
                                    if moveEffect["Type"] == "Intelligence":
                                       if cpuParty[0]._type == "Dexterity":
                                          effect = "It's super effective!"
                                       elif cpuParty[0]._type == "Strength":
                                          effect = "It's not very effective..."
                                       else:
                                          effect = "It has standard effectiveness."
                                    elif moveEffect["Type"] == "Dexterity":
                                       if cpuParty[0]._type == "Charisma":
                                          effect = "It's super effective!"
                                       elif cpuParty[0]._type == "Intelligence":
                                          effect = "It's not very effective..."
                                       else:
                                          effect = "It has standard effectiveness."
                                    elif moveEffect["Type"] == "Charisma":
                                       if cpuParty[0]._type == "Strength":
                                          effect = "It's super effective!"
                                       elif cpuParty[0]._type == "Dexterity":
                                          effect = "It's not very effective..."
                                       else:
                                          effect = "It has standard effectiveness."
                                    elif moveEffect["Type"] == "Strength":
                                       if cpuParty[0]._type == "Intelligence":
                                          effect = "It's super effective!"
                                       elif cpuParty[0]._type == "Charisma":
                                          effect = "It's not very effective..."
                                       else:
                                          effect = "It has standard effectiveness."
                                 elif moveEffect["Category"] == "Stat":
                                    if moveEffect["Target"] == "Other":
                                       effect = cpuParty[0]._name + "'s " + moveEffect["Stat"] + " has diminished!"
                                    else:
                                       effect = playParty[0]._name + "'s " + moveEffect["Stat"] + " has risen!"
                                 isOpaque = True
                                 menu = "main"
                                 pygame.mixer.Sound.play(selectSound)
                              #right click
                              else:
                                 tBox.update("describe", moveEffect["Description"])
                                 pygame.mixer.Sound.play(selectSound)
                                 isOpaque = True
                              
                        else:
                           # If Player presses exit
                           l_coords = (button._coords[0], button._coords[1])
                           r_coords = (l_coords[0] + 240, l_coords[1] + 150)
                           
                           if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                           event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:
                              
                              menu = "main"
                              pygame.mixer.Sound.play(exitSound)

                  elif menu == "switch":
                     for button in buttons:
                           
                        if button._buttonName == playParty[0]._name:
                           l_coords = (button._coords[0], button._coords[1])
                           r_coords = (l_coords[0] + 300, l_coords[1] + 150)
                           if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                              event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:

                              #left click
                              if pygame.mouse.get_pressed()[0] == 1:
                                 menu = "main"
                                 pygame.mixer.Sound.play(deniedSound)
                              #right click
                              else:
                                 displayString = playParty[0]._name + ": " + "HP: " + str(playParty[0]._stats["HP"]) + \
                                                 ", ATK: " + str(playParty[0]._stats["Attack"]) + \
                                                 ", DEF: " + str(playParty[0]._stats["Defense"]) + \
                                                 ", SPD: " + str(playParty[0]._stats["Speed"])
                                 tBox.update("describe", displayString)
                                 pygame.mixer.Sound.play(selectSound)
                                 isOpaque = True
                              
                              
                              

                        elif button._buttonName == playParty[1]._name:
                           l_coords = (button._coords[0], button._coords[1])
                           r_coords = (l_coords[0] + 300, l_coords[1] + 150)
                           if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                              event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:

                              #left click
                              if pygame.mouse.get_pressed()[0] == 1:
                                 if playParty[1].isDead() == True:
                                    menu = "main"
                                    pygame.mixer.Sound.play(deniedSound)
                                 else:
                                    tBox.update("action", str(playParty[0]._name + " has been withdrawn!"))
                                    oldPeter = playParty[0]
                                    playParty[0] = playParty[1]
                                    playParty[1] = oldPeter
                                    playerSB = StatusBar(playParty[0]._name,
                                                         playParty[0]._type,
                                                         playParty[0]._baseStats["HP"],
                                                         playParty[0]._stats["HP"])
                                    effect = "Go, " + str(playParty[0]._name) + "!"
                                    isOpaque = True
                                    menu = "main"
                                    pygame.mixer.Sound.play(selectSound)
                                    moveEffect["Category"] = "Switch"
                              #right click
                              else:
                                 displayString = playParty[1]._name + ": " + "HP: " + str(playParty[1]._stats["HP"]) + \
                                                 ", ATK: " + str(playParty[1]._stats["Attack"]) + \
                                                 ", DEF: " + str(playParty[1]._stats["Defense"]) + \
                                                 ", SPD: " + str(playParty[1]._stats["Speed"])
                                 tBox.update("describe", displayString)
                                 pygame.mixer.Sound.play(selectSound)
                                 isOpaque = True

                        elif button._buttonName == playParty[2]._name:
                           l_coords = (button._coords[0], button._coords[1])
                           r_coords = (l_coords[0] + 300, l_coords[1] + 150)
                           if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                              event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:

                              #left click
                              if pygame.mouse.get_pressed()[0] == 1:
                                 if playParty[2].isDead() == True:
                                    menu = "main"
                                    pygame.mixer.Sound.play(deniedSound)
                                 else:
                                    tBox.update("action", str(playParty[0]._name + " has been withdrawn!"))
                                    oldPeter = playParty[0]
                                    playParty[0] = playParty[2]
                                    playParty[2] = oldPeter
                                    playerSB = StatusBar(playParty[0]._name,
                                                         playParty[0]._type,
                                                         playParty[0]._baseStats["HP"],
                                                         playParty[0]._stats["HP"])
                                    effect = "Go, " + str(playParty[0]._name) + "!"
                                    isOpaque = True
                                    menu = "main"
                                    pygame.mixer.Sound.play(selectSound)
                                    moveEffect["Category"] = "Switch"
                              #right click
                              else:
                                 displayString = playParty[2]._name + ": " + "HP: " + str(playParty[2]._stats["HP"]) + \
                                                 ", ATK: " + str(playParty[2]._stats["Attack"]) + \
                                                 ", DEF: " + str(playParty[2]._stats["Defense"]) + \
                                                 ", SPD: " + str(playParty[2]._stats["Speed"])
                                 tBox.update("describe", displayString)
                                 pygame.mixer.Sound.play(selectSound)
                                 isOpaque = True
                        
                        elif button._buttonName == "Exit":
                           l_coords = (button._coords[0], button._coords[1])
                           r_coords = (l_coords[0] + 300, l_coords[1] + 150)
                           if event.pos[0] > l_coords[0] and event.pos[1] > l_coords[1] and \
                              event.pos[0] < r_coords[0] and event.pos[1] < r_coords[1]:
                              menu = "main"
                              pygame.mixer.Sound.play(exitSound)
            
      
      # Update everything

      # Determine which menu buttons are present
      buttons = []
      if menu == "start":
         buttons = startMenu(buttons, drawSurface)
      elif menu == "select":
         buttons = selectMenu(buttons, drawSurface)
      elif menu == "main":
         buttons = mainMenu(buttons, drawSurface)
      elif menu == "battle":
         buttons = battleMenu(buttons, drawSurface, playParty[0])
      elif menu == "switch":
         buttons = switchMenu(buttons, drawSurface, playParty)

      # Reset stats if you return to start menu
      if gamePhase == "start":
         for peter in playParty:
            peter._stats = peter._baseStats.copy()
         for peter in cpuParty:
            peter._stats = peter._baseStats.copy()
         for row in peterBoxes:
            for peterBox in row:
               peterBox._selected = False
         numSelected = 0
         
         

      # Determine whose turn it is
      if sum(hasGone) == 2:
         if cpuParty[0]._stats["Speed"] > playParty[0]._stats["Speed"]:
            turn = "cpu"
         else:
            turn = "player"
         hasGone = [0, 0]

      # Indicate whose turn it is
      if turn == "cpu":
         playerSB.setColor("white")
         cpuSB.setColor("yellow")
      else:
         playerSB.setColor("yellow")
         cpuSB.setColor("white")
         
      # Update Status Bars
      playerSB.update(playParty[0]._name,
                      playParty[0]._type,
                      playParty[0]._baseStats["HP"],
                      playParty[0]._stats["HP"])
      cpuSB.update(cpuParty[0]._name,
                   cpuParty[0]._type,
                   cpuParty[0]._baseStats["HP"],
                   cpuParty[0]._stats["HP"])
      
      # Let our game clock tick at 60 fps
      gameClock.tick(60)
      # Get some time in seconds
      seconds = gameClock.get_time() / 1000
      
      # let others update based on the amount of time elapsed
   pygame.quit()

if __name__ == "__main__":
   main()
