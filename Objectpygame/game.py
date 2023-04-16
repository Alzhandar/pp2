import pygame

pygame.init()
W=700
H=400
FPS=15
clock=pygame.time.Clock()
screen=pygame.display.set_mode((W,H))
pygame.display.set_caption("Legend of the Hunter")
pygame.display.set_icon(pygame.image.load('static/icon.png'))

bg=pygame.image.load('static/d.png')
bg1=pygame.image.load('static/d.png')
bg2=pygame.image.load('static/d.png')
bg3=pygame.image.load('static/d.png')
left=[
    pygame.image.load('images/player_left/player_left1.png'),
    pygame.image.load('images/player_left/player_left2.png'),
    pygame.image.load('images/player_left/player_left3.png'),
    pygame.image.load('images/player_left/player_left4.png'),
]
right=[
    pygame.image.load('images/player_right/player_right1.png'),
    pygame.image.load('images/player_right/player_right2.png'),
    pygame.image.load('images/player_right/player_right3.png'),
    pygame.image.load('images/player_right/player_right4.png'),
]

scorpion=[
    pygame.image.load('images/scorpion/scorpion1.png'),
    pygame.image.load('images/scorpion/scorpion2.png'),
    pygame.image.load('images/scorpion/scorpion3.png'),
    pygame.image.load('images/scorpion/scorpion4.png'),
    pygame.image.load('images/scorpion/scorpion5.png'),
    pygame.image.load('images/scorpion/scorpion6.png'),
]
snake=[
    pygame.image.load('snake/snake1.png'),
    pygame.image.load('snake/snake2.png'),
    pygame.image.load('snake/snake3.png'),
    pygame.image.load('snake/snake4.png'),
    pygame.image.load('snake/snake5.png'),
    pygame.image.load('snake/snake6.png'),
    pygame.image.load('snake/snake7.png'),
    pygame.image.load('snake/snake8.png'),
    pygame.image.load('snake/snake9.png'),
    pygame.image.load('snake/snake10.png'),
    pygame.image.load('snake/snake11.png'),
    pygame.image.load('snake/snake12.png'),
]
for i in range(len(snake)):
    snake[i] = pygame.transform.flip(snake[i], True, False)
for i in range(len(snake)):
    snake[i] = pygame.transform.scale(snake[i], (int(snake[i].get_width() * 0.7), int(snake[i].get_height() * 0.7)))
snake_anim_count=0
snake_x=800
heart=pygame.image.load('images/heart.png')
heart = pygame.transform.scale(heart, (100, 100))
stars=pygame.image.load('images/nostars.png')
stars1=pygame.image.load('images/stars_1.png')
stars2=pygame.image.load('images/stars_2.png')
stars3=pygame.image.load('images/stars_3.png')
heart=pygame.image.load('images/heart.png')
weapons=pygame.image.load('static/weapons.png')
new_weapons = pygame.transform.scale(weapons, (90, 50))
weapons_speed=5


bg_sound=pygame.mixer.Sound('sounds/pustynya.mp3')
bg_sound1=pygame.mixer.Sound('sounds/8-bit.mp3')
bg_sound1.play()
bg_sound.play()
player_anim_count=0
scorpion_anim_count=0
running=True
bg_x=0
scorpion_x=700
player_speed=8
stars_pos=(W//2-30,50)
scorpion_speed=5
snake_speed=5
player_x=150
player_y=290
lives=3
scorpion_kills=0
is_jump=False
jump_count=9
gameplay=True
font = pygame.font.Font(None, 40)
font_restart=font.render('Restart',True,(225,0,0))
screen.blit(new_weapons,(W//2,500))
while running:

    screen.blit(bg,(bg_x,0))
    screen.blit(bg1,(bg_x+700,0))
    screen.blit(bg2,(bg_x+1400,0))
    screen.blit(bg3,(bg_x+2100,0))
    screen.blit(heart,(10,110))

    
    screen.blit(scorpion[scorpion_anim_count], (scorpion_x, 310))
    screen.blit(snake[snake_anim_count],(snake_x,310))
    screen.blit(scorpion[scorpion_anim_count],(900,310))

    player_rect=pygame.Rect(player_x, player_y, left[0].get_width(), left[0].get_height())
    if scorpion_x< -100:
        scorpion_x=700
        scorpion_anim_count=0
    
    scorpion_rect=scorpion[scorpion_anim_count].get_rect(topleft=(scorpion_x,310))
    snake_rect=snake[snake_anim_count].get_rect(topleft=(snake_x,310))
    if snake_x<-100:
        snake_x=1200
        snake_anim_count=0
    
    if player_rect.colliderect(scorpion_rect) and is_jump:
        scorpion_x = 700
        scorpion_kills+=1
        print("Scorpion killed")
    elif player_rect.colliderect(scorpion_rect) or player_rect.colliderect(snake_rect):
        snake_x=1000
        lives -= 1
        if lives == 0:
            running=False
          
        else:
            player_x = 150
            player_y = 290
            scorpion_x = 700
            scorpion_kills = 0
    lives_text = font.render(f"{lives}", True, (255, 255, 255))
    
    screen.blit(lives_text, (37, 127))
    if scorpion_anim_count == 5:
      scorpion_anim_count = 0
    else:
      scorpion_anim_count += 1
    scorpion_x -= scorpion_speed
    kills_text = font.render( str(scorpion_kills), True, (225, 225, 225))
    screen.blit(kills_text, (10, 10))

    if snake_anim_count==11:
        snake_anim_count=0
    else:
        snake_anim_count+=1
    snake_x-=snake_speed

    keys=pygame.key.get_pressed()
    if keys[pygame.K_a]:
        screen.blit(left[player_anim_count],(player_x,player_y))
    else:
        screen.blit(right[player_anim_count],(player_x,player_y))


    if keys[pygame.K_a] and player_x>50:
        player_x-=player_speed
    elif keys[pygame.K_d] and player_x<600:
        player_x+=player_speed

    if not is_jump:
        if keys[pygame.K_w]:
            is_jump=True
    else:
        if jump_count>=-9:
            if jump_count>0:
                player_y-=(jump_count**2)/2
            else:
                player_y+=(jump_count**2)/2
            jump_count-=1
        else:
            is_jump=False
            jump_count=9

    if player_anim_count==3:
        player_anim_count=0
    else:
        player_anim_count+=1


    bg_x-=2
    if bg_x==-2100:
        bg_x=0
    if scorpion_kills<=4:
        screen.blit(stars,stars_pos)
    elif scorpion_kills>=5 and scorpion_kills<10:
        screen.blit(stars1,stars_pos)
    elif scorpion_kills>=10 and scorpion_kills<15:
        screen.blit(stars2,stars_pos)
    else:
        screen.blit(stars3,stars_pos)

    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()