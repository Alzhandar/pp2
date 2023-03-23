import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,300))
speed = 20
x = 300
y = 150
icon =pygame.image.load('static/images/icon.png')
pygame.display.set_icon(icon)
running = True
while running:
    screen.fill((114,157,224))
    pygame.draw.circle(screen,'Red', (x,y), 25)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 50:
        x -= speed
    elif keys[pygame.K_RIGHT] and x < 550:
        x += speed
    
    elif keys[pygame.K_DOWN] and y < 260:
        y += speed
    
    elif keys[pygame.K_UP] and y > 10:
        y -= speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()    
    clock.tick(15)
    pygame.display.update()