import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define the vertices of the cube
vertices = (
    (1, -1, -1),  # Vertex 0
    (1, 1, -1),   # Vertex 1
    (-1, 1, -1),  # Vertex 2
    (-1, -1, -1), # Vertex 3
    (1, -1, 1),   # Vertex 4
    (1, 1, 1),    # Vertex 5
    (-1, -1, 1),  # Vertex 6
    (-1, 1, 1)    # Vertex 7
)

# Define the edges that connect the vertices
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

# Function to draw the cube
def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Main function to start pygame, set up the display, and run the main loop
def main():
    pygame.init()  # Initialize pygame
    display = (800, 600)  # Set display size
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # Set display mode

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Set perspective
    glTranslatef(0.0, 0.0, -5)  # Move the cube back so it's visible

    while True:  # Main loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for quit event
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
        draw_cube()  # Draw the cube
        pygame.display.flip()  # Update the display
        pygame.time.wait(10)  # Wait a short time

if __name__ == "__main__":
    main()  
