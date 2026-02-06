# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robots = []
spawn_timer = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Randomly create new falling robots
    spawn_timer += 1
    if spawn_timer >= 120:  # 1 robot per second (60 frames)
        x = random.randint(0, 640 - robot.get_width())
        robots.append({'x': x, 'y': 0, 'state': 'falling'})
        spawn_timer = 0

    window.fill((0, 0, 0))
    
    # Update and draw robots
    robots_to_remove = []
    for i, r in enumerate(robots):
        if r['state'] == 'falling':
            r['y'] += 2  # falling speed
            if r['y'] + robot.get_height() >= 480:  # reached ground
                r['y'] = 480 - robot.get_height()
                r['state'] = 'walking'
                r['direction'] = random.choice([-1, 1])  # left or right
        elif r['state'] == 'walking':
            r['x'] += r['direction'] * 2  # walking speed
            if r['x'] < 0 or r['x'] > 640:  # disappeared off screen
                robots_to_remove.append(i)
        
        window.blit(robot, (r['x'], r['y']))
    
    # Remove robots that went off screen
    for i in reversed(robots_to_remove):
        robots.pop(i)
    
    pygame.display.flip()
    clock.tick(60)