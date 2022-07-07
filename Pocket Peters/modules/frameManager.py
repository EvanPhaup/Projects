"""
A Singleton Frame Manager class
Author: Liz Matthews, 9/20/2019

Provides on-demand loading of images for a pygame program. Will load entire sprite sheets if given an offset.

"""


from pygame import image, Surface, Rect, SRCALPHA
from os.path import join


class FrameManager(object):
   """A singleton factory class to create and store frames on demand."""
   
   # The singleton instance variable
   _INSTANCE = None
   
   @classmethod
   def getInstance(cls):
      """Used to obtain the singleton instance"""
      if cls._INSTANCE == None:
         cls._INSTANCE = cls._FM()
      
      return cls._INSTANCE
   
   # Do not directly instantiate this class!
   class _FM(object):
      """An internal FrameManager class to contain the actual code. Is a private class."""
      
      # Folder in which images are stored
      _IMAGE_FOLDER = "images"
      
      # Static information about the frame sizes of particular image sheets.
      _FRAME_SIZES = {
         "peterGriffin.png" :  (165,300),
         "peterBalboa.png" : (184,300),
         "easterPeter.png" : (157, 300),
         "handsomePeter.png" : (191, 300),
         "indianaGriffin.png" : (164, 300),
         "longJohnPeter.png" : (173, 300),
         "millenialPeter.png" : (183, 300),
         "peterBay.png" : (214, 300),
         "peterVice.png" : (165, 300),
         "peterMcdonald.png" : (152, 300),
         "peterSoprano.png" : (178, 300),
         "pimpGriffin.png" : (176, 300),
         "peterSnow.png" :  (198, 300),
         "heisenpeter.png" : (174, 300),
         "professorGriffin.png" : (206, 300),
         "tweakingPeter.png" : (184, 300),
         "peteFighter.png" : (169, 300),
         "background.png" : (1200, 750),
         "startScreen.png" : (1200, 750),
         "selectScreen.png" : (1200, 750)
      }
      
      # A default frame size
      _DEFAULT_FRAME = (32,32)
      
      # A list of images that require to be loaded with transparency
      _TRANSPARENCY = ["peterGriffin.png", "peterBalboa.png", "easterPeter.png",
                       "indianaGriffin.png", "longJohnPeter.png", "millenialPeter.png",
                       "peterBay.png", "peterVice.png", "peterMcdonald.png", "peterSoprano.png",
                       "pimpGriffin.png", "handsomePeter.png", "peterSnow.png",
                       "heisenpeter.png", "professorGriffin.png", "tweakingPeter.png",
                       "peteFighter.png"]
      
      # A list of images that require to be loaded with a color key
      _COLOR_KEY = ["background.png", "startScreen.png", "selectScreen.png"]
      
      
      
      def __init__(self):
         # Stores the surfaces indexed based on file name
         # The values in _surfaces can be a single Surface
         #  or a two dimentional grid of surfaces if it is an image sheet
         self._surfaces = {}
      
      
      def __getitem__(self, key):
         return self._surfaces[key]
   
      def __setitem__(self, key, item):
         self._surfaces[key] = item
      
      
      def getFrame(self, fileName, offset=None):
         # If this frame has not already been loaded, load the image from memory
         if fileName not in self._surfaces.keys():
            self._loadImage(fileName, offset != None)
         
         # If this is an image sheet, return the correctly offset sub surface
         if offset != None:
            return self[fileName][offset[1]][offset[0]]
         
         # Otherwise, return the sheet created
         return self[fileName]
      
      def _loadImage(self, fileName, sheet=False):
         # Load the full image
         fullImage = image.load(join(FrameManager._FM._IMAGE_FOLDER, fileName))
         
         # Look up some information about the image to be loaded
         transparent = fileName in FrameManager._FM._TRANSPARENCY
         colorKey = fileName in FrameManager._FM._COLOR_KEY
         
         # Detect if a transparency is needed
         if transparent:
            fullImage = fullImage.convert_alpha()
         else:
            fullImage = fullImage.convert()
         
         # If the image to be loaded is an image sheet, split it up based on the frame size
         if sheet:
               
            self[fileName] = []
            
            # Try to get the sprite size, use the default size if it is not stored
            spriteSize = FrameManager._FM._FRAME_SIZES.get(fileName, FrameManager._FM._DEFAULT_FRAME)
            
            # See how big the sprite sheet is
            sheetDimensions = fullImage.get_size()
            
            # Iterate over the entire sheet, increment by the sprite size
            for y in range(0, sheetDimensions[1], spriteSize[1]):
               self[fileName].append([])
               for x in range(0, sheetDimensions[0], spriteSize[0]):
                  
                  # If we need transparency
                  if transparent:
                     frame = Surface(spriteSize, SRCALPHA, 32)
                  else:
                     frame = Surface(spriteSize)
                  
                  frame.blit(fullImage, (0,0), Rect((x,y), spriteSize))
                  
                  # If we need to set the color key
                  if colorKey:
                     frame.set_colorkey(frame.get_at((0,0)))
                  
                  # Add the frame to the end of the current row
                  self[fileName][-1].append(frame)
         else:
            # Not a sprite sheet, full image is what we wish to store
            self[fileName] = fullImage
               
            # If we need to set the color key
            if colorKey:
               self[fileName].set_colorkey(self[fileName].get_at((0,0)))
               
            
         
