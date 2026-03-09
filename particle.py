import pygame
import random

class Particle:
    """A class representing a bouncing particle."""

    def __init__(self, ai_game, x, y):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Physics properties (REAL position)
        # self.x = self.screen_rect.centerx
        # self.y = self.screen_rect.centery
        
        self.x = x
        self.y = y

        sigma = 100
        self.vx = random.gauss(0, sigma) # velocity in x
        self.vy = random.gauss(0, sigma) # velocity in y

        self.radius = 12
        self.color = (136, 8, 8)

    def update(self, dt):
        """Update particle position."""
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Right wall
        if self.x + self.radius >= self.screen_rect.width:
            self.x = self.screen_rect.width - self.radius
            self.vx *= -1

        # Left wall
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vx *= -1

        # Bottom wall
        if self.y + self.radius >= self.screen_rect.height:
            self.y = self.screen_rect.height - self.radius
            self.vy *= -1

        # Top wall
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.vy *= -1
                    

    def draw(self):
        """Draw particle with color based on kinetic energy."""
        # Kinetic energy (mass = 1)
        ke = 0.5 * (self.vx**2 + self.vy**2)
        
        # Map KE to 0-255 range for color
        max_ke = 12_500  # adjust based on sigma, tweak to fit visually
        intensity = min(int((ke / max_ke) * 255), 255)
        
        # Color: slow = blue, fast = red
        color = (intensity, 0, 255 - intensity)
        
        pygame.draw.circle(
            self.screen,
            color,
            (int(self.x), int(self.y)),
            self.radius
        )

    
    
# def draw_heatmap(screen, particles, cell_size=20):
#     """Draw a heatmap showing local kinetic energy."""
#     width, height = screen.get_size()
#     cols = width // cell_size + 1
#     rows = height // cell_size + 1
    

#     # Grid to accumulate KE
#     ke_grid = [[0 for _ in range(rows)] for _ in range(cols)]
#     count_grid = [[0 for _ in range(rows)] for _ in range(cols)]

#     # Accumulate KE per cell
#     for p in particles:
#         col = int(p.x // cell_size)
#         row = int(p.y // cell_size)
#         ke = 0.5 * (p.vx**2 + p.vy**2)
#         ke_grid[col][row] += ke
#         count_grid[col][row] += 1

#     # Draw each cell
#     for i in range(cols):
#         for j in range(rows):
#             if count_grid[i][j] > 0:
#                 avg_ke = ke_grid[i][j] / count_grid[i][j]
#                 # Map to color
#                 max_ke = 200_000
#                 intensity = min(int((avg_ke / max_ke) * 255), 255)
#                 color = (intensity, 0, 255 - intensity)
#                 rect = pygame.Rect(i*cell_size, j*cell_size, cell_size, cell_size)
#                 pygame.draw.rect(screen, color, rect)
