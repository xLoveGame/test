import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """创建外星人"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图片
        self.image = pygame .image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在最左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        """绘制外星人"""
        self.screen.blit(self.image, self.rect)
