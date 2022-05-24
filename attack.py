import pygame as pg

from Characters import Entity, P1

pg.init()

box  = (0, 0, 0, 255)

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

def Strike(self):
    for n in self.atk_frames:
        pg.draw.rect(screen, box, pg.Rect(self.x, self.y, 50, 50))

        #CheckHit(self)

        screen.blit(self.atk_frames, (self.x, self.y))

def CheckHit(self):
    hit = repr(self)
    if hit == "P1":
        if P1.atk.collidepoint(P1):
            pass
    
    """ elif hit == "P2":
        if P2.atk.collidepoint(P1):
            pass """

def Weak(self):

    for self.W_grap in self.W_grap:
        pg.draw.rect(screen, box, pg.Rect(self.x, self.y, 50, 50))

        #CheckHit(self)

        screen.blit(self.W_grap, (self.x, self.y))