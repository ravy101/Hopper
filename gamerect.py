import ipygame
import hopper
import gameobject

class GameRect(gameobject.GameObject):
    def __init__(self, name, x, y, width, height):
        super(GameRect, self).__init__(name, x, y, 0)
        self.rect = Rect(0,0,width,height)
        self.fill_colour = WHITE
