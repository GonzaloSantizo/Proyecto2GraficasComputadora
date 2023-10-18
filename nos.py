import pygame

# Inicializar pygame
pygame.init()

# Tamaños y colores
ANCHO = 800
ALTO = 600
COLOR_FONDO = (255, 255, 255)  # Blanco
COLOR_OJO = (0, 0, 0)  # Negro

# Crear ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Creeper')

corriendo = True
while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False

    ventana.fill(COLOR_FONDO)

    # Dibujar los ojos del Creeper (cuadrados)
    pygame.draw.rect(ventana, COLOR_OJO, (ANCHO // 2 - 60, ALTO // 2 - 60, 50, 50))  # Ojo izquierdo
    pygame.draw.rect(ventana, COLOR_OJO, (ANCHO // 2 + 10, ALTO // 2 - 60, 50, 50))  # Ojo derecho

    pygame.display.flip()

pygame.quit()
