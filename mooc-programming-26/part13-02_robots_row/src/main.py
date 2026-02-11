# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width = 800
height = 500
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

window.fill((0, 0, 0))


for i in range(10):
    window.blit(robot, (50+i*robot_width, 50))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()