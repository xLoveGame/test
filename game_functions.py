import pygame
import sys
from bullet import Bullet
"""此文件用来存储游戏相关控制函数"""
"""
            左右移动的控制
            KEYDOWN为按下按键
            KEYUP为松开按键  
            每次按下的记为事件  
"""


def check_down_event(event, ai_settings, screen, ship, bullets):
    """检测按键按下"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_up_event(event, ship):
    """"检测按键松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_event(ai_settings, screen, ship, bullets):
    """响应按键和鼠标"""
    for event in pygame.event.get():        # 用event.get()函数获得事件
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_up_event(event, ship)


def update_bullet(bullets):
    """"更新子弹位置"""
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """若没到限制就发射一发子弹"""
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, alien, bullets):
    """每次刷新屏幕和船， 注意，这个函数才是绘制新的效果的函数"""
    screen.fill(ai_settings.bg_color)       # 设置背景颜色
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()                           # 把船画在背景上
    alien.blitme()                          # 画出外星人
    """让刷新显示出来"""
    pygame.display.flip()
