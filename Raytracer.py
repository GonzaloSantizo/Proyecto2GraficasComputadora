import pygame
from pygame.locals import *
import math
from rt import RayTracer
from figures import *
from lights import *
from materials import *
width = 256
height = 256

pygame.init()

screen = pygame.display.set_mode((width,height),pygame.DOUBLEBUF|pygame.HWACCEL|pygame.HWSURFACE)
screen.set_alpha(None)

raytracer = RayTracer(screen)
raytracer.envMap = pygame.image.load("textures/parkingLot.bmp")
raytracer.rtClearColor(0.25,0.25,0.25)

earthTexture = pygame.image.load("textures/earthDay.bmp")

brick = Material(diffuse=(1,0.4,0.4),spec=8,Ks=0.01)
grass = Material(diffuse=(0.4,1,0.4),spec=32,Ks=0.1)
water = Material(diffuse=(0.4,0.4,1),spec=256,Ks=0.2)
mirror = Material(diffuse=(0.9,0.9,0.9),spec=64,Ks=0.2,matType=REFLECTIVE)
blueMirror = Material(diffuse=(0.4,0.4,0.9),spec=32,Ks=0.15,matType=REFLECTIVE)
earth = Material(texture = earthTexture,spec=64,Ks=0.1,matType=REFLECTIVE)
# Definición de las matrices de rotación
def rotation_y(theta):
    """Matriz de rotación alrededor del eje Y."""
    return [
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ]

def rotation_x(phi):
    """Matriz de rotación alrededor del eje X."""
    return [
        [1, 0, 0],
        [0, math.cos(phi), -math.sin(phi)],
        [0, math.sin(phi), math.cos(phi)]
    ]

def get_orientation(theta, phi):
    orientation_y = rotation_y(theta)
    orientation_x = rotation_x(phi)
    orientation = [
        [
            orientation_x[i][0] * orientation_y[0][0] + orientation_x[i][1] * orientation_y[1][0] + orientation_x[i][2] * orientation_y[2][0],
            orientation_x[i][0] * orientation_y[0][1] + orientation_x[i][1] * orientation_y[1][1] + orientation_x[i][2] * orientation_y[2][1],
            orientation_x[i][0] * orientation_y[0][2] + orientation_x[i][1] * orientation_y[1][2] + orientation_x[i][2] * orientation_y[2][2]
        ] for i in range(3)
    ]
    return orientation

# ... [Resto del código de inicialización y carga de materiales]

# Para la cabeza
theta_head = math.radians(50)
phi_head = math.radians(10)
orientation_head = get_orientation(theta_head, phi_head)

# Para el cuerpo
theta_body = math.radians(10)
phi_body = math.radians(10)
orientation_body = get_orientation(theta_body, phi_body)

# Agregar el OBB a tu escena con la orientación
obb = OBB(position=(0, 0, -5), size=(0.5, 0.5, 0.5), orientation=orientation_head, material=grass)
raytracer.scene.append(obb)

body = OBB(position=(0, -1.65, -5), size=(0.4, 1, 0.3), orientation=orientation_body, material=grass)
#raytracer.scene.append(body)

# ... [Resto del código para renderizar y manejar eventos]



raytracer.lights.append(AmbientLight(intensity=0.4))
raytracer.lights.append(DirectionalLight(direction=(-1,-1,0),intensity=0.1))
#raytracer.lights.append(PointLight(point=(1.5,0,-5),intensity=1,color=(1,0,1)))

raytracer.rtClear()
raytracer.rtRender()

print("\nRender Time:",pygame.time.get_ticks()/1000,"secs")

isRunning = True
while isRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				isRunning = False

pygame.quit()