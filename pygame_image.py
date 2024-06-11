import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton,True,False)
    bg_img2 = pg.transform.flip(bg_img,True,False)
    kkrect = koukaton.get_rect()
    kkrect.center = 300,200
    tmr = 0
    img_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600,0])
        screen.blit(bg_img, [-x + 3200, 0])
        screen.blit(bg_img2, [-x + 4800, 0])
        screen.blit(koukaton, kkrect.center)
        key_lst = pg.key.get_pressed()
        dx = -1
        dy = 0
        if key_lst[pg.K_UP]:
            dy = -1
        elif key_lst[pg.K_DOWN]:
            dy = 1
        elif key_lst[pg.K_LEFT]:
            dx = -2
        elif key_lst[pg.K_RIGHT]:
            dx = 2      
        kkrect.move_ip((dx,dy))   
        pg.display.update()
        tmr += 1
        img_x = img_x - 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()