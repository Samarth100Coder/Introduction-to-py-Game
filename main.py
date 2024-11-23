import pygame
pygame.init()
screen=pygame.display.set_mode((300,400))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
pygame.display.set_caption('Adding image and background image')
background_image=pygame.transform.scale(
    pygame.image.load('download (9).jpg').convert(),
    (300,400))
penguin_image=pygame.transform.scale(
    pygame.image.load('download.jpg').convert_alpha(), (200,200))
penguin_rect=penguin_image.get_rect(center=(150,370))
text=pygame.font.Font(None,36).render('Hello World',True,
                                      pygame.Color('black'))
text_rect=text.get_rect(center=(150,310))