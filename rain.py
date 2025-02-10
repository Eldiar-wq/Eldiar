import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Simulator")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Параметры дождя
NUM_DROPS = 100  # Количество капель
drops = [(random.randint(0, WIDTH), random.randint(-HEIGHT, 0)) for _ in range(NUM_DROPS)]
drop_speed = 5
water_level = HEIGHT  # Начальный уровень воды

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)  # Заливаем фон

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисуем и двигаем капли дождя
    for i in range(len(drops)):
        x, y = drops[i]
        pygame.draw.circle(screen, BLUE, (x, y), 2)  # Капли
        y += drop_speed

        # Если капля достигла воды, увеличиваем уровень воды
        if y >= water_level:
            water_level -= 1
            y = random.randint(-HEIGHT, 0)  # Новая капля сверху

        drops[i] = (x, y)

    # Рисуем уровень воды
    pygame.draw.rect(screen, BLUE, (0, water_level, WIDTH, HEIGHT - water_level))

    pygame.display.flip()  # Обновляем экран
    clock.tick(30)  # Ограничиваем FPS

pygame.quit()
