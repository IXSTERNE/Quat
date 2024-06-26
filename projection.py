import pygame
import math
import numpy as np

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600

pygame.display.set_caption("3D projection")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

scale = 100
circle_pos = [WIDTH / 2, HEIGHT / 2]
points = []
point_texts = ["A", "B", "C", "D", "E", "F", "G", "H"]

points.append(np.matrix([-1, -1, 1]).reshape((3, 1)))
points.append(np.matrix([1, -1, 1]).reshape((3, 1)))
points.append(np.matrix([1, 1, 1]).reshape((3, 1)))
points.append(np.matrix([-1, 1, 1]).reshape((3, 1)))
points.append(np.matrix([-1, -1, -1]).reshape((3, 1)))
points.append(np.matrix([1, -1, -1]).reshape((3, 1)))
points.append(np.matrix([1, 1, -1]).reshape((3, 1)))
points.append(np.matrix([-1, 1, -1]).reshape((3, 1)))

projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

text_font = pygame.font.SysFont("Arial", 15)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    screen.fill(WHITE)

    for point, text in zip(points, point_texts):
        projected2d = np.dot(projection_matrix, point)
        x = int(projected2d[0, 0] * scale) + circle_pos[0]
        y = int(projected2d[1, 0] * scale) + circle_pos[1]
        draw_text(text, text_font, BLACK, x + 5, y + 5)
        pygame.draw.circle(screen, BLACK, (x, y), 5)

    pygame.display.update()