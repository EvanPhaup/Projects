from .drawable import Drawable
from .vector2D import Vector2
from .frameManager import FrameManager

import pygame

class PeterBox(Drawable):
   def __init__(self, coords, imageName):
      super().__init__(imageName, Vector2(coords[0], coords[1]))
      self._coords = coords
      self._selected = False
      self._imageName = imageName
      self._image = FrameManager.getInstance().getFrame(self._imageName, None)
      
   def draw(self, surface):

      if self._selected == True:
         pygame.draw.rect(surface, (255, 0, 0), self._coords, 2)
      else:
         pygame.draw.rect(surface, (0, 0, 0), self._coords, 2)
      
      blitImage = pygame.transform.scale(self._image, (150, 200))
      
      surface.blit(blitImage, (self._coords[0], self._coords[1]))



      
      
      
      
   
   
   
      
   
