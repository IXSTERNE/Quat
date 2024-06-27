import pygame
import math
import numpy as np
from quaternion import Quaternion

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 800, 600

pygame.display.set_caption("Quaternion 3D rotation in 2D projection")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
circle_pos = [WIDTH / 2, HEIGHT / 2]
points = []
point_texts = ["A", "B", "C", "D", "E", "F", "G", "H"]
text_font = pygame.font.SysFont("Arial", 15)
angle = 0



vertices = [[-1, -1, 1], [1, -1, 1], 
            [1, 1, 1], [-1, 1, 1],
            [-1, -1, -1], [1, -1, -1], 
            [1, 1, -1], [-1, 1, -1]]

edges = [[0, 1], [1, 2], [2, 3], [3, 0],
         [4, 5], [5, 6], [6, 7], [7, 4],
         [0, 4], [1, 5], [2, 6], [3, 7]]



def rotate_vectors(sample_vertices, q, q_con):

    rotated_vectors = []
    
    for vertex in sample_vertices:
        pure_quaternion = Quaternion.pure_quaternion(vertex[0], vertex[1], vertex[2])
        rotated_vertices = q * pure_quaternion * q_con
        rotated_vector = [rotated_vertices.x, rotated_vertices.y, rotated_vertices.z]
        rotated_vectors.append(rotated_vector)
    return rotated_vectors


def project_points(sample_rotated_vectors):

    projected_points = []
    
    for point in sample_rotated_vectors:
        x, y, z = point
        f = 200 / (z + 4)
        x, y = x * f, y * f
        projected_points.append([WIDTH / 2 + x, HEIGHT / 2 - y])
    return projected_points


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))




while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    angle += 2

    q = Quaternion.compute_rotation(math.radians(angle), 1, 1, 0)
    q_con = q.conjugate()

    rotated_vectors = rotate_vectors(vertices, q, q_con)
    projected_points = project_points(rotated_vectors)
    
    screen.fill(BLACK)

    for point, text in zip(projected_points, point_texts):
        x, y = point[0], point[1]
        draw_text(text, text_font, WHITE, x + 5, y + 5)
        pygame.draw.circle(screen, WHITE, (x, y), 5)
        
    
    for edge in edges:
        p1, p2 = edge
        pygame.draw.line(screen, RED, projected_points[p1], projected_points[p2], 1)
    
    
    pygame.display.flip()