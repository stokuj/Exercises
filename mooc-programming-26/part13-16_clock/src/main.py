import pygame
import time
import math

pygame.init()
display = pygame.display.set_mode((640, 480))
clock_obj = pygame.time.Clock()
font = pygame.font.Font(None, 36)

center_x = 320
center_y = 240
radius = 150

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    display.fill((0, 0, 0))
    
    # Get current time
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    
    # Update window title with time
    time_text = f"{current_time.tm_hour:02d}:{minutes:02d}:{seconds:02d}"
    pygame.display.set_caption(f"Clock - {time_text}")
    
    # Draw clock circle with red border
    pygame.draw.circle(display, (255, 0, 0), (center_x, center_y), radius, 3)
    
    # Calculate hand angles
    second_angle = seconds * 6 * math.pi / 180  # 360/60 = 6 degrees per second
    minute_angle = (minutes * 6 + seconds * 0.1) * math.pi / 180  # 6 degrees per minute
    hour_angle = (hours * 30 + minutes * 0.5) * math.pi / 180  # 30 degrees per hour
    
    # Draw second hand (blue)
    sec_x = center_x + (radius - 20) * math.sin(second_angle)
    sec_y = center_y - (radius - 20) * math.cos(second_angle)
    pygame.draw.line(display, (0, 0, 255), (center_x, center_y), (sec_x, sec_y), 2)
    
    # Draw minute hand (blue)
    min_x = center_x + (radius - 40) * math.sin(minute_angle)
    min_y = center_y - (radius - 40) * math.cos(minute_angle)
    pygame.draw.line(display, (0, 0, 255), (center_x, center_y), (min_x, min_y), 4)
    
    # Draw hour hand (blue)
    hour_x = center_x + (radius - 70) * math.sin(hour_angle)
    hour_y = center_y - (radius - 70) * math.cos(hour_angle)
    pygame.draw.line(display, (0, 0, 255), (center_x, center_y), (hour_x, hour_y), 6)
    
    # Draw center dot (red)
    pygame.draw.circle(display, (255, 0, 0), (center_x, center_y), 8)
    
    pygame.display.flip()
    clock_obj.tick(60)