import pygame

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Player Movement')
clock = pygame.time.Clock()
REFRESH_RATE = 120

# Load images
background = pygame.image.load(r"C:\Users\User\OneDrive\שולחן העבודה\cours.py\1\tt.png").convert()
background = pygame.transform.scale(background, (screen_width, screen_height))
player_img = pygame.image.load(r"C:\Users\User\OneDrive\שולחן העבודה\cours.py\playr.png").convert_alpha()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height // 2))
        self.velocity = pygame.Vector2(0, 0)



# Create player
player = Player()
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # Clear the screen and draw the background
    screen.blit(background, (0, 0))

    # Update and draw sprites
    all_sprites_list.update()
    all_sprites_list.draw(screen)

    # Update the display
    pygame.display.flip()

    # Maintain the refresh rate
    clock.tick(REFRESH_RATE)

# Quit Pygame
pygame.quit()
