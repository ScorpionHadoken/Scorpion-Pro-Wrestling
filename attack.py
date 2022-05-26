import pygame as pg

from Characters import Entity, P1

import threading

pg.init()

box  = (0, 0, 0, 255)

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

def Strike(self):
    for n in self.atk_frames:
        screen.fill((200, 200, 200))

        n = pg.transform.scale(n, (75, 75))
        n.set_colorkey((0, 0, 0))

        #CheckHit(self)

        screen.blit(n, (self.x, self.y))

def CheckHit(self):
    hit = repr(self)
    if hit == "P1":
        if P1.atk.collidepoint(P1):
            pass
    
    """ elif hit == "P2":
        if P2.atk.collidepoint(P1):
            pass """

def Weak(self):

    for t in self.W_grap:
        screen.fill(200, 200, 200)

        t = pg.transform.scale(t, (75, 75))
        t.set_colorkey((0, 0, 0))

        #CheckHit(self)

        screen.blit(t, (self.x, self.y))

