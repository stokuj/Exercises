# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 10
direction = "right"
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if direction == "right":
        x += velocity
        if x + robot.get_width() >= 640:
            x = 640 - robot.get_width()
            direction = "down"
    elif direction == "down":
        y += velocity
        if y + robot.get_height() >= 480:
            y = 480 - robot.get_height()
            direction = "left"
    elif direction == "left":
        x -= velocity
        if x <= 0:
            x = 0
            direction = "up"
    elif direction == "up":
        y -= velocity
        if y <= 0:
            y = 0
            direction = "right"
    
    clock.tick(60)
