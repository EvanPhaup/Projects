
import pygame

class StatusBar(object):
   def __init__(self, name, pType, maxhp, hp, color = (255, 255, 255)):
      self._name = name
      self._type = pType
      self._maxHP = maxhp
      self._currHP = hp
      self._hco = float(225.0 / self._maxHP) #health coefficient
      self._color = color
      
   def draw(self, surface, side):
      if side == "left":
         #Outline and Inside of StatusBox
         pygame.draw.rect(surface, self._color,
                          pygame.Rect(50, 50, 300, 100))
         pygame.draw.rect(surface, (0, 0, 0),
                          pygame.Rect(50, 50, 300, 100), 2)

         #Create Font
         font = pygame.font.SysFont('Verdana', 20)
         #Name of Peter
         nameSurface = font.render(self._name + " (player)", False, (0, 0, 0))
         surface.blit(nameSurface,(60, 60))
         #Type of Peter
         typeSurface = font.render(self._type + " Type", False, (0, 0, 0))
         surface.blit(typeSurface,(60, 90))
         #Health of Peter
         healthSurface = font.render("HP:", False, (0, 0, 0))
         surface.blit(healthSurface,(60, 120))
         #Health Bar
         pygame.draw.rect(surface, (255, 0, 0),
                          pygame.Rect(105, 125, 225, 20))
         pygame.draw.rect(surface, (0, 255, 0),
                          pygame.Rect(105, 125, int(self._currHP * self._hco), 20))
         pygame.draw.rect(surface, (0, 0, 0),
                          pygame.Rect(105, 125, 225, 20), 2)
      else:
         #Outline and Inside of StatusBox
         pygame.draw.rect(surface, self._color,
                          pygame.Rect(850, 50, 300, 100))
         pygame.draw.rect(surface, (0, 0, 0),
                          pygame.Rect(850, 50, 300, 100), 2)
         #Create Font
         font = pygame.font.SysFont('Verdana', 20)
         #Name of Peter
         nameSurface = font.render(self._name + " (enemy)", False, (0, 0, 0))
         surface.blit(nameSurface,(860, 60))
         #Type of Peter
         typeSurface = font.render(self._type + " Type", False, (0, 0, 0))
         surface.blit(typeSurface,(860, 90))
         #Health of Peter
         healthSurface = font.render("HP:", False, (0, 0, 0))
         surface.blit(healthSurface,(860, 120))
         #Health Bar
         pygame.draw.rect(surface, (255, 0, 0),
                          pygame.Rect(905, 125, 225, 20))
         pygame.draw.rect(surface, (0, 255, 0),
                          pygame.Rect(905, 125, int(self._currHP * self._hco), 20))
         pygame.draw.rect(surface, (0, 0, 0),
                          pygame.Rect(905, 125, 225, 20), 2)
   def setColor(self, color):
      if color == "white":
         self._color = (255, 255, 255)
      elif color == "yellow":
         self._color = (255, 255, 0)
         
   def update(self, name, pType, maxHP, hp):
      self._name = name
      self._type = pType
      self._maxHP = maxHP
      self._currHP = hp
      self._hco = float(225.0 / self._maxHP)
      
      
      
   
   
   
      
   
