import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Тестовое окно")

screen.fill((255, 255, 255))  # Заполняем белым цветом
pygame.display.flip()  # Обновляем экран

pygame.time.delay(5000)  # Ждём 5 секунд
pygame.quit()
