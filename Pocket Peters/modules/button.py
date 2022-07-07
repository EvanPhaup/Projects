
import pygame

class Button(object):
   def __init__(self, buttonName, coords, menuType, moveType = ""):
      self._buttonName = buttonName
      self._coords = coords
      self._isPressed = False
      self._menuType = menuType
      self._moveType = moveType
      
   def draw(self, surface, textColor = (0,0,0)):

      if self._menuType == "start":

         font = pygame.font.SysFont('Verdana', 60)
         
         if self._buttonName == "Start":
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(self._coords))
            textsurface = font.render(self._buttonName, False, (0, 0, 0))
            surface.blit(textsurface,(self._coords[0]+200, self._coords[1] + 35))
                         
         elif self._buttonName == "Exit":
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self._coords))
            textsurface = font.render(self._buttonName, False, (0, 0, 0))
            surface.blit(textsurface,(self._coords[0]+220, self._coords[1] + 35))

      elif self._menuType == "select":

         font = pygame.font.SysFont('Verdana', 60)
         
         if self._buttonName == "Confirm":
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(self._coords))
            textsurface = font.render(self._buttonName, False, (0, 0, 0))
            surface.blit(textsurface,(self._coords[0]+200, self._coords[1] + 35))
                         
         elif self._buttonName == "Back":
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self._coords))
            textsurface = font.render(self._buttonName, False, (0, 0, 0))
            surface.blit(textsurface,(self._coords[0]+220, self._coords[1] + 35))
            
      elif self._menuType == "main":

         font = pygame.font.SysFont('Verdana', 30)
         
         if self._buttonName == "Attack":
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(self._coords))
            textsurface = font.render(self._buttonName, False, (0, 0, 0))
            surface.blit(textsurface,(self._coords[0]+133, self._coords[1] + 50))
            
         elif self._buttonName == "Switch":
            pygame.draw.rect(surface, (0, 0, 255), pygame.Rect(self._coords))
            textsurface = font.render(self._buttonName, False, (0, 0, 0))
            surface.blit(textsurface,(self._coords[0]+148, self._coords[1] + 50))
                         
         elif self._buttonName == "Exit":
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self._coords))
            textsurface = font.render(self._buttonName, False, (0, 0, 0))
            surface.blit(textsurface,(self._coords[0]+168, self._coords[1] + 50))         
         
      elif self._menuType == "battle":

         font = pygame.font.SysFont('Verdana', 20)

         if self._buttonName == "Exit":
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self._coords))
            
         else:
            pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(self._coords))

         if self._moveType == "Dexterity":
            textColor = (0, 255, 0)
         elif self._moveType == "Charisma":
            textColor = (255, 0, 0)
         elif self._moveType == "Intelligence":
            textColor = (0, 0, 255)
         elif self._moveType == "Strength":
            textColor = (128, 0, 128)
         else:
            textColor = (0, 0, 0)
            
         textsurface = font.render(self._buttonName, False, textColor)
         # Start each text at 120 [half of rectangle width] - 11 [average character widith for font] * .5(button name length)
         surface.blit(textsurface,(self._coords[0]+(120 - int(11/2 * len(self._buttonName))), self._coords[1]+60))

      elif self._menuType == "switch":

         font = pygame.font.SysFont('Verdana', 20)

         if self._buttonName == "Exit":
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self._coords))
            
         else:
            pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(self._coords))

         textsurface = font.render(self._buttonName, False, (0, 0, 0))
         # Start each text at 150 [half of rectangle width] - 11 [average character widith] * .5(button name length)
         surface.blit(textsurface,(self._coords[0]+(150 - int(11/2 * len(self._buttonName))), self._coords[1]+60))
         
      pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(self._coords), 2)

      
      
      
      
   
   
   
      
   
