import json
import pygame
from perceptron import Perceptron

# Initialize pygame
pygame.init()

# Set up the display
WINDOW_SIZE = (28, 28)
ZOOM_FACTOR = 20
DISPLAY_SIZE = (WINDOW_SIZE[0] * ZOOM_FACTOR, WINDOW_SIZE[1] * ZOOM_FACTOR)
window = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption("Drawing Window")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the drawing surface
drawing_surface = pygame.Surface(WINDOW_SIZE)
drawing_surface.fill(WHITE)

# Initialize the 2D array to store pixel information
pixel_array = [[0 for _ in range(WINDOW_SIZE[1])] for _ in range(WINDOW_SIZE[0])]

# Set up the brush
brush_size = 2

# Function to draw on the surface
def draw(x, y):
    pygame.draw.circle(drawing_surface, BLACK, (x // ZOOM_FACTOR, y // ZOOM_FACTOR), brush_size)
    # Update pixel_array
    for i in range((x // ZOOM_FACTOR) - brush_size, (x // ZOOM_FACTOR) + brush_size + 1):
        for j in range((y // ZOOM_FACTOR) - brush_size, (y // ZOOM_FACTOR) + brush_size + 1):
            if 0 <= i < WINDOW_SIZE[0] and 0 <= j < WINDOW_SIZE[1]:
                pixel_array[i][j] = 1

# Function to execute when the button is clicked
def button_click():
    print("Button clicked!")
    # Reset drawing surface and pixel array to all white
    drawing_surface.fill(WHITE)
    for i in range(WINDOW_SIZE[0]):
        for j in range(WINDOW_SIZE[1]):
            pixel_array[i][j] = 0

def guess():
    with open('weights.json', 'r') as f:
        saved_weights = json.load(f)
    
    my_perceptron = Perceptron(saved_weights)
    list_of_pixels = []
    for row in pixel_array:
        list_of_pixels += row
    print(my_perceptron.activate(list_of_pixels))


# Function to save the pixel array to JSON file
def save_pixel_array(label):
    with open("data.json", "r") as file:
        data = json.load(file)
    
    if label == '0':
        data['0'].append(pixel_array)
        print("Saved as 0")
    elif label == '1':
        data['1'].append(pixel_array)
        print("Saved as 1")
    
    with open("data.json", "w") as file:
        json.dump(data, file)

# Main loop
drawing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                draw(*event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                button_click()
            elif event.key == pygame.K_a:
                guess()
            elif event.unicode == '0' or event.unicode == '1':
                save_pixel_array(event.unicode)
    # Update the display
    scaled_surface = pygame.transform.scale(drawing_surface, DISPLAY_SIZE)
    window.fill(WHITE)
    window.blit(scaled_surface, (0, 0))
    pygame.display.flip()

# Quit pygame
pygame.quit()
