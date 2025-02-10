import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Game")

# Цвета
GRAY = (150, 150, 150)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Создаём 6 случайных цветных кругов
circles = []
for _ in range(6):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    color = random.choice(COLORS)
    circles.append((x, y, color))

# Показываем цветные круги 3 секунды
screen.fill((255, 255, 255))
for x, y, color in circles:
    pygame.draw.circle(screen, color, (x, y), 30)
pygame.display.flip()
time.sleep(3)

# Закрываем круги серым
screen.fill((255, 255, 255))
for x, y, _ in circles:
    pygame.draw.circle(screen, GRAY, (x, y), 30)
pygame.display.flip()

# Основной игровой цикл (пока игрок угадывает)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
