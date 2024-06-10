import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import math

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
screen_dimensions = (800, 600)
screen = pygame.display.set_mode(screen_dimensions, DOUBLEBUF | OPENGL)
pygame.display.set_caption('Desenho de uma Casa com OpenGL')

# Configura a viewport e a matriz de projeção
glViewport(0, 0, screen_dimensions[0], screen_dimensions[1])
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, screen_dimensions[0], 0, screen_dimensions[1])
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()


# Função para desenhar um retângulo
def draw_rectangle(x1, y1, x2, y2):
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()


# Função para desenhar um triângulo
def draw_triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


# Função para renderizar as formas
def render_shapes():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Desenha o corpo da casa (retângulo)
    glColor3f(1.0, 0.5, 0.0)  # Cor laranja
    draw_rectangle(300, 200, 500, 400)

    # Desenha o telhado da casa (triângulo)
    glColor3f(0.6, 0.3, 0.0)  # Cor marrom
    draw_triangle(280, 400, 520, 400, 400, 500)

    # Desenha a porta da casa (retângulo)
    glColor3f(0.3, 0.15, 0.0)  # Cor marrom escuro
    draw_rectangle(375, 200, 425, 300)

    # Desenha uma janela da casa (quadrado)
    glColor3f(0.7, 0.9, 1.0)  # Cor azul claro
    draw_rectangle(320, 320, 360, 360)
    draw_rectangle(440, 320, 480, 360)

    pygame.display.flip()


# Loop principal do programa
active = True
while active:
    for event in pygame.event.get():
        if event.type == QUIT:
            active = False

    render_shapes()
    pygame.time.wait(10)

pygame.quit()
