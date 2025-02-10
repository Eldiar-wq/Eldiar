import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Twinkling Stars")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Параметры звёзд
NUM_STARS = 50  # Количество звёзд
stars = []
for _ in range(NUM_STARS):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.randint(2, 5)
    speed = random.uniform(0.02, 0.05)  # Скорость мерцания
    stars.append([x, y, size, speed, 1])  # (x, y, размер, скорость, направление)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)  # Чёрный фон (ночное небо)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисуем и анимируем звёзды
    for star in stars:
        x, y, size, speed, direction = star
        pygame.draw.circle(screen, WHITE, (x, y), int(size))

        # Изменяем размер (мерцание)
        size += speed * direction
        if size >= 6 or size <= 2:
            star[4] *= -1  # Меняем направление увеличения/уменьшения

        star[2] = size  # Обновляем размер звезды

    pygame.display.flip()  # Обновляем экран
    clock.tick(30)  # Ограничиваем FPS

pygame.quit(