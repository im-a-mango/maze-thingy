#Import modules
import pygame as py
import random
import os
#declare variables
w = 500
h = 500
size = w,h
scr = py.display.set_mode(size)
running = True
white = (255,255,255)
g = True
lines1 = []
lines2 = []
lx1 = []
up = False
placex2 = -100
placey2 = -100
down = False
left = False
right = False
cursor = py.mouse.get_pos()
#start pygame
while running:
    point2 = py.rect.Rect(placex2,placey2,3,3)
    py.draw.rect(scr,white,point2)
    for event in py.event.get():
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False
            if event.key == py.K_RETURN:
                g = True
            if event.key == py.K_UP:
                if up == False:
                    placey2-=50
                    up = True
            if event.key == py.K_DOWN:
                if down == False:
                    placey2+=50
                    down = True
            if event.key == py.K_LEFT:
                if left == False:
                    placex2-=50
                    left = True
            if event.key == py.K_RIGHT:
                if right == False:
                    placex2+=50
                    right = True
        if event.type == py.QUIT:
            running = False

    #Build Grid
    if g:
        scr.fill(white)
        print(lines1)
        if len(lines1) != 0:
            print(lines1[0])
        if len(lx1) != 0:
            print(lx1[0])
        lines1 = []
        lx1 = []
        lx2 = []
        ly1 = []
        ly2 = []
        lines2 = []
        l2x1 = []
        l2x2 = []
        l2y1 = []
        l2y2 = []
        for x in range(0,6):
            x2 = x*100
            for y in range(0,6):
                y2 = y*100
                coord = x2,y2
                coord2 = x2,y2-100
                coord3 = x2+100,y2
                if random.randint(1,2) == 1:
                    line1 = py.draw.line(scr,(255,0,0),coord,coord2,1)
                    lines1.append(line1)
                    lx1.append(coord[0])
                    lx2.append(coord[1])
                    ly1.append(coord2[0])
                    ly2.append(coord2[1])
                if random.randint(1,2) == 1:
                    line2 = py.draw.line(scr,(255,0,0),coord,coord3,1)
                    lines2.append(line2)
                    l2x1.append(coord[0])
                    l2x2.append(coord[1])
                    l2y1.append(coord3[0])
                    l2y2.append(coord3[1])
                    cursor = py.mouse.get_pos()
        placex = random.randint(1,4)
        placex = placex*100-50
        placey = random.randint(1,4)
        placey = placey*100-50
        py.draw.circle(scr,(0,255,255),(placex,placey),10)
        treas = py.rect.Rect(placex-25,placey-25,50,50)
        placex2 = random.randint(1,5)
        placex2 = placex2*100-50
        placey2 = random.randint(1,5)
        placey2 = placey2*100-50
        g = False
    #Check collision
    cursor = py.mouse.get_pos()
    point = py.rect.Rect(placex2,placey2,3,3)
    py.draw.rect(scr,(0,0,0),point)
    cursor = py.mouse.get_pos()
    if treas.colliderect(point):
        g = True
    c = 0
    for line in lines1:
        if point.clipline(lx1[c],lx2[c],ly1[c],ly2[c]):
            print("collide")
            running = False
        c+=1
    c=0
    for line in lines2:
        if point.clipline(l2x1[c],l2x2[c],l2y1[c],l2y2[c]):
            print("collide")
            running = False
        c+=1
    #Move character
    if up == True:
        placey2-=50
        up = False
        print("up")
    if down:
        placey2+=50
        down = False
    if left:
        placex2-=50
        left = False
    if right:
        placex2+=50
        right = False
    clock = py.time.Clock()
    clock.tick(60)
    #Update the display
    py.display.flip()
