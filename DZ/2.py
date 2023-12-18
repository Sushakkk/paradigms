import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана и ячеек лабиринта
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player_pos = [1, 1]
finish_pos = [3,6]

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Лабиринт")

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Обработка клавиш для перемещения игрока
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and MAZE[player_pos[0] - 1][player_pos[1]] != 1:
                player_pos[0] -= 1
            elif event.key == pygame.K_DOWN and MAZE[player_pos[0] + 1][player_pos[1]] != 1:
                player_pos[0] += 1
            elif event.key == pygame.K_LEFT and MAZE[player_pos[0]][player_pos[1] - 1] != 1:
                player_pos[1] -= 1
            elif event.key == pygame.K_RIGHT and MAZE[player_pos[0]][player_pos[1] + 1] != 1:
                player_pos[1] += 1

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка лабиринта
    for i in range(len(MAZE)):
        for j in range(len(MAZE[i])):
            if MAZE[i][j] == 1:
                pygame.draw.rect(screen, WHITE, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif MAZE[i][j] == 2:
                pygame.draw.rect(screen, RED, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Отрисовка игрока
    pygame.draw.circle(screen, WHITE, (player_pos[1] * CELL_SIZE + CELL_SIZE // 2, player_pos[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

    # Отрисовка финиша
    pygame.draw.circle(screen, RED, (finish_pos[1] * CELL_SIZE + CELL_SIZE // 2, finish_pos[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

    # Проверка, достиг ли игрок финиша
    if player_pos == finish_pos:
        print("Вы достигли финиша! Игра завершена.")
        pygame.quit()
        sys.exit()

    # Обновление экрана
    pygame.display.flip()

    # Задержка для управления скоростью игры
    pygame.time.delay(100)
