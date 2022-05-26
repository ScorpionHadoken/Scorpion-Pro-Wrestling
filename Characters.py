import pygame as pg

pg.init()

class Entity(pg.sprite.Sprite):

    def __init__(self, name):

        self.name = name
        self.img = pg.image.load(f"C:\\Users\Dell\Desktop\Scorpion-Pro-Wrestling\Sprites\{self.name}1000.png")
        self.img.set_colorkey((0, 0, 0))
        self.img = pg.transform.scale(self.img, (75, 75))
        self.x = 10
        self.y = 10
        self.hurt = (self.x, self.y, 13, 23)
        self.weight = 0
        self.strgh = 0
        self.spd = 0
        self.P = 0
        self.walk = [pg.image.load(f"C:\\Users\Dell\Desktop\Scorpion-Pro-Wrestling\Sprites\{self.name}24.png"), pg.image.load(f"C:\\Users\Dell\Desktop\Scorpion-Pro-Wrestling\Sprites\{self.name}25.png")]

        self.atk_frames = [] # Strike
        self.W_grap = [] # Weak Grapple
        self.S_grap = []  # Strong Grapple
        self.F_frames = [] # Finisher
        i = 0

        # Punch
        while i < 2:
            self.atk_frames.append(pg.image.load(f"C:\\Users\Dell\Desktop\Scorpion-Pro-Wrestling\Sprites\{self.name}"+str(i)+'.png'))
            i += 1

        i = 7
            
        """while i < 18: # frames 7-17 are finisher animations
            self.F_frames.append(pg.image.load(f"C:\\Users\Dell\Desktop\Scorpion-Pro-Wrestling\Sprites\{self.name}"+str(i)+'.png'))
            # Goes to the specified location and adds file names like: Wrestler7.png or Wrestler17.png, to the list
            i += 1 """
        
        i = 18

        # Weak Grapple
        """while i < 24:
            self.W_frames.append(pg.image.load(f"C:\\Users\Dell\Desktop\Scorpion-Pro-Wrestlng\Sprites\{self.name}"+str(i)+'.png'))"""


P1 = Entity("The Bruiser")

def identity(self):
    self.P = self.strgh / 4
    if self.name == "The Bruiser":
        self.weight = 230
        self.strgh = 450
        self.spd = 1.5
