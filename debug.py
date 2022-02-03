import pygame
font = pygame.font.Font(None,30)


def debug(info,y = 10, x=10):
    display_surface = pygame.display.get_surface()
    debug = font.render(str(info),True,'White')
    debug = debug_surf.get_react(topleft = (x,y))
    pygame.draw.rect(display_surface,'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)