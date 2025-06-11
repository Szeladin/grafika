import pygame
import math

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

# Function to calculate dodecagon points
def calculate_dodecagon_points(center, radius):
    points = []
    for i in range(12):
        angle = math.radians(30 + i * 30)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))
    return points

# Define the dodecagon points
center = (300, 300)
radius = 150
dodecagon_points = calculate_dodecagon_points(center, radius)

# Function to draw the dodecagon with specified colors
def draw_dodecagon(surface, points):
    surface.fill((255, 255, 255, 0))  # Clear the surface with transparency
    colors = [(255, 0, 0), (255, 255, 0), (0, 0, 255)]  # Red, Yellow, Blue
    for i in range(len(points)):
        start_point = points[i]
        end_point = points[(i + 1) % len(points)]
        color = colors[i // 4]  # Use integer division to select color
        pygame.draw.line(surface, color, start_point, end_point, 2)
    screen.fill((255, 255, 255))  # Clear the screen
    screen.blit(surface, (0, 0))
    pygame.display.flip()

# Create a surface for the dodecagon
dodecagon_surface = pygame.Surface((600, 600), pygame.SRCALPHA)
draw_dodecagon(dodecagon_surface, dodecagon_points)

# Function to draw the transformed dodecagon centered on the screen
def draw_transformed_dodecagon(transformed_surface):
    screen.fill((255, 255, 255))
    rect = transformed_surface.get_rect(center=(300, 300))
    screen.blit(transformed_surface, rect.topleft)
    pygame.display.flip()

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_1]:  # Option 1: Make it smaller
        scaled_surface = pygame.transform.scale(dodecagon_surface, (300, 300))
        draw_transformed_dodecagon(scaled_surface)
    elif keys[pygame.K_2]:  # Option 2: Rotate 45 degrees from the center
        rotated_surface = pygame.transform.rotate(dodecagon_surface, 45)
        draw_transformed_dodecagon(rotated_surface)
    elif keys[pygame.K_3]:  # Option 3: Flip upside down
        flipped_surface = pygame.transform.flip(dodecagon_surface, False, True)
        draw_transformed_dodecagon(flipped_surface)
    elif keys[pygame.K_4]:  # Option 4: Make it lean
        lean_factor = 0.5
        leaned_points = [(x + lean_factor * y, y) for x, y in dodecagon_points]
        leaned_surface = pygame.Surface((600, 600), pygame.SRCALPHA)
        draw_dodecagon(leaned_surface, leaned_points)
    elif keys[pygame.K_5]:  # Option 5: Move it to the top
        moved_points = [(x, y - 150) for x, y in dodecagon_points]
        moved_surface = pygame.Surface((600, 600), pygame.SRCALPHA)
        draw_dodecagon(moved_surface, moved_points)
    elif keys[pygame.K_6]:  # Option 6: Lean and rotate 90 degrees
        lean_factor = 0.5
        leaned_points = [(x + lean_factor * y, y) for x, y in dodecagon_points]
        leaned_surface = pygame.Surface((600, 600), pygame.SRCALPHA)
        draw_dodecagon(leaned_surface, leaned_points)
        rotated_surface = pygame.transform.rotate(leaned_surface, 90)
        draw_transformed_dodecagon(rotated_surface)
    elif keys[pygame.K_7]:  # Option 7: Flip upside down and horizontally
        flipped_surface = pygame.transform.flip(dodecagon_surface, True, True)
        draw_transformed_dodecagon(flipped_surface)
    elif keys[pygame.K_8]:  # Option 8: Rotate 45 degrees from the center and reduce y by half
        rotated_surface = pygame.transform.rotate(dodecagon_surface, 45)
        reduced_surface = pygame.transform.scale(rotated_surface, (600, 300))
        draw_transformed_dodecagon(reduced_surface)
    elif keys[pygame.K_9]:  # Option 9: Lean, flip upside down, flip horizontally
        lean_factor = 0.5
        leaned_points = [(x + lean_factor * y, y) for x, y in dodecagon_points]
        leaned_surface = pygame.Surface((600, 600), pygame.SRCALPHA)
        draw_dodecagon(leaned_surface, leaned_points)
        flipped_surface = pygame.transform.flip(leaned_surface, True, True)
        draw_transformed_dodecagon(flipped_surface)
    elif keys[pygame.K_0]:  # Option 0: Default
        draw_dodecagon(dodecagon_surface, dodecagon_points)