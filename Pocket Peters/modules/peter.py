from .drawable import Drawable

import pygame
import random
class Peter(Drawable):
   def __init__(self, imageName, position, facing):
      super().__init__(imageName, position, facing)

      if self._imageName == "peterGriffin.png":
         self._name = "Peter Griffin"
         self._moveset = ["Cutaway Gag",
                          "Chicken Punch",
                          "Plot Armor",
                          "Annoy"]
         self._baseStats = {
            "HP" : 150,
            "Attack" : 150,
            "Defense" : 150,
            "Speed" : 150,
            }
         
         self._type = "Normal"
      elif self._imageName == "easterPeter.png":
         self._name = "Easter Peter"
         self._moveset = ["Egg Toss",
                          "Burp",
                          "Hop",
                          "Dig"]
         self._baseStats = {
            "HP" : 100,
            "Attack" : 100,
            "Defense" : 75,
            "Speed" : 125,
            }
         self._type = "Dexterity"
      elif self._imageName == "handsomePeter.png":
         self._name = "Handsome Peter"
         self._moveset = ["Attract",
                          "Flex",
                          "Mortify",
                          "Olympic Toss"]
         self._baseStats = {
            "HP" : 100,
            "Attack" : 75,
            "Defense" : 125,
            "Speed" : 100,
            }
         self._type = "Charisma"
      elif self._imageName == "indianaGriffin.png":
         self._name = "Indiana Griffin"
         self._moveset = ["Whip",
                          "Lecture",
                          "Bullseye",
                          "Plot Armor"]
         self._baseStats = {
            "HP" : 75,
            "Attack" : 150,
            "Defense" : 100,
            "Speed" : 125,
            }
         self._type = "Intelligence"
      elif self._imageName == "longJohnPeter.png":
         self._name = "Long John Peter"
         self._moveset = ["Slash",
                          "Sea Shanty",
                          "Rum Rage",
                          "Scurvy"]
         self._baseStats = {
            "HP" : 125,
            "Attack" : 75,
            "Defense" : 150,
            "Speed" : 100,
            }
         self._type = "Charisma"
      elif self._imageName == "millenialPeter.png":
         self._name = "Millenial Peter"
         self._moveset = ["Tweet",
                          "Protest",
                          "Cancel",
                          "Selfie"]
         self._baseStats = {
            "HP" : 100,
            "Attack" : 125,
            "Defense" : 75,
            "Speed" : 150,
            }
         self._type = "Dexterity"
      elif self._imageName == "peterBalboa.png":
         self._name = "Peter Balboa"
         self._moveset = ["Mega Punch",
                          "Mumble",
                          "Comeback",
                          "Train"]
         self._baseStats = {
            "HP" : 150,
            "Attack" : 125,
            "Defense" : 125,
            "Speed" : 100,
            }
         self._type = "Strength"
      elif self._imageName == "peterBay.png":
         self._name = "Peter Bay"
         self._moveset = ["Explosion",
                          "Keg Toss",
                          "One Liner",
                          "Quick Sequel"]
         self._baseStats = {
            "HP" : 150,
            "Attack" : 100,
            "Defense" : 125,
            "Speed" : 75,
            }
         self._type = "Strength"
      elif self._imageName == "peterMcdonald.png":
         self._name = "Peter McDonald"
         self._moveset = ["Slash",
                          "Agility",
                          "Stab",
                          "Clown"]
         self._baseStats = {
            "HP" : 125,
            "Attack" : 150,
            "Defense" : 100,
            "Speed" : 175,
            }
         self._type = "Dexterity"
      elif self._imageName == "peterSoprano.png":
         self._name = "Peter Soprano"
         self._moveset = ["Intimidate",
                          "Negotiate",
                          "Excommunicate",
                          "Bribe"]
         self._baseStats = {
            "HP" : 100,
            "Attack" : 150,
            "Defense" : 100,
            "Speed" : 125,
            }
         self._type = "Intelligence"
      elif self._imageName == "peterVice.png":
         self._name = "Peter Vice"
         self._moveset = ["Montage",
                          "Shootout",
                          "Detect",
                          "Bring to Justice"]
         self._baseStats = {
            "HP" : 125,
            "Attack" : 100,
            "Defense" : 150,
            "Speed" : 125,
            }
         self._type = "Charisma"
      elif self._imageName == "pimpGriffin.png":
         self._name = "Pimp Griffin"
         self._moveset = ["Backhand",
                          "Negotiate",
                          "Hitman Burner",
                          "Make Bail"]
         self._baseStats = {
            "HP" : 175,
            "Attack" : 125,
            "Defense" : 150,
            "Speed" : 100,
            }
         self._type = "Strength"
      elif self._imageName == "peterSnow.png":
         self._name = "Peter Snow"
         self._moveset = ["Northern Chill",
                          "Longclaw",
                          "Bend the Knee",
                          "Stark's Wrath"]
         self._baseStats = {
            "HP" : 150,
            "Attack" : 100,
            "Defense" : 175,
            "Speed" : 125,
            }
         self._type = "Charisma"
      elif self._imageName == "heisenpeter.png":
         self._name = "Heisenpeter"
         self._moveset = ["Burn Rubber",
                          "Call Saul",
                          "The Cigarette",
                          "Rapid Fire"]
         self._baseStats = {
            "HP" : 100,
            "Attack" : 175,
            "Defense" : 125,
            "Speed" : 150,
            }
         self._type = "Intelligence"
      elif self._imageName == "professorGriffin.png":
         self._name = "Professor Griffin"
         self._moveset = ["Cutting Wit",
                          "Tenure",
                          "Lecture",
                          "Trick Question"]
         self._baseStats = {
            "HP" : 75,
            "Attack" : 125,
            "Defense" : 100,
            "Speed" : 100,
            }
         self._type = "Intelligence"
      elif self._imageName == "tweakingPeter.png":
         self._name = "Tweaking Peter"
         self._moveset = ["Claw",
                          "Claw",
                          "Claw",
                          "Claw"]
         self._baseStats = {
            "HP" : 125,
            "Attack" : 125,
            "Defense" : 100,
            "Speed" : 150,
            }
         self._type = "Dexterity"
      elif self._imageName == "peteFighter.png":
         self._name = "Pete Fighter"
         self._moveset = ["Meditate",
                          "Drop Kick",
                          "The Finger Hold",
                          "Train"]
         self._baseStats = {
            "HP" : 125,
            "Attack" : 100,
            "Defense" : 100,
            "Speed" : 75,
            }
         self._type = "Strength"
      self._stats = self._baseStats.copy()

   def __str__(self):
      return ("\n" + self._name + "\n" +
              str(self._stats["HP"]) + "\n" +
              str(self._stats["Attack"]) + "\n" +
              str(self._stats["Defense"]) + "\n" +
              str(self._stats["Speed"]))

   def performMove(self, moveName):
      if moveName == "Agility":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Speed by 20%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Speed",
                 "Effect" : .20,
                 "Description" : "Raises Own Speed by 20%"}
      elif moveName == "Annoy":
         """
         Category: Damage
         Type: Charisma
         Target: Opposing Peter
         Effect: Deals 30 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Charisma",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 30,
                 "Description" : "Charisma-Type; Deals 30 Base Damage to Enemy"}
      elif moveName == "Attract":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Attack by 15%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : -.15,
                 "Description" : "Lowers Opposing Attack by 15%"}
      elif moveName == "Backhand":
         """
         Category: Damage
         Type: Strength
         Target: Opposing Peter
         Effect: Deals 80 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Strength",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 80,
                 "Description" : "Strength-Type; Deals 80 Base Damage to Enemy"}
      elif moveName == "Bend the Knee":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Defense by 30%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Defense",
                 "Effect" : -.30,
                 "Description" : "Lowers Opposing Defense by 30%"}
      elif moveName == "Bribe":
         """
         Category: Damage
         Type: Intelligence
         Target: Opposing Peter
         Effect: Deals 30 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Intelligence",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 30,
                 "Description" : "Intelligence-Type; Deals 30 Base Damage to Enemy"}
      elif moveName == "Bring to Justice":
         """
         Category: Damage
         Type: Charisma
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Charisma",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : 40,
                 "Description" : "Charisma-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "Bullseye":
         """
         Category: Damage
         Type: Intelligence
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Intelligence",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : 40,
                 "Description" : "Intelligence-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "Burn Rubber":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Speed by 25%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Speed",
                 "Effect" : .25,
                 "Description" : "Raises Own Speed by 25%"}

      elif moveName == "Burp":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Attack by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : -.10,
                 "Description" : "Lowers Opposing Attack by 10%"}
      elif moveName == "Call Saul":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Defense by 25%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Defense",
                 "Effect" : .25,
                 "Description" : "Raises Own Defense by 25%"}
      elif moveName == "Cancel":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Attack by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : -.10,
                 "Description" : "Lowers Opposing Attack by 10%"}
      elif moveName == "Claw":
         """
         Category: Damage
         Type: Dexterity
         Target: Opposing Peter
         Effect: Deals 80 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Dexterity",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 80,
                 "Description" : "Dexterity-Type; Deals 80 Base Damage to Enemy"}
      elif moveName == "Clown":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Defense by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Defense",
                 "Effect" : -.10,
                 "Description" : "Lowers Opposing Defense by 10%"}
      elif moveName == "Chicken Punch":
         """
         Category: Damage
         Type: Strength
         Target: Opposing Peter
         Effect: Deals 70 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Strength",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : 70,
                 "Description" : "Strength-Type; Deals 70 Base Damage to Enemy"}
      elif moveName == "Comeback":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Attack by 20%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Attack",
                 "Effect" : .20,
                 "Description" : "Raises Own Attack by 20%"}
      elif moveName == "Cutaway Gag":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Speed by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Speed",
                 "Effect" : -.10,
                 "Description" : "Lowers Opposing Speed by 10%"}
      elif moveName == "Cutting Wit":
         """
         Category: Damage
         Type: Charisma
         Target: Opposing Peter
         Effect: Deals 30 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Charisma",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : 30,
                 "Description" : "Charisma-Type; Deals 30 Base Damage to Enemy"}
      elif moveName == "Detect":
         """
         Category: Stat
         Type: Normal
         Target: Own Peter
         Effect: Raises own Defense by 20%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Defense",
                 "Effect" : .20,
                 "Description" : "Raises Own Defense by 20%"}
      elif moveName == "Dig":
         """
         Category: Damage
         Type: Intelligence
         Target: Opposing Peter
         Effect: Deals 30 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Intelligence",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 30,
                 "Description" : "Intelligence-Type; Deals 30 Base Damage to Enemy"}
      elif moveName == "Drop Kick":
         """
         Category: Damage
         Type: Strength
         Target: Opposing Peter
         Effect: Deals 45 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Strength",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 45,
                 "Description" : "Strength-Type; Deals 45 Base Damage to Enemy"}

      elif moveName == "Egg Toss":
         """
         Category: Damage
         Type: Dexterity
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Dexterity",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 40,
                 "Description" : "Dexterity-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "Excommunicate":
         """
         Category: Damage
         Type: Charisma
         Target: Opposing Peter
         Effect: Deals 50 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Charisma",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : 50,
                 "Description" : "Charisma-Type; Deals 50 Base Damage to Enemy"}
      elif moveName == "Explosion":
         """
         Category: Damage
         Type: Charisma
         Target: Opposing Peter
         Effect: Deals 70 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Charisma",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : 70,
                 "Description" : "Charisma-Type; Deals 70 Base Damage to Enemy"}
      elif moveName == "Flex":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Attack by 30%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Attack",
                 "Effect" : .30,
                 "Description" : "Raises Own Attack by 30%"}
      elif moveName == "Hitman Burner":
         """
         Category: Damage
         Type: Intelligence
         Target: Opposing Peter
         Effect: Deals 45 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Intelligence",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : 45,
                 "Description" : "Intelligence-Type; Deals 45 Base Damage to Enemy"}
      elif moveName == "Hop":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Speed by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Speed",
                 "Effect" : .10,
                 "Description" : "Raises Own Speed by 10%"}
      elif moveName == "Intimidate":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Defense by 20%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Defense",
                 "Effect" : -.20,
                 "Description" : "Lowers Opposing Defense by 20%"}
      elif moveName == "Keg Toss":
         """
         Category: Damage
         Type: Strength
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Strength",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 40,
                 "Description" : "Strength-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "Lecture":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Speed by 30%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Speed",
                 "Effect" : -.30,
                 "Description" : "Lowers Opposing Speed by 30%"}
      elif moveName == "Longclaw":
         """
         Category: Damage
         Type: Dexterity
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Dexterity",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 40,
                 "Description" : "Dexterity-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "Make Bail":
         """
         Category: Stat
         Type: Normal
         Target: Own Peter
         Effect: Raises own Defense by 15%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Defense",
                 "Effect" : .15,
                 "Description" : "Raises Own Defense by 15%"}
      elif moveName == "Meditate":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Attack by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Attack",
                 "Effect" : .10,
                 "Description" : "Raises Own Attack by 10%"}
      elif moveName == "Mega Punch":
         """
         Category: Damage
         Type: Strength
         Target: Opposing Peter
         Effect: Deals 50 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Strength",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : 50,
                 "Description" : "Strength-Type; Deals 50 Base Damage to Enemy"}
      elif moveName == "Montage":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Attack by 30%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Attack",
                 "Effect" : .30,
                 "Description" : "Raises Own Attack by 30%"}
      elif moveName == "Mortify":
         """
         Category: Damage
         Type: Charisma
         Target: Opposing Peter
         Effect: Deals 30 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Charisma",
                 "Target" : "Other",
                 "Stat" : "Attack",
                 "Effect" : 30,
                 "Description" : "Charisma-Type; Deals 30 Base Damage to Enemy"}
      elif moveName == "Mumble":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Speed by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Speed",
                 "Effect" : -.10,
                 "Description" : "Lowers Opposing Speed by 10%"}
      elif moveName == "Negotiate":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Speed by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Speed",
                 "Effect" : -.10,
                 "Description" : "Lowers Opposing Speed by 10%"}
      elif moveName == "Northern Chill":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Speed by 20%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Speed",
                 "Effect" : -.20,
                 "Description" : "Lowers Opposing Speed by 20%"}
      elif moveName == "Olympic Toss":
         """
         Category: Damage
         Type: Strength
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Strength",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 40,
                 "Description" : "Strength-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "One Liner":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Attack by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Attack",
                 "Effect" : .10,
                 "Description" : "Raises Own Attack by 10%"}
      
      elif moveName == "Plot Armor":
         """
         Category: Stat
         Type: Normal
         Target: Own Peter
         Effect: Raises own Defense by 20%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Defense",
                 "Effect" : .20,
                 "Description" : "Raises Own Defense by 20%"}

      elif moveName == "Protest":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing Defense by 10%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Defense",
                 "Effect" : -.10,
                 "Description" : "Lowers Opposing Defense by 10%"}
      elif moveName == "Quick Sequel":
         """
         Category: Stat
         Type: Normal
         Target: Performing Peter
         Effect: Raises own Speed by 15%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Speed",
                 "Effect" : .15,
                 "Description" : "Raises Own Speed by 15%"}
      elif moveName == "Rapid Fire":
         """
         Category: Damage
         Type: Dexterity
         Target: Opposing Peter
         Effect: Deals 70 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Dexterity",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 70,
                 "Description" : "Dexterity-Type; Deals 70 Base Damage to Enemy"}
      elif moveName == "Rum Rage":
         """
         Category: Damage
         Type: Charisma
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Charisma",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 40,
                 "Description" : "Charisma-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "Scurvy":
         """
         Category: Stat
         Type: Normal
         Target: Opposing Peter
         Effect: Lowers oppossing defense by 30%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Other",
                 "Stat" : "Speed",
                 "Effect" : -.30,
                 "Description" : "Lowers Opposing Defense by 30%"}
      elif moveName == "Sea Shanty":
         """
         Category: Stat
         Type: Normal
         Target: Own Peter
         Effect: Raises own Attack by 25%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Attack",
                 "Effect" : .25,
                 "Description" : "Raises Own Attack by 25%"}
      elif moveName == "Selfie":
         """
         Category: Stat
         Type: Normal
         Target: Own Peter
         Effect: Raises own Attack by 20%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Attack",
                 "Effect" : .20,
                 "Description" : "Raises Own Attack by 20%"}
      elif moveName == "Shootout":
         """
         Category: Damage
         Type: Intelligence
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Intelligence",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 40,
                 "Description" : "Intelligence-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "Slash":
         """
         Category: Damage
         Type: Dexterity
         Target: Opposing Peter
         Effect: Deals 30 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Dexterity",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 30,
                 "Description" : "Dexterity-Type; Deals 30 Base Damage to Enemy"}
      elif moveName == "Stab":
         """
         Category: Damage
         Type: Strength
         Target: Opposing Peter
         Effect: Deals 30 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Strength",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 30,
                 "Description" : "Strength-Type; Deals 30 Base Damage to Enemy"}
      elif moveName == "Stark's Wrath":
         """
         Category: Damage
         Type: Charisma
         Target: Opposing Peter
         Effect: Deals 60 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Charisma",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 60,
                 "Description" : "Charisma-Type; Deals 60 Base Damage to Enemy"}

      elif moveName == "Tenure":
         """
         Category: Stat
         Type: Normal
         Target: Own Peter
         Effect: Raises own Defense by 15%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Defense",
                 "Effect" : .15,
                 "Description" : "Raises Own Defense by 15%"}
      elif moveName == "The Cigarette":
         """
         Category: Damage
         Type: Intelligence
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Intelligence",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 40,
                 "Description" : "Intelligence-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "The Finger Hold":
         """
         Category: Damage
         Type: Dexterity
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Dexterity",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 40,
                 "Description" : "Dexterity-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "Train":
         """
         Category: Stat
         Type: Normal
         Target: Own Peter
         Effect: Raises own Speed by 20%
         """
         return {"Category" : "Stat",
                 "Type" : "Normal",
                 "Target" : "Self",
                 "Stat" : "Speed",
                 "Effect" : .20,
                 "Description" : "Raises Own Speed by 20%"}
      elif moveName == "Trick Question":
         """
         Category: Damage
         Type: Intelligence
         Target: Opposing Peter
         Effect: Deals 40 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Intelligence",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 40,
                 "Description" : "Intelligence-Type; Deals 40 Base Damage to Enemy"}
      elif moveName == "Tweet":
         """
         Category: Damage
         Type: Dexterity
         Target: Opposing Peter
         Effect: Deals 50 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Dexterity",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 50,
                 "Description" : "Dexterity-Type; Deals 50 Base Damage to Enemy"}
      elif moveName == "Whip":
         """
         Category: Damage
         Type: Strength
         Target: Opposing Peter
         Effect: Deals 50 Base Damage
         """
         return {"Category" : "Damage",
                 "Type" : "Strength",
                 "Target" : "Other",
                 "Stat" : "HP",
                 "Effect" : 50,
                 "Description" : "Strength-Type; Deals 50 Base Damage to Enemy"}

         

   def update(self, moveEffect, enemyStats = None, enemyType = ""):
      if moveEffect["Category"] == "Damage":
         # Find Type Multiplier
         if moveEffect["Type"] == "Dexterity" and self._type == "Charisma" \
            or moveEffect["Type"] == "Charisma" and self._type == "Strength" \
            or moveEffect["Type"] == "Strength" and self._type == "Intelligence" \
            or moveEffect["Type"] == "Intelligence" and self._type == "Dexterity":
            typeMult = 2
         elif moveEffect["Type"] == "Dexterity" and self._type == "Intelligence" \
            or moveEffect["Type"] == "Intelligence" and self._type == "Strength" \
            or moveEffect["Type"] == "Strength" and self._type == "Charisma" \
            or moveEffect["Type"] == "Charisma" and self._type == "Dexterity":
            typeMult = .5
         else:
            typeMult = 1
         # Check if Same Type Attack Bonus Applies
         if enemyType == moveEffect["Type"]:
            stab = 1.5
         else:
            stab = 1
         # Calculate random multiplier
         rand = random.randint(85, 100) / 100

         damage = 22 * moveEffect["Effect"] * (enemyStats["Attack"] / self._stats["Defense"])
         damage = int(((damage / 50) + 2) *rand * stab * typeMult)
         
         self._stats["HP"] = self._stats["HP"] - damage
         
      elif moveEffect["Category"] == "Stat":
         #Don't boost stats past 150% of base stats
         if moveEffect["Target"] == "Self" and \
            (self._stats[moveEffect["Stat"]] < self._baseStats[moveEffect["Stat"]] * 1.5):


            self._stats[moveEffect["Stat"]] = int(self._stats[moveEffect["Stat"]] * (1 + moveEffect["Effect"]))
         #Don't lower stats past 50% of base stats
         elif moveEffect["Target"] == "Other" and \
            (self._stats[moveEffect["Stat"]] > self._baseStats[moveEffect["Stat"]] * .5):

            self._stats[moveEffect["Stat"]] = int(self._stats[moveEffect["Stat"]] * (1 + moveEffect["Effect"]))

   def isDead(self):
      if self._stats["HP"] <= 0:
         return True
      else:
         return False
            
      
      
   
   
   
      
   
