'''
   Author: Lan Jing Li
   
   Date: May 5, 2017
   
   Description: The main program contains the re-make version of Atari's "Break-Out!" game. However, asides from the original version, some enhancements were added to the game. The first one is that different bricks are worth different points. The amount of points each brick is worth increases as the location of the higher rows are harder to reach. The second enhancement I had made is cutting the width of the paddle in half when half of the bricks have been destroyed.
'''
# I - Import and Initialize
import pygame, myBreakOutSprites
pygame.init()
 
def main():
    # DISPLAY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Super Break-Out!")
 
    # ENTITIES
    background = pygame.image.load("spaceBackground.jpg")
    background = background.convert()
    screen.blit(background, (0, 0))

    x = 50
    y = 50
    brickLeft = 0

    #Create a list for each row of bricks
    brickRow1 = []
    brickRow2 = []
    brickRow3 = []
    brickRow4 = []
    brickRow5 = []
    brickRow6 = []

    #For loops to append bricks to each list
    for column in range(0, 18):
        brick1 = myBreakOutSprites.Brick (1, x + column * 30, y)
        brickRow1.append(brick1)

    for column in range(0, 18):
        brick2 = myBreakOutSprites.Brick (2, x + column * 30, y + 15)
        brickRow2.append(brick2)
    
    for column in range(0, 18):
        brick3 = myBreakOutSprites.Brick (3, x + column * 30, y + 30)
        brickRow3.append(brick3)
    
    for column in range(0, 18):
        brick4 = myBreakOutSprites.Brick (4, x + column * 30, y + 45)
        brickRow4.append(brick4)
    
    for column in range(0, 18):
        brick5 = myBreakOutSprites.Brick (5, x + column * 30, y + 60)
        brickRow5.append(brick5)
    
    for column in range(0, 18):
        brick6 = myBreakOutSprites.Brick (6, x + column * 30, y + 75)
        brickRow6.append(brick6)

    #Sprites for: player, ball, endzones, ScoreKeeper label and lifecounter label
    player = myBreakOutSprites.Player(screen)
    ball = myBreakOutSprites.Ball(screen)
    bottomEndzone = myBreakOutSprites.EndZone (screen, 479)
    topEndzone = myBreakOutSprites.EndZone (screen, 50)
    scoreKeeper = myBreakOutSprites.ScoreKeeper()
    lifeCounter = myBreakOutSprites.LifeCounter()

    #Create sprite groups
    brickGroup1 = pygame.sprite.Group(brickRow1)
    brickGroup2 = pygame.sprite.Group(brickRow2)
    brickGroup3 = pygame.sprite.Group(brickRow3)
    brickGroup4 = pygame.sprite.Group(brickRow4)
    brickGroup5 = pygame.sprite.Group(brickRow5)
    brickGroup6 = pygame.sprite.Group(brickRow6)

    allSprites = pygame.sprite.Group (brickRow1, brickRow2, brickRow3, brickRow4, brickRow5, brickRow6, scoreKeeper, lifeCounter, player, ball, topEndzone, bottomEndzone)

    # "Game Over" Image to Display After Game Loop Terminates 
    gameover = pygame.image.load ("gameOver.png")
    gameover = gameover.convert()

    #Background music and Sound Effects
    pygame.mixer.music.load("background music.mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    laser = pygame.mixer.Sound ("laser.ogg")
    laser.set_volume(0.6)

    # ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True
 
    # LOOP
    while keepGoing:
 
        # TIME
        clock.tick(30)
 
        # EVENT HANDLING: Player uses left and right arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event. type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.change_direction ((1,0))
                if event.key == pygame.K_RIGHT:
                    player.change_direction ((-1,0))
    
        #Adds certain amount of points to the score according the the brick hit. If two bricks are hit at the same time, two individual scores of the bricks are added.
        hitList1 = pygame.sprite.spritecollide(ball, brickGroup1, False)
        for hitBrick in hitList1:
            scoreKeeper.player1_scored(1)
            hitBrick.kill()
            brickLeft += 1
            laser.play()
        if len(hitList1) == 2 or len(hitList1) == 1:
            ball.change_direction()    
    
        #Adds certain amount of points to the score according the the brick hit. If two bricks are hit at the same time, two individual scores of the bricks are added.        
        hitList2 = pygame.sprite.spritecollide(ball, brickGroup2, False)
        for hitBrick in hitList2:
            scoreKeeper.player1_scored(2)
            hitBrick.kill()
            brickLeft += 1
            laser.play()
        if len(hitList2) == 2 or len(hitList2) == 1:
            ball.change_direction()
    
        #Adds certain amount of points to the score according the the brick hit. If two bricks are hit at the same time, two individual scores of the bricks are added.
        hitList3 = pygame.sprite.spritecollide(ball, brickGroup3, False)
        for hitBrick in hitList3:
            scoreKeeper.player1_scored(3)
            hitBrick.kill()
            brickLeft += 1
            laser.play()
        if len(hitList3) == 2 or len(hitList3) == 1:
            ball.change_direction()
    
        #Adds certain amount of points to the score according the the brick hit. If two bricks are hit at the same time, two individual scores of the bricks are added.
        hitList4 = pygame.sprite.spritecollide(ball, brickGroup4, False)
        for hitBrick in hitList4:
            scoreKeeper.player1_scored(4)
            hitBrick.kill()
            brickLeft += 1
            laser.play()
        if len(hitList4) == 2 or (hitList4) == 1:
            ball.change_direction()
    
        #Adds certain amount of points to the score according the the brick hit. If two bricks are hit at the same time, two individual scores of the bricks are added.
        hitList5 = pygame.sprite.spritecollide(ball, brickGroup5, False)
        for hitBrick in hitList5:
            scoreKeeper.player1_scored(5)
            hitBrick.kill()
            brickLeft += 1
            laser.play()
        if len(hitList5) == 2 or len(hitList5) == 1:       
            ball.change_direction()
    
        #Adds certain amount of points to the score according the the brick hit. If two bricks are hit at the same time, two individual scores of the bricks are added.
        hitList6 = pygame.sprite.spritecollide(ball, brickGroup6, False)
        for hitBrick in hitList6:
            scoreKeeper.player1_scored(6) 
            hitBrick.kill()
            brickLeft += 1
            laser.play()
        if len(hitList6) == 2 or len(hitList6) == 1:
            ball.change_direction()
    
        #Checks to see if the ball did NOT hit the paddle. One life will be deducted if so.
        if ball.rect.colliderect(bottomEndzone):
            lifeCounter.died()
            ball.change_direction()
    
        #Check for game over (losing - if player has 0 lives left)
        if lifeCounter.gameOver():
            pygame.mixer.music.fadeout (2000)
            keepGoing = False
    
        #Check for game over (winning - if the player has cleared all blocks)
        if scoreKeeper.winner():
            pygame.mixer.music.fadeout (2000)
            keepGoing = False
            
        #Check to see if the ball had hit the endzone, if so, change direction
        if ball.rect.colliderect(topEndzone):
            ball.change_direction()
    
        #Check to see if the ball had hit the endzone, if so, change direction
        if ball.rect.colliderect (player.rect):
            ball.change_direction()
            laser.play()
        
        #Check to see if half of the blocks are cleared, if so, the player board is cut in half
        if brickLeft == 54 or brickLeft == 55:
            player.half(screen)
    
        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)

    pygame.time.delay (3000)
    
    # Close the game window
    pygame.quit()   

# Call the main function
main()