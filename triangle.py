from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to draw a triangle
def draw_triangle():
    glClear(GL_COLOR_BUFFER_BIT) # Clear the screen
    glBegin(GL_TRIANGLES) # Start drawing a triangle
    glColor3f(1.0, 0.0, 0.0) # Set color to red
    glVertex2f(0.0, 0.5) # First vertex
    glColor3f(0.0, 1.0, 0.0) # Set color to green
    glVertex2f(-0.5, -0.5) # Second vertex
    glColor3f(0.0, 0.0, 1.0) # Set color to blue
    glVertex2f(0.5, -0.5) # Third vertex
    glEnd()
    glutSwapBuffers() # Display the triangle
# Setup function for the OpenGL window

def setup_window():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) # Use double buffering and RGB colors
    glutInitWindowSize(1000, 1000) # Set window size
    glutCreateWindow(b"Basic Triangle") # Create the window
# Main function

def main():
    setup_window()
    glutDisplayFunc(draw_triangle) # Register the display function to draw the triangle
    glutMainLoop() # Start the OpenGL event loop

if __name__ == "__main__":
    main()