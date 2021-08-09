import re
#import networkx as nx
#from collections import defaultdict, Counter

data = """"""

test = """"""
import pygame
pygame.init()

def is_increasing(num):
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True
import sys
def is_valid(num, pattern):
    for j in re.findall(pattern, str(num)):
        if len(j[0]) == 2:
            if is_increasing(str(num)):
                return True
            return False
    return False
pattern = r"((\d)\2+)"
print(is_valid("123444", pattern))
def solve():
    pattern = r"((\d)\2+)"
    c = 0
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    running = True
    clock = pygame.time.Clock()
    while running:
        for num in range(100000,1000000):
            if is_valid(num, pattern):
                c += 1
                coords = (int(str(num)[:3])*3, int(str(num)[3:])*2)
                screen.set_at(coords, (255,255,255))
                pygame.display.flip()

        clock.tick(400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False
                pygame.quit()
                sys.exit()
    print(c)
solve()