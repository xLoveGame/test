import pygame


class Ship:
    """船"""
    def __init__(self, ai_settings, screen):
        """初始化船的位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 存储小数值
        self.center = float(self.rect.centerx)
        """移动标志"""
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据标志移动飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据center的值修改centerx
        self.rect.centerx = self.center

    def blitme(self):
        """Draws a source Surface onto this Surface, 前面screen就是surface"""
        self.screen.blit(self.image, self.rect)



