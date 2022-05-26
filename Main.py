import pygame as pg
import threading
pg.init()

from attack import *
import Characters

LEFT = 1
RIGHT = 3
clock = pg.time.Clock()

GameFont = pg.font.SysFont("C:\\Windows\Fonts\vgasys.fon", 35)

def update_fps(): # Shows in the top left corner the current FPS
    fps = str(int(clock.get_fps()))
    fps_text = GameFont.render(fps, 1, pg.Color("red"))
    screen.blit(fps_text, (10, 10))
    return fps_text

def main(self):
    while True:

        pressed = pg.key.get_pressed()
        state = pg.mouse.get_pressed()

        clock.tick(30)

        for event in pg.event.get():
            
            if event.type == pg.MOUSEBUTTONDOWN:
                
                if event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                    Strike(self)
            
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == RIGHT:
                    NotImplementedError() # This error tells the user that I'm lazy
                
                elif pressed[pg.K_SPACE]:
                    Weak(self)

        if pressed[pg.K_w]:
            self.y -= self.spd
            
        if pressed[pg.K_s]:
            self.y += self.spd
        
        if pressed[pg.K_d]:
            self.x += self.spd
        
        if pressed[pg.K_a]:
            self.x -= self.spd


        screen.fill((200, 200, 200)) # I'll add wrestling ring l8r
        screen.blit(self.img, (self.x, self.y))
        
        update_fps()        
        pg.display.flip()



if __name__ == "__main__":
    main(P1)
