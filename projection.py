import pygame
import math
import numpy as np
from quaternion import Quaternion

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

vertices = [[-1, -1, 1], [1, -1, 1], 
            [1, 1, 1], [-1, 1, 1],
            [-1, -1, -1], [1, -1, -1], 
            [1, 1, -1], [-1, 1, -1]]

edges = [[0, 1], [1, 2], [2, 3], [3, 0],
         [4, 5], [5, 6], [6, 7], [7, 4],
         [0, 4], [1, 5], [2, 6], [3, 7]]


q = Quaternion.compute_rotation(45, 1, 0, 0)
q_con = q.conjugate()



rotated_vectors = []
for vertex in vertices:
    pure_quaternion = Quaternion.pure_quaternion(vertex[0], vertex[1], vertex[2])
    rotated_vertices = q * pure_quaternion * q_con
    rotated_vector = [rotated_vertices.x, rotated_vertices.y, rotated_vertices.z]
    rotated_vectors.append(rotated_vector)

for vector in rotated_vectors:
    print(vector)


projected_points = []
for point in rotated_vectors:
    x, y, z = point
    f =  200 / (z + 5)
    x, y = x * f, y * f
    projected_points.append([WIDTH / 2 + int(x), HEIGHT / 2 - int(y)])

print(projected_points)



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

    for point, text in zip(projected_points, point_texts):
        x = point[0]
        y = point[1]
        draw_text(text, text_font, BLACK, x + 5, y + 5)
        pygame.draw.circle(screen, BLACK, (x, y), 5)
    
    for edge in edges:
        p1, p2 = edge
        pygame.draw.line(screen, RED, projected_points[p1], projected_points[p2], 1)


    

    pygame.display.update()