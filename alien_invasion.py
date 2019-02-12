import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from alien import Alien


def run_game():
    """初始化并创建pygame对象"""
    pygame.init()
    # 实例化settings类
    ai_setting = Settings()
    # 创建一个名为screen的画板
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("大战外星人")
    # 实例化ship类
    ship = Ship(ai_setting, screen)
    # 创建用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    alien = Alien(ai_setting, screen)

    while True:
        gf.check_event(ai_setting, screen, ship, bullets)
        ship.update()
        # 调用bullets的update（）之后，会分别调用各个对象的update（）函数
        gf.update_bullet(bullets)
        gf.update_screen(ai_setting, screen, ship, alien, bullets)


run_game()

