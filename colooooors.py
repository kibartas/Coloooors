#!/bin/python3

import pygame
import pygame.freetype
import re

# to choose from 142 different colors
def giveColorV0(ColorsRGBString, i):
    colorRGB = ColorsRGBString[i]
    colorRGB = colorRGB.split(', ')
    colorRGB = [int(x) for x in colorRGB]
    colorName = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', ColorsRGBString[i-1])
    colorName = ' '.join(colorName)
    return (colorRGB, colorName)

# to choose from 1537 different colors
def giveColorV1(RGBString, NamesString, i):
    RGBString = RGBString.split('\n')
    RGBCopy = RGBString[i].split(' ')
    RGBCopy = [int(i) for i in RGBCopy]
    NamesString = NamesString.split('\n')
    return (RGBCopy, NamesString[i])

def main():
    ColorsRGBFile = open('RGBValuesWikipedia.txt', 'r')
    ColorsNamesFile = open('ColorNamesWikipedia.txt', 'r')

    fileStrings = (ColorsRGBFile.read(), ColorsNamesFile.read())


    #ColorsRGBString = ColorsRGBFile.read().split('\n')
    
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    myfont = pygame.freetype.SysFont('Comic Sans MS', 15)
    running = True
    #colorNumber = 1
    #screen_colors, screen_colors_name = giveColorV0(ColorsRGBString, colorNumber)
    colorNumber = 0
    screen_colors, screen_colors_name = giveColorV1(fileStrings[0], fileStrings[1], colorNumber)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP:
                screen.fill(screen_colors)
                myfont.render_to(screen, (10, 10), screen_colors_name, (0, 0, 0))
                pygame.display.flip()
                print(screen_colors_name)
                colorNumber += 1
                if colorNumber > 1536:
                    colorNumber = 0
                screen_colors, screen_colors_name = giveColorV1(fileStrings[0], fileStrings[1], colorNumber)

                #colorNumber += 2
                #if colorNumber > 285:
                #    colorNumber = 1
                #screen_colors, screen_colors_name = giveColorV0(ColorsRGBString, colorNumber)


if __name__=="__main__":
    main()
