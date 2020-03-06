import pygame
pygame.init() # required to initialize python

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 50
y = 450
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10
run = True
while run:
    pygame.time.delay(100) # 100 ms delay
    for event in pygame.event.get(): # check of events which are actions from user
        if event.type == pygame.QUIT: # literally if you click 'X"
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if not isJump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - vel - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= jumpCount**2 * 0.5 * neg  # to the power of 2
            jumpCount -= 0
            # from 10-0 (jump increases) from -1 to -10 jump decreases back to original position due to neg sign
        else:
            isJump = False
            jumpCount = 10
    win.fill((0,0,0))
    pygame.draw.rect(win, (0,0,255), (x, y, width, height))
    pygame.display.update()


pygame.quit()
