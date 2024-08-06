import pygame
import sys
import yaml

from core.layout.main_window import MainWindow


def main():
    with open("setting.yml") as fp:
        cfg = yaml.load(fp, Loader=yaml.FullLoader)

    pygame.init()
    SCREEN = pygame.display.set_mode((cfg["window"]["WINDOW_WIDTH"], cfg["window"]["WINDOW_HEIGHT"]))
    CLOCK = pygame.time.Clock()
    SCREEN.fill((200, 200, 200))

    mw = MainWindow()

    while True:
        mw.drawGrid(SCREEN)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
