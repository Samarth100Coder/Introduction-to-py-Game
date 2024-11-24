import pygame
pygame.init()
screen=pygame.display.set_mode((300,400))
pygame.display.set_caption('Adding image and background image')
background_image=pygame.transform.scale(
    pygame.image.load('download (9).jpg').convert(),
    (300,400))
penguin_image=pygame.transform.scale(
    pygame.image.load('download.jpg').convert_alpha(), (200,200))
penguin_rect=penguin_image.get_rect(center=(150,270))
text=pygame.font.Font(None,36).render('Hello World',True,pygame.Color('black'))
text_rect=text.get_rect(center=(150,310))
def game_loop():

    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.blit(background_image,(0,0))
        screen.blit(penguin_image,penguin_rect)
        screen.blit(text,text_rect)
  
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
game_loop()