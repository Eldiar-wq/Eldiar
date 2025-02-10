import pygame
import math

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Колобок и лиса")

# Цвета
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
RED = (255, 0, 0)

# Параметры Колобка
kolobok_x, kolobok_y = 100, 200
kolobok_radius = 20
angle = 0  # Угол вращения

# Параметры Лисы
fox_x, fox_y = 500, 200
fox_speed = 2

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)  # Фон

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Двигаем лису к Колобку
    if fox_x > kolobok_x:
        fox_x -= fox_speed

    # Вращаем Колобка
    angle += 5
    rotated_x = kolobok_x + math.cos(math.radians(angle)) * 5
    rotated_y = kolobok_y + math.sin(math.radians(angle)) * 5

    # Рисуем Колобка (вращение по кругу)
    pygame.draw.circle(screen, YELLOW, (int(rotated_x), int(rotated_y)), kolobok_radius)

    # Рисуем Лису (просто красный круг для упрощения)
    pygame.draw.circle(screen, RED, (fox_x, fox_y), 30)

    pygame.display.flip()  # Обновляем экран
    clock.tick(30)  # Ограничиваем FPS

pygame.quit()
