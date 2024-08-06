import yaml
import pygame
import os


class MainWindow:

    def __init__(self):
        with open(os.path.join(os.getcwd(), "setting.yml")) as fp:
            self.cfg = yaml.load(fp, Loader=yaml.FullLoader)
        print(self.cfg["window"])

    def drawGrid(self, __screen):
        blockSize = self.cfg["window"]["blockSize"]
        for x in range(0, self.cfg["window"]["WINDOW_WIDTH"], blockSize):
            for y in range(0, self.cfg["window"]["WINDOW_HEIGHT"], blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(__screen, (0, 0, 0), rect, 1)
