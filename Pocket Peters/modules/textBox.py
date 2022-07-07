
import pygame

class TextBox(object):
   def __init__(self):
      self._text = ""
      #none --> action --> effect --> check isDead
      #--> action --> effect --> none
      self._state = "none"
      
   def draw(self, surface, isOpaque):
      if isOpaque:
         font = pygame.font.SysFont('Verdana', 30)
         pygame.draw.rect(surface, (255, 255, 255), (0, 600, 1200, 150))
         textsurface = font.render(self._text, False, (0, 0, 0))
         surface.blit(textsurface,(25, 625))
         pygame.draw.rect(surface, (0, 0, 0), (0, 600, 1200, 150), 2)

   def update(self, state, text):
      self._state = state
      self._text = text

      
      
      
      
   
   
   
      
   
