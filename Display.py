import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Import the draw functions from your model files
from Pyramid import draw_pyramid
from Prism import draw_prism
from Cube import draw_cube

# Initialize the models list with the draw functions of your models
models = [draw_pyramid, draw_prism, draw_cube]
current_model = 0  # Index of the currently displayed model
translation_vectors = [(0, 0, 0)] * len(models)  # Initialize translation vectors for each model
rotation_angles = [(0, 0, 0)] * len(models)  # Initialize rotation angles for each model
scaling_factors = [(1, 1, 1)] * len(models)  # Initialize scaling factors for each model

class Display:
    def __init__(self):
        pygame.init()
        self.display = (800, 600)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

    def main_loop(self):
        global current_model, translation_vectors, rotation_angles, scaling_factors
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_model = (current_model + 1) % len(models)
                    # Translation keys
                    elif event.key == pygame.K_a:  # Translate left on x-axis
                        translation_vectors[current_model] = (translation_vectors[current_model][0] - 0.1, translation_vectors[current_model][1], translation_vectors[current_model][2])
                    elif event.key == pygame.K_d:  # Translate right on x-axis
                        translation_vectors[current_model] = (translation_vectors[current_model][0] + 0.1, translation_vectors[current_model][1], translation_vectors[current_model][2])
                    elif event.key == pygame.K_w:  # Translate up on y-axis
                        translation_vectors[current_model] = (translation_vectors[current_model][0], translation_vectors[current_model][1] + 0.1, translation_vectors[current_model][2])
                    elif event.key == pygame.K_s:  # Translate down on y-axis
                        translation_vectors[current_model] = (translation_vectors[current_model][0], translation_vectors[current_model][1] - 0.1, translation_vectors[current_model][2])
                    elif event.key == pygame.K_q:  # Translate closer on z-axis
                        translation_vectors[current_model] = (translation_vectors[current_model][0], translation_vectors[current_model][1], translation_vectors[current_model][2] + 0.1)
                    elif event.key == pygame.K_e:  # Translate further on z-axis
                        translation_vectors[current_model] = (translation_vectors[current_model][0], translation_vectors[current_model][1], translation_vectors[current_model][2] - 0.1)
                    # Rotation keys
                    elif event.key == pygame.K_u:  # Rotate counter-clockwise around x-axis
                        rotation_angles[current_model] = (rotation_angles[current_model][0] + 5, rotation_angles[current_model][1], rotation_angles[current_model][2])
                    elif event.key == pygame.K_j:  # Rotate clockwise around x-axis
                        rotation_angles[current_model] = (rotation_angles[current_model][0] - 5, rotation_angles[current_model][1], rotation_angles[current_model][2])
                    elif event.key == pygame.K_i:  # Rotate counter-clockwise around y-axis
                        rotation_angles[current_model] = (rotation_angles[current_model][0], rotation_angles[current_model][1] + 5, rotation_angles[current_model][2])
                    elif event.key == pygame.K_k:  # Rotate clockwise around y-axis
                        rotation_angles[current_model] = (rotation_angles[current_model][0], rotation_angles[current_model][1] - 5, rotation_angles[current_model][2])
                    elif event.key == pygame.K_o:  # Rotate counter-clockwise around z-axis
                        rotation_angles[current_model] = (rotation_angles[current_model][0], rotation_angles[current_model][1], rotation_angles[current_model][2] + 5)
                    elif event.key == pygame.K_l:  # Rotate clockwise around z-axis
                        rotation_angles[current_model] = (rotation_angles[current_model][0], rotation_angles[current_model][1], rotation_angles[current_model][2] - 5)
                    # Scaling keys
                    elif event.key == pygame.K_z:  # Scale down uniformly
                        scaling_factors[current_model] = tuple(s * 0.9 for s in scaling_factors[current_model])
                    elif event.key == pygame.K_x:  # Scale up uniformly
                        scaling_factors[current_model] = tuple(s * 1.1 for s in scaling_factors[current_model])

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glPushMatrix()
            # Apply translation to the current model
            glTranslatef(*translation_vectors[current_model])
            # Apply rotation to the current model
            x_angle, y_angle, z_angle = rotation_angles[current_model]
            glRotatef(x_angle, 1, 0, 0)
            glRotatef(y_angle, 0, 1, 0)
            glRotatef(z_angle, 0, 0, 1)
            # Apply scaling to the current model
            sx, sy, sz = scaling_factors[current_model]
            glScalef(sx, sy, sz)
            models[current_model]()  # Call the draw function of the current model
            glPopMatrix()
            pygame.display.flip()
            pygame.time.wait(10)

if __name__ == "__main__":
    display = Display()
    display.main_loop()

