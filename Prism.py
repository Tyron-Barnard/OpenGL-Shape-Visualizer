import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# The vertices of the triangular prism
vertices = (
    (1, -1, -2),  # Back right of the bottom base
    (1, 1, -2),   # Back left of the bottom base
    (-1, 0, -2),  # Front center of the bottom base
    (1, -1, 2),   # Back right of the top base
    (1, 1, 2),    # Back left of the top base
    (-1, 0, 2)    # Front center of the top base
)

# The edges that connect the vertices
edges = (
    (0, 1),  # Bottom base edges
    (1, 2),
    (2, 0),
    (3, 4),  # Top base edges
    (4, 5),
    (5, 3),
    (0, 3),  # Side edges connecting top and bottom bases
    (1, 4),
    (2, 5)
)

def draw_prism():
    """Function to draw the triangular prism using OpenGL."""
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    """Main function to set up the display and run the rendering loop."""
    pygame.init()  # Pygame
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
        draw_prism()  # Draw the triangular prism
        pygame.display.flip()  # Update the display
        pygame.time.wait(10)  # Wait a short time

if __name__ == "__main__":
    main()  # Run the main function
