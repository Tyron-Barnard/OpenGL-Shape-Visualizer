import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define the vertices of the pyramid
vertices = (
    (0, 1, 0),   # Top vertex
    (1, -1, 1),  # Bottom front-right vertex
    (-1, -1, 1), # Bottom front-left vertex
    (-1, -1, -1), # Bottom back-left vertex
    (1, -1, -1)  # Bottom back-right vertex
)

# Define the edges that connect the vertices
edges = (
    (0, 1),  # Edges connecting the top vertex to the base vertices
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),  # Edges forming the base of the pyramid
    (2, 3),
    (3, 4),
    (4, 1)
)

def draw_pyramid():
    """Function to draw the pyramid using OpenGL."""
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    """Main function to set up the display and run the rendering loop."""
    pygame.init()  # Initialize pygame
    display = (800, 600)  # Set the display size
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)  # Create the display

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Set the perspective
    glTranslatef(0.0, 0.0, -5)  # Move the object back so it's visible

    while True:  # Main rendering loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check if the window was closed
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
        draw_pyramid()  # Draw the pyramid
        pygame.display.flip()  # Update the display
        pygame.time.wait(10)  # Wait a short time

if __name__ == "__main__":
    main()  # Run the main function
