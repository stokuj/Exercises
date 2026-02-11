# Complete your game here
import pygame
import random


class Player:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.width = image.get_width()
        self.height = image.get_height()

        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False

    def move(self, max_width, max_height):
        if self.to_right and self.x < max_width - self.width:
            self.x += self.speed
        if self.to_left and self.x > 0:
            self.x -= self.speed
        if self.to_down and self.y < max_height - self.height:
            self.y += self.speed
        if self.to_up and self.y > 0:
            self.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)
        
class Coin:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()

    def spawn_next(self, max_width, max_height):
        max_x = max_width - self.width
        max_y = max_height - self.height
        self.x = random.randint(0, max_x) if max_x > 0 else 0
        self.y = random.randint(0, max_y) if max_y > 0 else 0

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)

class Enemy:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width = image.get_width()
        self.height = image.get_height()
        self.vx = random.choice([-3, 3])
        self.vy = random.choice([-3, 3])

    def move(self, max_width, max_height):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= max_width - self.width:
            self.vx = -self.vx
            self.x = max(0, min(self.x, max_width - self.width))
        if self.y <= 0 or self.y >= max_height - self.height:
            self.vy = -self.vy
            self.y = max(0, min(self.y, max_height - self.height))

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.width, self.height)
        
class MyGame:
    def __init__(self):
        pygame.init()
        
        self.width = 800
        self.height = 500
        self.window = pygame.display.set_mode((self.width, self.height))
        
        self.load_images()
        
        robot = self.images[2]

        coin = self.images[0]
        monster = self.images[1]

        pygame.display.set_caption("Test")

        self.player = Player(robot, 0, 0, speed=4)
        self.coin = Coin(coin, 0, 0)
        self.enemy_image = monster
        self.enemies = []

        self.enemy_spawn_ms = 10000
        self.last_enemy_spawn = pygame.time.get_ticks()

        self.score = 0
        self.font = pygame.font.Font(None, 28)
        self.title_font = pygame.font.Font(None, 56)

        self.paused = False
        self.game_over = False
        self.reset_game()
  

    def load_images(self):
        self.images = []
        for name in ["coin", "monster", "robot", "door"]:
            self.images.append(pygame.image.load(name + ".png"))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    if not self.game_over:
                        self.paused = not self.paused
                        if self.paused:
                            self.player.to_left = False
                            self.player.to_right = False
                            self.player.to_up = False
                            self.player.to_down = False
                if event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                if event.key == pygame.K_LEFT:
                    self.player.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.player.to_right = True
                if event.key == pygame.K_UP:
                    self.player.to_up = True
                if event.key == pygame.K_DOWN:
                    self.player.to_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.player.to_right = False
                if event.key == pygame.K_UP:
                    self.player.to_up = False
                if event.key == pygame.K_DOWN:
                    self.player.to_down = False

            if event.type == pygame.QUIT:
                pygame.quit(); raise SystemExit

    def move(self):
        self.player.move(self.width, self.height)
        for enemy in self.enemies:
            enemy.move(self.width, self.height)

    def random_enemy_pos(self, enemy_image):
        max_x = self.width - enemy_image.get_width()
        max_y = self.height - enemy_image.get_height()
        x = random.randint(0, max_x) if max_x > 0 else 0
        y = random.randint(0, max_y) if max_y > 0 else 0
        return x, y

    def create_enemy(self):
        x, y = self.random_enemy_pos(self.enemy_image)
        return Enemy(self.enemy_image, x, y)

    def spawn_enemies(self):
        now = pygame.time.get_ticks()
        if now - self.last_enemy_spawn >= self.enemy_spawn_ms:
            self.enemies.append(self.create_enemy())
            self.last_enemy_spawn = now

    def check_collisions(self):
        player_rect = self.player.rect()
        if player_rect.colliderect(self.coin.rect()):
            self.score += 1
            self.coin.spawn_next(self.width, self.height)
        for enemy in self.enemies:
            if player_rect.colliderect(enemy.rect()):
                self.game_over = True
                self.paused = False
                break

    def reset_game(self):
        self.player.x = (self.width - self.player.width) / 2
        self.player.y = (self.height - self.player.height) / 2
        self.player.to_left = False
        self.player.to_right = False
        self.player.to_up = False
        self.player.to_down = False

        self.coin.spawn_next(self.width, self.height)
        self.enemies = [self.create_enemy(), self.create_enemy()]
        self.last_enemy_spawn = pygame.time.get_ticks()
        self.score = 0
        self.paused = False
        self.game_over = False

    def draw_center_text(self, text, y, font):
        surface = font.render(text, True, (255, 255, 255))
        x = self.width / 2 - surface.get_width() / 2
        self.window.blit(surface, (x, y))

    def run(self):
        clock = pygame.time.Clock()    
        while True:
            self.check_events()
            if not self.paused and not self.game_over:
                self.move()
                self.check_collisions()
                self.spawn_enemies()

            # Draw the screen
            self.window.fill((135, 206, 235))
            self.coin.draw(self.window)
            self.player.draw(self.window)
            for enemy in self.enemies:
                enemy.draw(self.window)
            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.window.blit(score_text, (10, 10))
            if self.paused:
                self.draw_center_text("PAUSED", self.height / 2 - 40, self.title_font)
                self.draw_center_text("Press P or Esc to resume", self.height / 2 + 10, self.font)
            if self.game_over:
                self.draw_center_text("GAME OVER", self.height / 2 - 40, self.title_font)
                self.draw_center_text("Press R to restart", self.height / 2 + 10, self.font)
            pygame.display.flip()

            clock.tick(60)

if __name__ == "__main__":
    game = MyGame()
    game.run()
