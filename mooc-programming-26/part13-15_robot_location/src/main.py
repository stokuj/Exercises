
import random
import pygame

pygame.init()
width = 800
height = 500
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()


x, y = random.randint(0,800-robot_width), random.randint(0,500-robot_height)
window.fill((0, 0, 0))
window.blit(robot, (x, y))

pygame.display.flip()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.posz
            # Check if click is on robot
            if x <= mouse_x <= x + robot_width and y <= mouse_y <= y + robot_height:
                x, y = random.randint(0, 800-robot_width), random.randint(0, 500-robot_height)
                window.fill((0, 0, 0))
                window.blit(robot, (x, y))
                pygame.display.flip()
    
    clock.tick(60)