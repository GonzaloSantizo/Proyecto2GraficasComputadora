import pygame
from pygame.locals import *
import math
from rt import RayTracer
from figures import *
from lights import *
from materials import *
import math

width = 256
height = 256

pygame.init()

screen = pygame.display.set_mode((width,height),pygame.DOUBLEBUF|pygame.HWACCEL|pygame.HWSURFACE)
screen.set_alpha(None)

raytracer = RayTracer(screen)
raytracer.envMap = pygame.image.load("textures/forestbackground.bmp")
raytracer.rtClearColor(0.25,0.25,0.25)

marstextture = pygame.image.load("textures/mars.bmp")

brick = Material(diffuse=(1,0.4,0.4),spec=8,Ks=0.01)
grass = Material(diffuse=(0.4,1,0.4),spec=32,Ks=0.1)
water = Material(diffuse=(0.4,0.4,1),spec=256,Ks=0.2)
mirror = Material(diffuse=(0.9,0.9,0.9),spec=64,Ks=0.2,matType=REFLECTIVE)
blueMirror = Material(diffuse=(0.4,0.4,0.9),spec=32,Ks=0.15,matType=REFLECTIVE)
mars = Material(texture = marstextture,spec=64,Ks=0.1,matType=REFLECTIVE)

# Definición del material del Creeper (verde)
creeper_material = Material(diffuse=(0.4, 0.9, 0.4), spec=32, Ks=0.1)

hair = Material(diffuse=(0.6,0.3,0),spec=256,Ks=0.2)
shirt = Material(diffuse=(0,0.5,0.5),spec=256,Ks=0.2)
piel = Material(diffuse=(0.88,0.76,0.68),spec=256,Ks=0.2)
Sunmirror = Material(diffuse=(1,1,0),spec=64,Ks=0.2,matType=REFLECTIVE)

# Coordenadas para el ojo derecho (ajustar según se necesite)


def pixelate(surface, pixel_size):
    """
    Esta función toma una superficie de pygame y la "pixela" reduciendo su tamaño y luego escalándola de nuevo.
    """
    width, height = surface.get_size()
    # Reduce la resolución
    temp_surface = pygame.transform.scale(surface, (width // pixel_size, height // pixel_size))
    # Escala de nuevo a la resolución original
    pixelated_surface = pygame.transform.scale(temp_surface, (width, height))
    return pixelated_surface

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

# Ángulo de rotación de 45 grados para ambos ejes
theta = math.radians(65)
phi = math.radians(0)

# Aplicar las matrices de rotación
orientation_y = rotation_y(theta)
orientation_x = rotation_x(phi)

# Combinar las rotaciones (rotación en X seguida de una rotación en Y)
orientation = [
    [
        orientation_x[i][0] * orientation_y[0][0] + orientation_x[i][1] * orientation_y[1][0] + orientation_x[i][2] * orientation_y[2][0],
        orientation_x[i][0] * orientation_y[0][1] + orientation_x[i][1] * orientation_y[1][1] + orientation_x[i][2] * orientation_y[2][1],
        orientation_x[i][0] * orientation_y[0][2] + orientation_x[i][1] * orientation_y[1][2] + orientation_x[i][2] * orientation_y[2][2]
    ] for i in range(3)
]

orientacion_ojos = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Agregar el OBB a tu escena con la orientación combinada
#obb = OBB(position=(0, 0, -5), size=(1, 1, 1), orientation=orientation, material=grass)
#raytracer.scene.append(obb)
#obb2= OBB(position=(0, -1.65, -5), size=(0.4, 1, 0.6), orientation=orientation, material=grass)

#raytracer.scene.append(obb2)

orientation_default = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]



# Cabeza del Creeper
creeper_head = OBB(position=(0, 0.6, -5), size=(0.6, 0.6, 0.6), orientation=orientation, material=creeper_material)
raytracer.scene.append(creeper_head)

creeper_head = OBB(position=(0, 0.6, -5), size=(0.6, 0.6, 0.6), orientation=orientation, material=creeper_material)
#raytracer.scene.append(creeper_head)
# Material para las características faciales (negro)
face_material = Material(diffuse=(0, 0, 0), spec=32, Ks=0.1)
eye_material = Material(diffuse=(0, 0, 0), spec=32, Ks=0)
# Ojo izquierdo
#creeper_eye_left = OBB(position=(-0.25, 0.8, -4.4), size=(0.15, 0.15, 0.05), orientation=orientacion_ojos, material=face_material)
#raytracer.scene.append(creeper_eye_left)

# Ojo derecho
#creeper_eye_right = OBB(position=(0.35, 0.8, -4.4), size=(0.15, 0.15, 0.05), orientation=orientacion_ojos, material=eye_material)
#raytracer.scene.append(creeper_eye_right)




# Cuerpo del Creeper
creeper_body = OBB(position=(0, -0.8, -5), size=(-0.6, 0.8, 0.5), orientation=orientation, material=creeper_material)
raytracer.scene.append(creeper_body)
# Pata delantera izquierda
creeper_leg_front_left = OBB(position=(-0.35, -2, -4.75), size=(0.25, 0.5, 0.25), orientation=orientation, material=creeper_material)
raytracer.scene.append(creeper_leg_front_left)

# Pata delantera derecha
creeper_leg_front_right = OBB(position=(0.35, -2, -4.75), size=(0.25, 0.5, 0.25), orientation=orientation, material=creeper_material)
raytracer.scene.append(creeper_leg_front_right)

# Pata trasera izquierda
#creeper_leg_back_left = OBB(position=(-0.35, -2, -5.25), size=(0.25, 0.5, 0.25), orientation=orientation, material=creeper_material)
#raytracer.scene.append(creeper_leg_back_left)

# Pata trasera derecha
#creeper_leg_back_right = OBB(position=(0.35, -2, -5.25), size=(0.25, 0.5, 0.25), orientation=orientation, material=creeper_material)
#raytracer.scene.append(creeper_leg_back_right)

# Definición de dimensiones para los ojos


# Dibujar ojos

square_color = (255, 0, 0)  # Red color


# steve parts

# Cabeza de steve
steve_head = OBB(position=(1.5, 0.6, -5), size=(0.6, 0.6, 0.6), orientation=orientation, material=piel)
raytracer.scene.append(steve_head)

steve_head = OBB(position=(1.5, 0.6, -5), size=(0.6, 0.6, 0.6), orientation=orientation, material=piel)
#raytracer.scene.append(creeper_head)
# Material para las características faciales (negro)
face_material = Material(diffuse=(0, 0, 0), spec=32, Ks=0.1)
eye_material = Material(diffuse=(0, 0, 0), spec=32, Ks=0)
# Ojo izquierdo
#creeper_eye_left = OBB(position=(-0.25, 0.8, -4.4), size=(0.15, 0.15, 0.05), orientation=orientacion_ojos, material=face_material)
#raytracer.scene.append(creeper_eye_left)

# Ojo derecho
#creeper_eye_right = OBB(position=(0.35, 0.8, -4.4), size=(0.15, 0.15, 0.05), orientation=orientacion_ojos, material=eye_material)
#raytracer.scene.append(creeper_eye_right)




# Cuerpo de steve
steve_body = OBB(position=(1.5, -0.8, -5), size=(-0.6, 0.8, 0.5), orientation=orientation, material=shirt)
raytracer.scene.append(steve_body)
# Pata delantera izquierda
steve_leg_front_left = OBB(position=(1.15, -2, -4.75), size=(0.25, 0.5, 0.25), orientation=orientation, material=water)
raytracer.scene.append(steve_leg_front_left)

# Pata delantera derecha
steve_leg_front_right = OBB(position=(1.85, -2, -4.75), size=(0.25, 0.5, 0.25), orientation=orientation, material=water)
raytracer.scene.append(steve_leg_front_right)


#sun
raytracer.scene.append(Sphere(position=(-2,2,-5), radius = 0.8, material=Sunmirror))

#Steve arm
raytracer.scene.append(AABB(position=(-0.5,-0.3,-5),size=(0.5,0.5,0.5),material=piel))


raytracer.lights = []  # Limpiar las luces existentes
raytracer.lights.append(AmbientLight(intensity=0.5))
raytracer.lights.append(DirectionalLight(direction=(-1, 0, -1), intensity=0.7))
raytracer.lights.append(PointLight(point=(1.5,1.5,-5),intensity=1,color=(1,0,1)))

raytracer.rtClear()
raytracer.rtRender()


COLOR_OJO = (0, 0, 0)  # Negro

# Dibujar ojos
EYE_WIDTH = 15
EYE_HEIGHT = 15
EYE_VERTICAL_POSITION = height // 2 - 40  # Adjust this for vertical positioning
LEFT_EYE_HORIZONTAL_POSITION = width // 2 - EYE_WIDTH +5
RIGHT_EYE_HORIZONTAL_POSITION = width // 2 + 20


# ojos creeper
pygame.draw.rect(screen, COLOR_OJO, (LEFT_EYE_HORIZONTAL_POSITION, EYE_VERTICAL_POSITION, EYE_WIDTH, EYE_HEIGHT))  # Ojo izquierdo
pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION, EYE_VERTICAL_POSITION, EYE_WIDTH, EYE_HEIGHT))  # Ojo derecho
pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION-15, EYE_VERTICAL_POSITION+15, EYE_WIDTH, EYE_HEIGHT))  
pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION-20, EYE_VERTICAL_POSITION+20, EYE_WIDTH+10, EYE_HEIGHT))  

pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION-20, EYE_VERTICAL_POSITION+35, EYE_WIDTH-10, EYE_HEIGHT-10))  
pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION, EYE_VERTICAL_POSITION+35, EYE_WIDTH-10, EYE_HEIGHT-10))  



#ojos steve

pygame.draw.rect(screen, COLOR_OJO, (LEFT_EYE_HORIZONTAL_POSITION, EYE_VERTICAL_POSITION, EYE_WIDTH, EYE_HEIGHT))  # Ojo izquierdo
pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION, EYE_VERTICAL_POSITION, EYE_WIDTH, EYE_HEIGHT))  # Ojo derecho
pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION+25, EYE_VERTICAL_POSITION-5, EYE_WIDTH, EYE_HEIGHT))  
pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION+30, EYE_VERTICAL_POSITION-5, EYE_WIDTH-10, EYE_HEIGHT))  

pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION+45, EYE_VERTICAL_POSITION-5, EYE_WIDTH, EYE_HEIGHT))  
pygame.draw.rect(screen, COLOR_OJO, (RIGHT_EYE_HORIZONTAL_POSITION, EYE_VERTICAL_POSITION+35, EYE_WIDTH-10, EYE_HEIGHT-10))  

pygame.display.flip()
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