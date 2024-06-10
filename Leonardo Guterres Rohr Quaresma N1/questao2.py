import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
screen_dimensions = (400, 350)
pygame.display.set_mode(screen_dimensions, DOUBLEBUF | OPENGL)

# Configura a viewport e a matriz de projeção
glViewport(0, 0, screen_dimensions[0], screen_dimensions[1])
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, screen_dimensions[0], 0, screen_dimensions[1])
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Lista para armazenar os pontos clicados
click_points = []

# Função para renderizar os pontos
def render_points():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa o buffer de cor e profundidade
    glBegin(GL_POINTS)  # Inicia a renderização dos pontos
    for point in click_points:
        glVertex2fv(point)  # Define a posição dos pontos
    glEnd()
    pygame.display.flip()  # Atualiza a tela

# Loop principal do programa
active = True
while active:
    for event in pygame.event.get():
        if event.type == QUIT:  # Verifica se o evento de saída foi acionado
            active = False
        elif event.type == MOUSEBUTTONDOWN:  # Verifica se o botão do mouse foi pressionado
            if event.button == 1:  # Verifica se é o botão esquerdo do mouse
                x, y = event.pos
                y = screen_dimensions[1] - y  # Inverte a coordenada y
                click_points.append((x, y))  # Adiciona o ponto clicado à lista

    render_points()  # Renderiza os pontos

# Encerra o Pygame
pygame.quit()
