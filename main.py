import pygame, sys
from settings import * 
from level import Level
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The Warrior's Strength")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

        self.level = Level()
    
    def draw_text(self, text, pos, color = (0,0,0)):
        
        lines = text.splitlines()
        for i, line in enumerate(lines):
            rendered_text = self.font.render(line, True, color)
            self.screen.blit(rendered_text, (pos[0] , pos[1] + i * 40))

    def show_controls(self):
        controls_text = """
        Welcome to The Warrior's Strength!
        
        Controls:
        Move: W/A/S/D
        Attack Weapon: SpaceBar
        Attack Magic: M Key
        Change Weapon : Q Key
        Change Magic : E Key

        Toggle Menu/Level Up: P Key
        Upgrade : Key SpaceBar while Menu Toggled

        Press any key to start the your Journey!
        """

        waiting = True
        while waiting :
            self.screen.fill("#92DE05")
            self.draw_text(controls_text, (50,50))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def run(self):
        
        self.show_controls()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOUR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()