import sys
import pygame
from settings import Settings
from particle import Particle
import random
import math
from analysis import Analysis


class GasParticleSim:
    """Overall class to manage sim assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Gas Particle Simulation")

        # ai_game = current instance of AlienInvasion class
        # self.particle = Particle(self)
        self.particles = []
        # self.particles.append(Particle(self, 100, 200))
        # self.particles.append(Particle(self, 300, 200))
        # self.particles.append(Particle(self, 500, 400))

        # random.uniform(a, b) in Python is designed to generate pseudo-random floating-point numbers that follow a continuous uniform distribution within the range.

        # Random placement of particles without overlap
        for _ in range(350):
            while True:
                x = random.uniform(12, self.settings.screen_width - 12)
                y = random.uniform(12, self.settings.screen_height - 12)
                overlap = False

                for p in self.particles:
                    dx = x - p.x
                    dy = y - p.y
                    dist_sq = dx*dx + dy*dy
                    
                    if dist_sq < (2*p.radius)**2:
                        overlap = True
                        break
               
                if not overlap:
                    self.particles.append(Particle(self, x, y))
                    break

        #set the background color.
        self.bg_color = self.settings.bg_color

    def run_sim(self):
        """Start the main loop for the game."""
        # print(len(self.particles))
        # analysis = Analysis(bins=50, clip_ke=5000)
        # frame_count = 0
        while True:
            # frame_count += 1
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            self.clock.tick(60)
            print(self.clock.get_fps())
            dt = 1 / 60

            # Per frame: 
            # Update all positions -> Resolve all collisions -> Draw everything
            
            # Update all particles
            for particle in self.particles:
                particle.update(dt)

            # Handle collisions once
            self.handle_collisions()

            # Draw heatmap 
            # draw_heatmap(self.screen, self.particles, cell_size=20)

            # Draw all particles
            for particle in self.particles:
                particle.draw()

            # Plot KE distribution every 10 frames (adjust as needed)
            # if frame_count % 10 == 0:
            #     analysis.update_ke(self.particles)
            #     analysis.plot()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def handle_collisions(self):
        for i in range(len(self.particles)):
            for j in range(i+1, len(self.particles)):
                p1 = self.particles[i]
                p2 = self.particles[j]
                
                dx = p1.x - p2.x
                dy = p1.y - p2.y
                dist_sq = dx*dx + dy*dy
                rad = p1.radius + p2.radius
                

                if dist_sq == 0:
                    continue  # avoid division by zero

                if dist_sq < rad * rad:
                    dist = math.sqrt(dist_sq)
                    # compute unit direction/collision normal
                    nx = dx/dist
                    ny = dy/dist

                    # Penetration correction
                    overlap = rad - dist
                    correction_x = nx * (overlap/2)
                    correction_y = ny * (overlap/2)
                    p1.x += correction_x
                    p1.y += correction_y
                    p2.x -= correction_x
                    p2.y -= correction_y
                    
                    # Relative velocity 
                    # This gives velocity of particle 1 as seen from particle 2
                    rvx = p1.vx - p2.vx
                    rvy = p1.vy - p2.vy

                    # dot production of relative velocity & Normal 
                    vel_along_normal = rvx * nx + rvy * ny

                    if vel_along_normal > 0:
                        continue

                    # Only resolve if moving toward each other
                    # > 0 => particles are moving away from each other
                    if vel_along_normal < 0:
                        # swap velocities (equal mass approximation) -> 1D only
                        # p1.vx, p2.vx = p2.vx, p1.vx
                        # p1.vy, p2.vy = p2.vy, p1.vy
                        
                        # For 2D
                        # Compute tangent vector
                        tx = -ny
                        ty = nx
                        # Scalar projections onto n and t (tangential _|_)
                        # Dot prod -> V . n and V . t
                        # Magnitude of V in the direction of n and t
                        v1n = p1.vx * nx + p1.vy * ny
                        v1t = p1.vx * tx + p1.vy * ty
                        v2n = p2.vx * nx + p2.vy * ny
                        v2t = p2.vx * tx + p2.vy * ty
                        # Swap normal components
                        v1n, v2n = v2n, v1n
                        # Rebuild velocity V(vect) = Vn(vect) + Vt(vect)
                        # Vn = Vn(scalar) * n (unit vector / collision normal)
                        # Vt = Vt (scalar) * t (tangential vector)
                        p1.vx = v1n * nx + v1t * tx
                        p1.vy = v1n * ny + v1t * ty
                        p2.vx = v2n * nx + v2t * tx
                        p2.vy = v2n * ny + v2t * ty
                        
                     

if __name__ == '__main__':
    # Make a game instance, run the game.
    p1 = GasParticleSim()
    p1.run_sim()
