import pygame
import random
import math

pygame.init()

# Screen configuration
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fogos de Artifício Interativos")

# Colors
BLACK = (0, 0, 0)
HEART_COLORS = [
    (255, 0, 0),
    (255, 20, 147),
    (255, 105, 180),
    (148, 0, 211),
    (75, 0, 130),
    (255, 140, 0),
    (255, 215, 0),
    (0, 255, 127),
]

class Particle:
    def __init__(self, x, y, angle, speed, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.color = color
        self.life = random.randint(40, 100)

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.speed *= 0.95
        self.life -= 1

    def draw(self, screen):
        if self.life > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)

class Firework:
    def __init__(self, x=None, y=None):
        self.x = x if x is not None else random.randint(100, WIDTH - 100)
        self.y = y if y is not None else HEIGHT
        self.color = random.choice(HEART_COLORS)
        self.speed = random.uniform(7, 20)
        self.exploded = False
        self.particles = []
        self.max_height = random.randint(180, 350)

    def update(self):
        if not self.exploded:
            self.y -= self.speed
            self.speed -= 0.25
            if self.speed <= 0 or self.y <= self.max_height:
                self.explode()
        else:
            for p in self.particles:
                p.update()

    def draw(self, screen):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)
        else:
            for p in self.particles:
                p.draw(screen)

    def explode(self):
        self.exploded = True
        num_particls = 220
        scale = 12 

        for i in range(num_particls):
            t = (2 * math.pi * i) / num_particls

            x = 16 * math.sin(t) ** 3
            y = (13 *math.cos(t)
                 - 5 * math)

def main():
    running = True
    clock = pygame.time.Clock()
    fireworks = []

    while running:
        screen.fill(BLACK)

        if random.randint(1, 30) == 1:
            fireworks.append(Firework())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for fw in fireworks[:]:
            fw.update()
            fw.draw(screen)
            if fw.exploded and all(p.life <= 0 for p in fw.particles):
                fireworks.remove(fw)

        pygame.display.flip()
        clock.tick(40)

    pygame.quit()

if __name__ == "__main__":
    main()
