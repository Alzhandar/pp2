import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600,300))
circle_speed = 20
circle_x = 300
circle_y = 150
icon =pygame.image.load('static/images/icon.png')
pygame.display.set_icon(icon)
running = True
while running:
    screen.fill((114,157,224))
    pygame.draw.circle(screen,'Red', (circle_x,circle_y), 25)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and circle_x > 50:
        circle_x -= circle_speed
    
    elif keys[pygame.K_RIGHT] and circle_x < 550:
        circle_x += circle_speed
    
    elif keys[pygame.K_DOWN] and circle_y < 260:
        circle_y += circle_speed
    
    elif keys[pygame.K_UP] and circle_y > 10:
        circle_y -= circle_speed
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()    
    clock.tick(15)
    pygame.display.update()