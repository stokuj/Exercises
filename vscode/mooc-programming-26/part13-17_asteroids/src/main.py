# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Asteroids Game")

robot = pygame.image.load("robot.png")
asteroid = pygame.image.load("rock.png")

# Player
player_x = 640 // 2 - robot.get_width() // 2
player_y = 480 - robot.get_height() - 10
player_speed = 5

# Asteroids
asteroids = []
asteroid_speed = 1.5
spawn_timer = 0

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game state
game_over = False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < 640 - robot.get_width():
            player_x += player_speed
        
        # Spawn asteroids
        spawn_timer += 1
        if spawn_timer >= 60:  # Spawn every 60 frames (2x mniej)
            x = random.randint(0, 640 - asteroid.get_width())
            asteroids.append({'x': x, 'y': 0})
            spawn_timer = 0
        
        # Update asteroids
        asteroids_to_remove = []
        for i, ast in enumerate(asteroids):
            ast['y'] += asteroid_speed
            
            # Check collision with player
            player_rect = pygame.Rect(player_x, player_y, robot.get_width(), robot.get_height())
            asteroid_rect = pygame.Rect(ast['x'], ast['y'], asteroid.get_width(), asteroid.get_height())
            
            if player_rect.colliderect(asteroid_rect):
                score += 1
                asteroids_to_remove.append(i)
            
            # Check if asteroid reached bottom
            elif ast['y'] > 480:
                game_over = True
        
        # Remove collected asteroids
        for i in reversed(asteroids_to_remove):
            asteroids.pop(i)
    
    # Draw
    window.fill((0, 0, 0))
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))
    
    # Draw player
    window.blit(robot, (player_x, player_y))
    
    # Draw asteroids
    for ast in asteroids:
        window.blit(asteroid, (ast['x'], ast['y']))
    
    # Draw game over message
    if game_over:
        game_over_text = font.render("GAME OVER! Press ESC to exit", True, (255, 0, 0))
        window.blit(game_over_text, (640 // 2 - game_over_text.get_width() // 2, 240))
        
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            exit()
    
    pygame.display.flip()
    clock.tick(60)